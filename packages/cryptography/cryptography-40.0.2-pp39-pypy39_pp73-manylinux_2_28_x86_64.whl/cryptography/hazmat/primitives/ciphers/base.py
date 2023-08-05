# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.


import abc
import typing

from cryptography.exceptions import (
    AlreadyFinalized,
    AlreadyUpdated,
    NotYetFinalized,
)
from cryptography.hazmat.primitives._cipheralgorithm import CipherAlgorithm
from cryptography.hazmat.primitives.ciphers import modes

if typing.TYPE_CHECKING:
    from cryptography.hazmat.backends.openssl.ciphers import (
        _CipherContext as _BackendCipherContext,
    )


class CipherContext(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, data: bytes) -> bytes:
        """
        Processes the provided bytes through the cipher and returns the results
        as bytes.
        """

    @abc.abstractmethod
    def update_into(self, data: bytes, buf: bytes) -> int:
        """
        Processes the provided bytes and writes the resulting data into the
        provided buffer. Returns the number of bytes written.
        """

    @abc.abstractmethod
    def finalize(self) -> bytes:
        """
        Returns the results of processing the final block as bytes.
        """


class AEADCipherContext(CipherContext, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def authenticate_additional_data(self, data: bytes) -> None:
        """
        Authenticates the provided bytes.
        """


class AEADDecryptionContext(AEADCipherContext, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def finalize_with_tag(self, tag: bytes) -> bytes:
        """
        Returns the results of processing the final block as bytes and allows
        delayed passing of the authentication tag.
        """


class AEADEncryptionContext(AEADCipherContext, metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def tag(self) -> bytes:
        """
        Returns tag bytes. This is only available after encryption is
        finalized.
        """


Mode = typing.TypeVar(
    "Mode", bound=typing.Optional[modes.Mode], covariant=True
)


class Cipher(typing.Generic[Mode]):
    def __init__(
        self,
        algorithm: CipherAlgorithm,
        mode: Mode,
        backend: typing.Any = None,
    ) -> None:
        if not isinstance(algorithm, CipherAlgorithm):
            raise TypeError("Expected interface of CipherAlgorithm.")

        if mode is not None:
            # mypy needs this assert to narrow the type from our generic
            # type. Maybe it won't some time in the future.
            assert isinstance(mode, modes.Mode)
            mode.validate_for_algorithm(algorithm)

        self.algorithm = algorithm
        self.mode = mode

    @typing.overload
    def encryptor(
        self: "Cipher[modes.ModeWithAuthenticationTag]",
    ) -> AEADEncryptionContext:
        ...

    @typing.overload
    def encryptor(
        self: "_CIPHER_TYPE",
    ) -> CipherContext:
        ...

    def encryptor(self):
        if isinstance(self.mode, modes.ModeWithAuthenticationTag):
            if self.mode.tag is not None:
                raise ValueError(
                    "Authentication tag must be None when encrypting."
                )
        from cryptography.hazmat.backends.openssl.backend import backend

        ctx = backend.create_symmetric_encryption_ctx(
            self.algorithm, self.mode
        )
        return self._wrap_ctx(ctx, encrypt=True)

    @typing.overload
    def decryptor(
        self: "Cipher[modes.ModeWithAuthenticationTag]",
    ) -> AEADDecryptionContext:
        ...

    @typing.overload
    def decryptor(
        self: "_CIPHER_TYPE",
    ) -> CipherContext:
        ...

    def decryptor(self):
        from cryptography.hazmat.backends.openssl.backend import backend

        ctx = backend.create_symmetric_decryption_ctx(
            self.algorithm, self.mode
        )
        return self._wrap_ctx(ctx, encrypt=False)

    def _wrap_ctx(
        self, ctx: "_BackendCipherContext", encrypt: bool
    ) -> typing.Union[
        AEADEncryptionContext, AEADDecryptionContext, CipherContext
    ]:
        if isinstance(self.mode, modes.ModeWithAuthenticationTag):
            if encrypt:
                return _AEADEncryptionContext(ctx)
            else:
                return _AEADDecryptionContext(ctx)
        else:
            return _CipherContext(ctx)


_CIPHER_TYPE = Cipher[
    typing.Union[
        modes.ModeWithNonce,
        modes.ModeWithTweak,
        None,
        modes.ECB,
        modes.ModeWithInitializationVector,
    ]
]


class _CipherContext(CipherContext):
    _ctx: typing.Optional["_BackendCipherContext"]

    def __init__(self, ctx: "_BackendCipherContext") -> None:
        self._ctx = ctx

    def update(self, data: bytes) -> bytes:
        if self._ctx is None:
            raise AlreadyFinalized("Context was already finalized.")
        return self._ctx.update(data)

    def update_into(self, data: bytes, buf: bytes) -> int:
        if self._ctx is None:
            raise AlreadyFinalized("Context was already finalized.")
        return self._ctx.update_into(data, buf)

    def finalize(self) -> bytes:
        if self._ctx is None:
            raise AlreadyFinalized("Context was already finalized.")
        data = self._ctx.finalize()
        self._ctx = None
        return data


class _AEADCipherContext(AEADCipherContext):
    _ctx: typing.Optional["_BackendCipherContext"]
    _tag: typing.Optional[bytes]

    def __init__(self, ctx: "_BackendCipherContext") -> None:
        self._ctx = ctx
        self._bytes_processed = 0
        self._aad_bytes_processed = 0
        self._tag = None
        self._updated = False

    def _check_limit(self, data_size: int) -> None:
        if self._ctx is None:
            raise AlreadyFinalized("Context was already finalized.")
        self._updated = True
        self._bytes_processed += data_size
        if self._bytes_processed > self._ctx._mode._MAX_ENCRYPTED_BYTES:
            raise ValueError(
                "{} has a maximum encrypted byte limit of {}".format(
                    self._ctx._mode.name, self._ctx._mode._MAX_ENCRYPTED_BYTES
                )
            )

    def update(self, data: bytes) -> bytes:
        self._check_limit(len(data))
        # mypy needs this assert even though _check_limit already checked
        assert self._ctx is not None
        return self._ctx.update(data)

    def update_into(self, data: bytes, buf: bytes) -> int:
        self._check_limit(len(data))
        # mypy needs this assert even though _check_limit already checked
        assert self._ctx is not None
        return self._ctx.update_into(data, buf)

    def finalize(self) -> bytes:
        if self._ctx is None:
            raise AlreadyFinalized("Context was already finalized.")
        data = self._ctx.finalize()
        self._tag = self._ctx.tag
        self._ctx = None
        return data

    def authenticate_additional_data(self, data: bytes) -> None:
        if self._ctx is None:
            raise AlreadyFinalized("Context was already finalized.")
        if self._updated:
            raise AlreadyUpdated("Update has been called on this context.")

        self._aad_bytes_processed += len(data)
        if self._aad_bytes_processed > self._ctx._mode._MAX_AAD_BYTES:
            raise ValueError(
                "{} has a maximum AAD byte limit of {}".format(
                    self._ctx._mode.name, self._ctx._mode._MAX_AAD_BYTES
                )
            )

        self._ctx.authenticate_additional_data(data)


class _AEADDecryptionContext(_AEADCipherContext, AEADDecryptionContext):
    def finalize_with_tag(self, tag: bytes) -> bytes:
        if self._ctx is None:
            raise AlreadyFinalized("Context was already finalized.")
        data = self._ctx.finalize_with_tag(tag)
        self._tag = self._ctx.tag
        self._ctx = None
        return data


class _AEADEncryptionContext(_AEADCipherContext, AEADEncryptionContext):
    @property
    def tag(self) -> bytes:
        if self._ctx is not None:
            raise NotYetFinalized(
                "You must finalize encryption before " "getting the tag."
            )
        assert self._tag is not None
        return self._tag
