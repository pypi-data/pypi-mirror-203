# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.


import binascii
import enum
import os
import re
import typing
import warnings
from base64 import encodebytes as _base64_encode

from cryptography import utils
from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import (
    dsa,
    ec,
    ed25519,
    padding,
    rsa,
)
from cryptography.hazmat.primitives.asymmetric import utils as asym_utils
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    KeySerializationEncryption,
    NoEncryption,
    PrivateFormat,
    PublicFormat,
    _KeySerializationEncryption,
)

try:
    from bcrypt import kdf as _bcrypt_kdf

    _bcrypt_supported = True
except ImportError:
    _bcrypt_supported = False

    def _bcrypt_kdf(
        password: bytes,
        salt: bytes,
        desired_key_bytes: int,
        rounds: int,
        ignore_few_rounds: bool = False,
    ) -> bytes:
        raise UnsupportedAlgorithm("Need bcrypt module")


_SSH_ED25519 = b"ssh-ed25519"
_SSH_RSA = b"ssh-rsa"
_SSH_DSA = b"ssh-dss"
_ECDSA_NISTP256 = b"ecdsa-sha2-nistp256"
_ECDSA_NISTP384 = b"ecdsa-sha2-nistp384"
_ECDSA_NISTP521 = b"ecdsa-sha2-nistp521"
_CERT_SUFFIX = b"-cert-v01@openssh.com"

# These are not key types, only algorithms, so they cannot appear
# as a public key type
_SSH_RSA_SHA256 = b"rsa-sha2-256"
_SSH_RSA_SHA512 = b"rsa-sha2-512"

_SSH_PUBKEY_RC = re.compile(rb"\A(\S+)[ \t]+(\S+)")
_SK_MAGIC = b"openssh-key-v1\0"
_SK_START = b"-----BEGIN OPENSSH PRIVATE KEY-----"
_SK_END = b"-----END OPENSSH PRIVATE KEY-----"
_BCRYPT = b"bcrypt"
_NONE = b"none"
_DEFAULT_CIPHER = b"aes256-ctr"
_DEFAULT_ROUNDS = 16

# re is only way to work on bytes-like data
_PEM_RC = re.compile(_SK_START + b"(.*?)" + _SK_END, re.DOTALL)

# padding for max blocksize
_PADDING = memoryview(bytearray(range(1, 1 + 16)))

# ciphers that are actually used in key wrapping
_SSH_CIPHERS: typing.Dict[
    bytes,
    typing.Tuple[
        typing.Type[algorithms.AES],
        int,
        typing.Union[typing.Type[modes.CTR], typing.Type[modes.CBC]],
        int,
    ],
] = {
    b"aes256-ctr": (algorithms.AES, 32, modes.CTR, 16),
    b"aes256-cbc": (algorithms.AES, 32, modes.CBC, 16),
}

# map local curve name to key type
_ECDSA_KEY_TYPE = {
    "secp256r1": _ECDSA_NISTP256,
    "secp384r1": _ECDSA_NISTP384,
    "secp521r1": _ECDSA_NISTP521,
}


def _get_ssh_key_type(
    key: typing.Union["SSHPrivateKeyTypes", "SSHPublicKeyTypes"]
) -> bytes:
    if isinstance(key, ec.EllipticCurvePrivateKey):
        key_type = _ecdsa_key_type(key.public_key())
    elif isinstance(key, ec.EllipticCurvePublicKey):
        key_type = _ecdsa_key_type(key)
    elif isinstance(key, (rsa.RSAPrivateKey, rsa.RSAPublicKey)):
        key_type = _SSH_RSA
    elif isinstance(key, (dsa.DSAPrivateKey, dsa.DSAPublicKey)):
        key_type = _SSH_DSA
    elif isinstance(
        key, (ed25519.Ed25519PrivateKey, ed25519.Ed25519PublicKey)
    ):
        key_type = _SSH_ED25519
    else:
        raise ValueError("Unsupported key type")

    return key_type


def _ecdsa_key_type(public_key: ec.EllipticCurvePublicKey) -> bytes:
    """Return SSH key_type and curve_name for private key."""
    curve = public_key.curve
    if curve.name not in _ECDSA_KEY_TYPE:
        raise ValueError(
            f"Unsupported curve for ssh private key: {curve.name!r}"
        )
    return _ECDSA_KEY_TYPE[curve.name]


def _ssh_pem_encode(
    data: bytes,
    prefix: bytes = _SK_START + b"\n",
    suffix: bytes = _SK_END + b"\n",
) -> bytes:
    return b"".join([prefix, _base64_encode(data), suffix])


def _check_block_size(data: bytes, block_len: int) -> None:
    """Require data to be full blocks"""
    if not data or len(data) % block_len != 0:
        raise ValueError("Corrupt data: missing padding")


def _check_empty(data: bytes) -> None:
    """All data should have been parsed."""
    if data:
        raise ValueError("Corrupt data: unparsed data")


def _init_cipher(
    ciphername: bytes,
    password: typing.Optional[bytes],
    salt: bytes,
    rounds: int,
) -> Cipher[typing.Union[modes.CBC, modes.CTR]]:
    """Generate key + iv and return cipher."""
    if not password:
        raise ValueError("Key is password-protected.")

    algo, key_len, mode, iv_len = _SSH_CIPHERS[ciphername]
    seed = _bcrypt_kdf(password, salt, key_len + iv_len, rounds, True)
    return Cipher(algo(seed[:key_len]), mode(seed[key_len:]))


def _get_u32(data: memoryview) -> typing.Tuple[int, memoryview]:
    """Uint32"""
    if len(data) < 4:
        raise ValueError("Invalid data")
    return int.from_bytes(data[:4], byteorder="big"), data[4:]


def _get_u64(data: memoryview) -> typing.Tuple[int, memoryview]:
    """Uint64"""
    if len(data) < 8:
        raise ValueError("Invalid data")
    return int.from_bytes(data[:8], byteorder="big"), data[8:]


def _get_sshstr(data: memoryview) -> typing.Tuple[memoryview, memoryview]:
    """Bytes with u32 length prefix"""
    n, data = _get_u32(data)
    if n > len(data):
        raise ValueError("Invalid data")
    return data[:n], data[n:]


def _get_mpint(data: memoryview) -> typing.Tuple[int, memoryview]:
    """Big integer."""
    val, data = _get_sshstr(data)
    if val and val[0] > 0x7F:
        raise ValueError("Invalid data")
    return int.from_bytes(val, "big"), data


def _to_mpint(val: int) -> bytes:
    """Storage format for signed bigint."""
    if val < 0:
        raise ValueError("negative mpint not allowed")
    if not val:
        return b""
    nbytes = (val.bit_length() + 8) // 8
    return utils.int_to_bytes(val, nbytes)


class _FragList:
    """Build recursive structure without data copy."""

    flist: typing.List[bytes]

    def __init__(
        self, init: typing.Optional[typing.List[bytes]] = None
    ) -> None:
        self.flist = []
        if init:
            self.flist.extend(init)

    def put_raw(self, val: bytes) -> None:
        """Add plain bytes"""
        self.flist.append(val)

    def put_u32(self, val: int) -> None:
        """Big-endian uint32"""
        self.flist.append(val.to_bytes(length=4, byteorder="big"))

    def put_u64(self, val: int) -> None:
        """Big-endian uint64"""
        self.flist.append(val.to_bytes(length=8, byteorder="big"))

    def put_sshstr(self, val: typing.Union[bytes, "_FragList"]) -> None:
        """Bytes prefixed with u32 length"""
        if isinstance(val, (bytes, memoryview, bytearray)):
            self.put_u32(len(val))
            self.flist.append(val)
        else:
            self.put_u32(val.size())
            self.flist.extend(val.flist)

    def put_mpint(self, val: int) -> None:
        """Big-endian bigint prefixed with u32 length"""
        self.put_sshstr(_to_mpint(val))

    def size(self) -> int:
        """Current number of bytes"""
        return sum(map(len, self.flist))

    def render(self, dstbuf: memoryview, pos: int = 0) -> int:
        """Write into bytearray"""
        for frag in self.flist:
            flen = len(frag)
            start, pos = pos, pos + flen
            dstbuf[start:pos] = frag
        return pos

    def tobytes(self) -> bytes:
        """Return as bytes"""
        buf = memoryview(bytearray(self.size()))
        self.render(buf)
        return buf.tobytes()


class _SSHFormatRSA:
    """Format for RSA keys.

    Public:
        mpint e, n
    Private:
        mpint n, e, d, iqmp, p, q
    """

    def get_public(self, data: memoryview):
        """RSA public fields"""
        e, data = _get_mpint(data)
        n, data = _get_mpint(data)
        return (e, n), data

    def load_public(
        self, data: memoryview
    ) -> typing.Tuple[rsa.RSAPublicKey, memoryview]:
        """Make RSA public key from data."""
        (e, n), data = self.get_public(data)
        public_numbers = rsa.RSAPublicNumbers(e, n)
        public_key = public_numbers.public_key()
        return public_key, data

    def load_private(
        self, data: memoryview, pubfields
    ) -> typing.Tuple[rsa.RSAPrivateKey, memoryview]:
        """Make RSA private key from data."""
        n, data = _get_mpint(data)
        e, data = _get_mpint(data)
        d, data = _get_mpint(data)
        iqmp, data = _get_mpint(data)
        p, data = _get_mpint(data)
        q, data = _get_mpint(data)

        if (e, n) != pubfields:
            raise ValueError("Corrupt data: rsa field mismatch")
        dmp1 = rsa.rsa_crt_dmp1(d, p)
        dmq1 = rsa.rsa_crt_dmq1(d, q)
        public_numbers = rsa.RSAPublicNumbers(e, n)
        private_numbers = rsa.RSAPrivateNumbers(
            p, q, d, dmp1, dmq1, iqmp, public_numbers
        )
        private_key = private_numbers.private_key()
        return private_key, data

    def encode_public(
        self, public_key: rsa.RSAPublicKey, f_pub: _FragList
    ) -> None:
        """Write RSA public key"""
        pubn = public_key.public_numbers()
        f_pub.put_mpint(pubn.e)
        f_pub.put_mpint(pubn.n)

    def encode_private(
        self, private_key: rsa.RSAPrivateKey, f_priv: _FragList
    ) -> None:
        """Write RSA private key"""
        private_numbers = private_key.private_numbers()
        public_numbers = private_numbers.public_numbers

        f_priv.put_mpint(public_numbers.n)
        f_priv.put_mpint(public_numbers.e)

        f_priv.put_mpint(private_numbers.d)
        f_priv.put_mpint(private_numbers.iqmp)
        f_priv.put_mpint(private_numbers.p)
        f_priv.put_mpint(private_numbers.q)


class _SSHFormatDSA:
    """Format for DSA keys.

    Public:
        mpint p, q, g, y
    Private:
        mpint p, q, g, y, x
    """

    def get_public(
        self, data: memoryview
    ) -> typing.Tuple[typing.Tuple, memoryview]:
        """DSA public fields"""
        p, data = _get_mpint(data)
        q, data = _get_mpint(data)
        g, data = _get_mpint(data)
        y, data = _get_mpint(data)
        return (p, q, g, y), data

    def load_public(
        self, data: memoryview
    ) -> typing.Tuple[dsa.DSAPublicKey, memoryview]:
        """Make DSA public key from data."""
        (p, q, g, y), data = self.get_public(data)
        parameter_numbers = dsa.DSAParameterNumbers(p, q, g)
        public_numbers = dsa.DSAPublicNumbers(y, parameter_numbers)
        self._validate(public_numbers)
        public_key = public_numbers.public_key()
        return public_key, data

    def load_private(
        self, data: memoryview, pubfields
    ) -> typing.Tuple[dsa.DSAPrivateKey, memoryview]:
        """Make DSA private key from data."""
        (p, q, g, y), data = self.get_public(data)
        x, data = _get_mpint(data)

        if (p, q, g, y) != pubfields:
            raise ValueError("Corrupt data: dsa field mismatch")
        parameter_numbers = dsa.DSAParameterNumbers(p, q, g)
        public_numbers = dsa.DSAPublicNumbers(y, parameter_numbers)
        self._validate(public_numbers)
        private_numbers = dsa.DSAPrivateNumbers(x, public_numbers)
        private_key = private_numbers.private_key()
        return private_key, data

    def encode_public(
        self, public_key: dsa.DSAPublicKey, f_pub: _FragList
    ) -> None:
        """Write DSA public key"""
        public_numbers = public_key.public_numbers()
        parameter_numbers = public_numbers.parameter_numbers
        self._validate(public_numbers)

        f_pub.put_mpint(parameter_numbers.p)
        f_pub.put_mpint(parameter_numbers.q)
        f_pub.put_mpint(parameter_numbers.g)
        f_pub.put_mpint(public_numbers.y)

    def encode_private(
        self, private_key: dsa.DSAPrivateKey, f_priv: _FragList
    ) -> None:
        """Write DSA private key"""
        self.encode_public(private_key.public_key(), f_priv)
        f_priv.put_mpint(private_key.private_numbers().x)

    def _validate(self, public_numbers: dsa.DSAPublicNumbers) -> None:
        parameter_numbers = public_numbers.parameter_numbers
        if parameter_numbers.p.bit_length() != 1024:
            raise ValueError("SSH supports only 1024 bit DSA keys")


class _SSHFormatECDSA:
    """Format for ECDSA keys.

    Public:
        str curve
        bytes point
    Private:
        str curve
        bytes point
        mpint secret
    """

    def __init__(self, ssh_curve_name: bytes, curve: ec.EllipticCurve):
        self.ssh_curve_name = ssh_curve_name
        self.curve = curve

    def get_public(
        self, data: memoryview
    ) -> typing.Tuple[typing.Tuple, memoryview]:
        """ECDSA public fields"""
        curve, data = _get_sshstr(data)
        point, data = _get_sshstr(data)
        if curve != self.ssh_curve_name:
            raise ValueError("Curve name mismatch")
        if point[0] != 4:
            raise NotImplementedError("Need uncompressed point")
        return (curve, point), data

    def load_public(
        self, data: memoryview
    ) -> typing.Tuple[ec.EllipticCurvePublicKey, memoryview]:
        """Make ECDSA public key from data."""
        (curve_name, point), data = self.get_public(data)
        public_key = ec.EllipticCurvePublicKey.from_encoded_point(
            self.curve, point.tobytes()
        )
        return public_key, data

    def load_private(
        self, data: memoryview, pubfields
    ) -> typing.Tuple[ec.EllipticCurvePrivateKey, memoryview]:
        """Make ECDSA private key from data."""
        (curve_name, point), data = self.get_public(data)
        secret, data = _get_mpint(data)

        if (curve_name, point) != pubfields:
            raise ValueError("Corrupt data: ecdsa field mismatch")
        private_key = ec.derive_private_key(secret, self.curve)
        return private_key, data

    def encode_public(
        self, public_key: ec.EllipticCurvePublicKey, f_pub: _FragList
    ) -> None:
        """Write ECDSA public key"""
        point = public_key.public_bytes(
            Encoding.X962, PublicFormat.UncompressedPoint
        )
        f_pub.put_sshstr(self.ssh_curve_name)
        f_pub.put_sshstr(point)

    def encode_private(
        self, private_key: ec.EllipticCurvePrivateKey, f_priv: _FragList
    ) -> None:
        """Write ECDSA private key"""
        public_key = private_key.public_key()
        private_numbers = private_key.private_numbers()

        self.encode_public(public_key, f_priv)
        f_priv.put_mpint(private_numbers.private_value)


class _SSHFormatEd25519:
    """Format for Ed25519 keys.

    Public:
        bytes point
    Private:
        bytes point
        bytes secret_and_point
    """

    def get_public(
        self, data: memoryview
    ) -> typing.Tuple[typing.Tuple, memoryview]:
        """Ed25519 public fields"""
        point, data = _get_sshstr(data)
        return (point,), data

    def load_public(
        self, data: memoryview
    ) -> typing.Tuple[ed25519.Ed25519PublicKey, memoryview]:
        """Make Ed25519 public key from data."""
        (point,), data = self.get_public(data)
        public_key = ed25519.Ed25519PublicKey.from_public_bytes(
            point.tobytes()
        )
        return public_key, data

    def load_private(
        self, data: memoryview, pubfields
    ) -> typing.Tuple[ed25519.Ed25519PrivateKey, memoryview]:
        """Make Ed25519 private key from data."""
        (point,), data = self.get_public(data)
        keypair, data = _get_sshstr(data)

        secret = keypair[:32]
        point2 = keypair[32:]
        if point != point2 or (point,) != pubfields:
            raise ValueError("Corrupt data: ed25519 field mismatch")
        private_key = ed25519.Ed25519PrivateKey.from_private_bytes(secret)
        return private_key, data

    def encode_public(
        self, public_key: ed25519.Ed25519PublicKey, f_pub: _FragList
    ) -> None:
        """Write Ed25519 public key"""
        raw_public_key = public_key.public_bytes(
            Encoding.Raw, PublicFormat.Raw
        )
        f_pub.put_sshstr(raw_public_key)

    def encode_private(
        self, private_key: ed25519.Ed25519PrivateKey, f_priv: _FragList
    ) -> None:
        """Write Ed25519 private key"""
        public_key = private_key.public_key()
        raw_private_key = private_key.private_bytes(
            Encoding.Raw, PrivateFormat.Raw, NoEncryption()
        )
        raw_public_key = public_key.public_bytes(
            Encoding.Raw, PublicFormat.Raw
        )
        f_keypair = _FragList([raw_private_key, raw_public_key])

        self.encode_public(public_key, f_priv)
        f_priv.put_sshstr(f_keypair)


_KEY_FORMATS = {
    _SSH_RSA: _SSHFormatRSA(),
    _SSH_DSA: _SSHFormatDSA(),
    _SSH_ED25519: _SSHFormatEd25519(),
    _ECDSA_NISTP256: _SSHFormatECDSA(b"nistp256", ec.SECP256R1()),
    _ECDSA_NISTP384: _SSHFormatECDSA(b"nistp384", ec.SECP384R1()),
    _ECDSA_NISTP521: _SSHFormatECDSA(b"nistp521", ec.SECP521R1()),
}


def _lookup_kformat(key_type: bytes):
    """Return valid format or throw error"""
    if not isinstance(key_type, bytes):
        key_type = memoryview(key_type).tobytes()
    if key_type in _KEY_FORMATS:
        return _KEY_FORMATS[key_type]
    raise UnsupportedAlgorithm(f"Unsupported key type: {key_type!r}")


SSHPrivateKeyTypes = typing.Union[
    ec.EllipticCurvePrivateKey,
    rsa.RSAPrivateKey,
    dsa.DSAPrivateKey,
    ed25519.Ed25519PrivateKey,
]


def load_ssh_private_key(
    data: bytes,
    password: typing.Optional[bytes],
    backend: typing.Any = None,
) -> SSHPrivateKeyTypes:
    """Load private key from OpenSSH custom encoding."""
    utils._check_byteslike("data", data)
    if password is not None:
        utils._check_bytes("password", password)

    m = _PEM_RC.search(data)
    if not m:
        raise ValueError("Not OpenSSH private key format")
    p1 = m.start(1)
    p2 = m.end(1)
    data = binascii.a2b_base64(memoryview(data)[p1:p2])
    if not data.startswith(_SK_MAGIC):
        raise ValueError("Not OpenSSH private key format")
    data = memoryview(data)[len(_SK_MAGIC) :]

    # parse header
    ciphername, data = _get_sshstr(data)
    kdfname, data = _get_sshstr(data)
    kdfoptions, data = _get_sshstr(data)
    nkeys, data = _get_u32(data)
    if nkeys != 1:
        raise ValueError("Only one key supported")

    # load public key data
    pubdata, data = _get_sshstr(data)
    pub_key_type, pubdata = _get_sshstr(pubdata)
    kformat = _lookup_kformat(pub_key_type)
    pubfields, pubdata = kformat.get_public(pubdata)
    _check_empty(pubdata)

    # load secret data
    edata, data = _get_sshstr(data)
    _check_empty(data)

    if (ciphername, kdfname) != (_NONE, _NONE):
        ciphername_bytes = ciphername.tobytes()
        if ciphername_bytes not in _SSH_CIPHERS:
            raise UnsupportedAlgorithm(
                f"Unsupported cipher: {ciphername_bytes!r}"
            )
        if kdfname != _BCRYPT:
            raise UnsupportedAlgorithm(f"Unsupported KDF: {kdfname!r}")
        blklen = _SSH_CIPHERS[ciphername_bytes][3]
        _check_block_size(edata, blklen)
        salt, kbuf = _get_sshstr(kdfoptions)
        rounds, kbuf = _get_u32(kbuf)
        _check_empty(kbuf)
        ciph = _init_cipher(ciphername_bytes, password, salt.tobytes(), rounds)
        edata = memoryview(ciph.decryptor().update(edata))
    else:
        blklen = 8
        _check_block_size(edata, blklen)
    ck1, edata = _get_u32(edata)
    ck2, edata = _get_u32(edata)
    if ck1 != ck2:
        raise ValueError("Corrupt data: broken checksum")

    # load per-key struct
    key_type, edata = _get_sshstr(edata)
    if key_type != pub_key_type:
        raise ValueError("Corrupt data: key type mismatch")
    private_key, edata = kformat.load_private(edata, pubfields)
    comment, edata = _get_sshstr(edata)

    # yes, SSH does padding check *after* all other parsing is done.
    # need to follow as it writes zero-byte padding too.
    if edata != _PADDING[: len(edata)]:
        raise ValueError("Corrupt data: invalid padding")

    if isinstance(private_key, dsa.DSAPrivateKey):
        warnings.warn(
            "SSH DSA keys are deprecated and will be removed in a future "
            "release.",
            utils.DeprecatedIn40,
            stacklevel=2,
        )

    return private_key


def _serialize_ssh_private_key(
    private_key: SSHPrivateKeyTypes,
    password: bytes,
    encryption_algorithm: KeySerializationEncryption,
) -> bytes:
    """Serialize private key with OpenSSH custom encoding."""
    utils._check_bytes("password", password)
    if isinstance(private_key, dsa.DSAPrivateKey):
        warnings.warn(
            "SSH DSA key support is deprecated and will be "
            "removed in a future release",
            utils.DeprecatedIn40,
            stacklevel=4,
        )

    key_type = _get_ssh_key_type(private_key)
    kformat = _lookup_kformat(key_type)

    # setup parameters
    f_kdfoptions = _FragList()
    if password:
        ciphername = _DEFAULT_CIPHER
        blklen = _SSH_CIPHERS[ciphername][3]
        kdfname = _BCRYPT
        rounds = _DEFAULT_ROUNDS
        if (
            isinstance(encryption_algorithm, _KeySerializationEncryption)
            and encryption_algorithm._kdf_rounds is not None
        ):
            rounds = encryption_algorithm._kdf_rounds
        salt = os.urandom(16)
        f_kdfoptions.put_sshstr(salt)
        f_kdfoptions.put_u32(rounds)
        ciph = _init_cipher(ciphername, password, salt, rounds)
    else:
        ciphername = kdfname = _NONE
        blklen = 8
        ciph = None
    nkeys = 1
    checkval = os.urandom(4)
    comment = b""

    # encode public and private parts together
    f_public_key = _FragList()
    f_public_key.put_sshstr(key_type)
    kformat.encode_public(private_key.public_key(), f_public_key)

    f_secrets = _FragList([checkval, checkval])
    f_secrets.put_sshstr(key_type)
    kformat.encode_private(private_key, f_secrets)
    f_secrets.put_sshstr(comment)
    f_secrets.put_raw(_PADDING[: blklen - (f_secrets.size() % blklen)])

    # top-level structure
    f_main = _FragList()
    f_main.put_raw(_SK_MAGIC)
    f_main.put_sshstr(ciphername)
    f_main.put_sshstr(kdfname)
    f_main.put_sshstr(f_kdfoptions)
    f_main.put_u32(nkeys)
    f_main.put_sshstr(f_public_key)
    f_main.put_sshstr(f_secrets)

    # copy result info bytearray
    slen = f_secrets.size()
    mlen = f_main.size()
    buf = memoryview(bytearray(mlen + blklen))
    f_main.render(buf)
    ofs = mlen - slen

    # encrypt in-place
    if ciph is not None:
        ciph.encryptor().update_into(buf[ofs:mlen], buf[ofs:])

    return _ssh_pem_encode(buf[:mlen])


SSHPublicKeyTypes = typing.Union[
    ec.EllipticCurvePublicKey,
    rsa.RSAPublicKey,
    dsa.DSAPublicKey,
    ed25519.Ed25519PublicKey,
]

SSHCertPublicKeyTypes = typing.Union[
    ec.EllipticCurvePublicKey,
    rsa.RSAPublicKey,
    ed25519.Ed25519PublicKey,
]


class SSHCertificateType(enum.Enum):
    USER = 1
    HOST = 2


class SSHCertificate:
    def __init__(
        self,
        _nonce: memoryview,
        _public_key: SSHPublicKeyTypes,
        _serial: int,
        _cctype: int,
        _key_id: memoryview,
        _valid_principals: typing.List[bytes],
        _valid_after: int,
        _valid_before: int,
        _critical_options: typing.Dict[bytes, bytes],
        _extensions: typing.Dict[bytes, bytes],
        _sig_type: memoryview,
        _sig_key: memoryview,
        _inner_sig_type: memoryview,
        _signature: memoryview,
        _tbs_cert_body: memoryview,
        _cert_key_type: bytes,
        _cert_body: memoryview,
    ):
        self._nonce = _nonce
        self._public_key = _public_key
        self._serial = _serial
        try:
            self._type = SSHCertificateType(_cctype)
        except ValueError:
            raise ValueError("Invalid certificate type")
        self._key_id = _key_id
        self._valid_principals = _valid_principals
        self._valid_after = _valid_after
        self._valid_before = _valid_before
        self._critical_options = _critical_options
        self._extensions = _extensions
        self._sig_type = _sig_type
        self._sig_key = _sig_key
        self._inner_sig_type = _inner_sig_type
        self._signature = _signature
        self._cert_key_type = _cert_key_type
        self._cert_body = _cert_body
        self._tbs_cert_body = _tbs_cert_body

    @property
    def nonce(self) -> bytes:
        return bytes(self._nonce)

    def public_key(self) -> SSHCertPublicKeyTypes:
        # make mypy happy until we remove DSA support entirely and
        # the underlying union won't have a disallowed type
        return typing.cast(SSHCertPublicKeyTypes, self._public_key)

    @property
    def serial(self) -> int:
        return self._serial

    @property
    def type(self) -> SSHCertificateType:
        return self._type

    @property
    def key_id(self) -> bytes:
        return bytes(self._key_id)

    @property
    def valid_principals(self) -> typing.List[bytes]:
        return self._valid_principals

    @property
    def valid_before(self) -> int:
        return self._valid_before

    @property
    def valid_after(self) -> int:
        return self._valid_after

    @property
    def critical_options(self) -> typing.Dict[bytes, bytes]:
        return self._critical_options

    @property
    def extensions(self) -> typing.Dict[bytes, bytes]:
        return self._extensions

    def signature_key(self) -> SSHCertPublicKeyTypes:
        sigformat = _lookup_kformat(self._sig_type)
        signature_key, sigkey_rest = sigformat.load_public(self._sig_key)
        _check_empty(sigkey_rest)
        return signature_key

    def public_bytes(self) -> bytes:
        return (
            bytes(self._cert_key_type)
            + b" "
            + binascii.b2a_base64(bytes(self._cert_body), newline=False)
        )

    def verify_cert_signature(self) -> None:
        signature_key = self.signature_key()
        if isinstance(signature_key, ed25519.Ed25519PublicKey):
            signature_key.verify(
                bytes(self._signature), bytes(self._tbs_cert_body)
            )
        elif isinstance(signature_key, ec.EllipticCurvePublicKey):
            # The signature is encoded as a pair of big-endian integers
            r, data = _get_mpint(self._signature)
            s, data = _get_mpint(data)
            _check_empty(data)
            computed_sig = asym_utils.encode_dss_signature(r, s)
            hash_alg = _get_ec_hash_alg(signature_key.curve)
            signature_key.verify(
                computed_sig, bytes(self._tbs_cert_body), ec.ECDSA(hash_alg)
            )
        else:
            assert isinstance(signature_key, rsa.RSAPublicKey)
            if self._inner_sig_type == _SSH_RSA:
                hash_alg = hashes.SHA1()
            elif self._inner_sig_type == _SSH_RSA_SHA256:
                hash_alg = hashes.SHA256()
            else:
                assert self._inner_sig_type == _SSH_RSA_SHA512
                hash_alg = hashes.SHA512()
            signature_key.verify(
                bytes(self._signature),
                bytes(self._tbs_cert_body),
                padding.PKCS1v15(),
                hash_alg,
            )


def _get_ec_hash_alg(curve: ec.EllipticCurve) -> hashes.HashAlgorithm:
    if isinstance(curve, ec.SECP256R1):
        return hashes.SHA256()
    elif isinstance(curve, ec.SECP384R1):
        return hashes.SHA384()
    else:
        assert isinstance(curve, ec.SECP521R1)
        return hashes.SHA512()


def _load_ssh_public_identity(
    data: bytes,
    _legacy_dsa_allowed=False,
) -> typing.Union[SSHCertificate, SSHPublicKeyTypes]:
    utils._check_byteslike("data", data)

    m = _SSH_PUBKEY_RC.match(data)
    if not m:
        raise ValueError("Invalid line format")
    key_type = orig_key_type = m.group(1)
    key_body = m.group(2)
    with_cert = False
    if key_type.endswith(_CERT_SUFFIX):
        with_cert = True
        key_type = key_type[: -len(_CERT_SUFFIX)]
    if key_type == _SSH_DSA and not _legacy_dsa_allowed:
        raise UnsupportedAlgorithm(
            "DSA keys aren't supported in SSH certificates"
        )
    kformat = _lookup_kformat(key_type)

    try:
        rest = memoryview(binascii.a2b_base64(key_body))
    except (TypeError, binascii.Error):
        raise ValueError("Invalid format")

    if with_cert:
        cert_body = rest
    inner_key_type, rest = _get_sshstr(rest)
    if inner_key_type != orig_key_type:
        raise ValueError("Invalid key format")
    if with_cert:
        nonce, rest = _get_sshstr(rest)
    public_key, rest = kformat.load_public(rest)
    if with_cert:
        serial, rest = _get_u64(rest)
        cctype, rest = _get_u32(rest)
        key_id, rest = _get_sshstr(rest)
        principals, rest = _get_sshstr(rest)
        valid_principals = []
        while principals:
            principal, principals = _get_sshstr(principals)
            valid_principals.append(bytes(principal))
        valid_after, rest = _get_u64(rest)
        valid_before, rest = _get_u64(rest)
        crit_options, rest = _get_sshstr(rest)
        critical_options = _parse_exts_opts(crit_options)
        exts, rest = _get_sshstr(rest)
        extensions = _parse_exts_opts(exts)
        # Get the reserved field, which is unused.
        _, rest = _get_sshstr(rest)
        sig_key_raw, rest = _get_sshstr(rest)
        sig_type, sig_key = _get_sshstr(sig_key_raw)
        if sig_type == _SSH_DSA and not _legacy_dsa_allowed:
            raise UnsupportedAlgorithm(
                "DSA signatures aren't supported in SSH certificates"
            )
        # Get the entire cert body and subtract the signature
        tbs_cert_body = cert_body[: -len(rest)]
        signature_raw, rest = _get_sshstr(rest)
        _check_empty(rest)
        inner_sig_type, sig_rest = _get_sshstr(signature_raw)
        # RSA certs can have multiple algorithm types
        if (
            sig_type == _SSH_RSA
            and inner_sig_type
            not in [_SSH_RSA_SHA256, _SSH_RSA_SHA512, _SSH_RSA]
        ) or (sig_type != _SSH_RSA and inner_sig_type != sig_type):
            raise ValueError("Signature key type does not match")
        signature, sig_rest = _get_sshstr(sig_rest)
        _check_empty(sig_rest)
        return SSHCertificate(
            nonce,
            public_key,
            serial,
            cctype,
            key_id,
            valid_principals,
            valid_after,
            valid_before,
            critical_options,
            extensions,
            sig_type,
            sig_key,
            inner_sig_type,
            signature,
            tbs_cert_body,
            orig_key_type,
            cert_body,
        )
    else:
        _check_empty(rest)
        return public_key


def load_ssh_public_identity(
    data: bytes,
) -> typing.Union[SSHCertificate, SSHPublicKeyTypes]:
    return _load_ssh_public_identity(data)


def _parse_exts_opts(exts_opts: memoryview) -> typing.Dict[bytes, bytes]:
    result: typing.Dict[bytes, bytes] = {}
    last_name = None
    while exts_opts:
        name, exts_opts = _get_sshstr(exts_opts)
        bname: bytes = bytes(name)
        if bname in result:
            raise ValueError("Duplicate name")
        if last_name is not None and bname < last_name:
            raise ValueError("Fields not lexically sorted")
        value, exts_opts = _get_sshstr(exts_opts)
        result[bname] = bytes(value)
        last_name = bname
    return result


def load_ssh_public_key(
    data: bytes, backend: typing.Any = None
) -> SSHPublicKeyTypes:
    cert_or_key = _load_ssh_public_identity(data, _legacy_dsa_allowed=True)
    public_key: SSHPublicKeyTypes
    if isinstance(cert_or_key, SSHCertificate):
        public_key = cert_or_key.public_key()
    else:
        public_key = cert_or_key

    if isinstance(public_key, dsa.DSAPublicKey):
        warnings.warn(
            "SSH DSA keys are deprecated and will be removed in a future "
            "release.",
            utils.DeprecatedIn40,
            stacklevel=2,
        )
    return public_key


def serialize_ssh_public_key(public_key: SSHPublicKeyTypes) -> bytes:
    """One-line public key format for OpenSSH"""
    if isinstance(public_key, dsa.DSAPublicKey):
        warnings.warn(
            "SSH DSA key support is deprecated and will be "
            "removed in a future release",
            utils.DeprecatedIn40,
            stacklevel=4,
        )
    key_type = _get_ssh_key_type(public_key)
    kformat = _lookup_kformat(key_type)

    f_pub = _FragList()
    f_pub.put_sshstr(key_type)
    kformat.encode_public(public_key, f_pub)

    pub = binascii.b2a_base64(f_pub.tobytes()).strip()
    return b"".join([key_type, b" ", pub])


SSHCertPrivateKeyTypes = typing.Union[
    ec.EllipticCurvePrivateKey,
    rsa.RSAPrivateKey,
    ed25519.Ed25519PrivateKey,
]


# This is an undocumented limit enforced in the openssh codebase for sshd and
# ssh-keygen, but it is undefined in the ssh certificates spec.
_SSHKEY_CERT_MAX_PRINCIPALS = 256


class SSHCertificateBuilder:
    def __init__(
        self,
        _public_key: typing.Optional[SSHCertPublicKeyTypes] = None,
        _serial: typing.Optional[int] = None,
        _type: typing.Optional[SSHCertificateType] = None,
        _key_id: typing.Optional[bytes] = None,
        _valid_principals: typing.List[bytes] = [],
        _valid_for_all_principals: bool = False,
        _valid_before: typing.Optional[int] = None,
        _valid_after: typing.Optional[int] = None,
        _critical_options: typing.List[typing.Tuple[bytes, bytes]] = [],
        _extensions: typing.List[typing.Tuple[bytes, bytes]] = [],
    ):
        self._public_key = _public_key
        self._serial = _serial
        self._type = _type
        self._key_id = _key_id
        self._valid_principals = _valid_principals
        self._valid_for_all_principals = _valid_for_all_principals
        self._valid_before = _valid_before
        self._valid_after = _valid_after
        self._critical_options = _critical_options
        self._extensions = _extensions

    def public_key(
        self, public_key: SSHCertPublicKeyTypes
    ) -> "SSHCertificateBuilder":
        if not isinstance(
            public_key,
            (
                ec.EllipticCurvePublicKey,
                rsa.RSAPublicKey,
                ed25519.Ed25519PublicKey,
            ),
        ):
            raise TypeError("Unsupported key type")
        if self._public_key is not None:
            raise ValueError("public_key already set")

        return SSHCertificateBuilder(
            _public_key=public_key,
            _serial=self._serial,
            _type=self._type,
            _key_id=self._key_id,
            _valid_principals=self._valid_principals,
            _valid_for_all_principals=self._valid_for_all_principals,
            _valid_before=self._valid_before,
            _valid_after=self._valid_after,
            _critical_options=self._critical_options,
            _extensions=self._extensions,
        )

    def serial(self, serial: int) -> "SSHCertificateBuilder":
        if not isinstance(serial, int):
            raise TypeError("serial must be an integer")
        if not 0 <= serial < 2**64:
            raise ValueError("serial must be between 0 and 2**64")
        if self._serial is not None:
            raise ValueError("serial already set")

        return SSHCertificateBuilder(
            _public_key=self._public_key,
            _serial=serial,
            _type=self._type,
            _key_id=self._key_id,
            _valid_principals=self._valid_principals,
            _valid_for_all_principals=self._valid_for_all_principals,
            _valid_before=self._valid_before,
            _valid_after=self._valid_after,
            _critical_options=self._critical_options,
            _extensions=self._extensions,
        )

    def type(self, type: SSHCertificateType) -> "SSHCertificateBuilder":
        if not isinstance(type, SSHCertificateType):
            raise TypeError("type must be an SSHCertificateType")
        if self._type is not None:
            raise ValueError("type already set")

        return SSHCertificateBuilder(
            _public_key=self._public_key,
            _serial=self._serial,
            _type=type,
            _key_id=self._key_id,
            _valid_principals=self._valid_principals,
            _valid_for_all_principals=self._valid_for_all_principals,
            _valid_before=self._valid_before,
            _valid_after=self._valid_after,
            _critical_options=self._critical_options,
            _extensions=self._extensions,
        )

    def key_id(self, key_id: bytes) -> "SSHCertificateBuilder":
        if not isinstance(key_id, bytes):
            raise TypeError("key_id must be bytes")
        if self._key_id is not None:
            raise ValueError("key_id already set")

        return SSHCertificateBuilder(
            _public_key=self._public_key,
            _serial=self._serial,
            _type=self._type,
            _key_id=key_id,
            _valid_principals=self._valid_principals,
            _valid_for_all_principals=self._valid_for_all_principals,
            _valid_before=self._valid_before,
            _valid_after=self._valid_after,
            _critical_options=self._critical_options,
            _extensions=self._extensions,
        )

    def valid_principals(
        self, valid_principals: typing.List[bytes]
    ) -> "SSHCertificateBuilder":
        if self._valid_for_all_principals:
            raise ValueError(
                "Principals can't be set because the cert is valid "
                "for all principals"
            )
        if (
            not all(isinstance(x, bytes) for x in valid_principals)
            or not valid_principals
        ):
            raise TypeError(
                "principals must be a list of bytes and can't be empty"
            )
        if self._valid_principals:
            raise ValueError("valid_principals already set")

        if len(valid_principals) > _SSHKEY_CERT_MAX_PRINCIPALS:
            raise ValueError(
                "Reached or exceeded the maximum number of valid_principals"
            )

        return SSHCertificateBuilder(
            _public_key=self._public_key,
            _serial=self._serial,
            _type=self._type,
            _key_id=self._key_id,
            _valid_principals=valid_principals,
            _valid_for_all_principals=self._valid_for_all_principals,
            _valid_before=self._valid_before,
            _valid_after=self._valid_after,
            _critical_options=self._critical_options,
            _extensions=self._extensions,
        )

    def valid_for_all_principals(self):
        if self._valid_principals:
            raise ValueError(
                "valid_principals already set, can't set "
                "valid_for_all_principals"
            )
        if self._valid_for_all_principals:
            raise ValueError("valid_for_all_principals already set")

        return SSHCertificateBuilder(
            _public_key=self._public_key,
            _serial=self._serial,
            _type=self._type,
            _key_id=self._key_id,
            _valid_principals=self._valid_principals,
            _valid_for_all_principals=True,
            _valid_before=self._valid_before,
            _valid_after=self._valid_after,
            _critical_options=self._critical_options,
            _extensions=self._extensions,
        )

    def valid_before(
        self, valid_before: typing.Union[int, float]
    ) -> "SSHCertificateBuilder":
        if not isinstance(valid_before, (int, float)):
            raise TypeError("valid_before must be an int or float")
        valid_before = int(valid_before)
        if valid_before < 0 or valid_before >= 2**64:
            raise ValueError("valid_before must [0, 2**64)")
        if self._valid_before is not None:
            raise ValueError("valid_before already set")

        return SSHCertificateBuilder(
            _public_key=self._public_key,
            _serial=self._serial,
            _type=self._type,
            _key_id=self._key_id,
            _valid_principals=self._valid_principals,
            _valid_for_all_principals=self._valid_for_all_principals,
            _valid_before=valid_before,
            _valid_after=self._valid_after,
            _critical_options=self._critical_options,
            _extensions=self._extensions,
        )

    def valid_after(
        self, valid_after: typing.Union[int, float]
    ) -> "SSHCertificateBuilder":
        if not isinstance(valid_after, (int, float)):
            raise TypeError("valid_after must be an int or float")
        valid_after = int(valid_after)
        if valid_after < 0 or valid_after >= 2**64:
            raise ValueError("valid_after must [0, 2**64)")
        if self._valid_after is not None:
            raise ValueError("valid_after already set")

        return SSHCertificateBuilder(
            _public_key=self._public_key,
            _serial=self._serial,
            _type=self._type,
            _key_id=self._key_id,
            _valid_principals=self._valid_principals,
            _valid_for_all_principals=self._valid_for_all_principals,
            _valid_before=self._valid_before,
            _valid_after=valid_after,
            _critical_options=self._critical_options,
            _extensions=self._extensions,
        )

    def add_critical_option(
        self, name: bytes, value: bytes
    ) -> "SSHCertificateBuilder":
        if not isinstance(name, bytes) or not isinstance(value, bytes):
            raise TypeError("name and value must be bytes")
        # This is O(n**2)
        if name in [name for name, _ in self._critical_options]:
            raise ValueError("Duplicate critical option name")

        return SSHCertificateBuilder(
            _public_key=self._public_key,
            _serial=self._serial,
            _type=self._type,
            _key_id=self._key_id,
            _valid_principals=self._valid_principals,
            _valid_for_all_principals=self._valid_for_all_principals,
            _valid_before=self._valid_before,
            _valid_after=self._valid_after,
            _critical_options=self._critical_options + [(name, value)],
            _extensions=self._extensions,
        )

    def add_extension(
        self, name: bytes, value: bytes
    ) -> "SSHCertificateBuilder":
        if not isinstance(name, bytes) or not isinstance(value, bytes):
            raise TypeError("name and value must be bytes")
        # This is O(n**2)
        if name in [name for name, _ in self._extensions]:
            raise ValueError("Duplicate extension name")

        return SSHCertificateBuilder(
            _public_key=self._public_key,
            _serial=self._serial,
            _type=self._type,
            _key_id=self._key_id,
            _valid_principals=self._valid_principals,
            _valid_for_all_principals=self._valid_for_all_principals,
            _valid_before=self._valid_before,
            _valid_after=self._valid_after,
            _critical_options=self._critical_options,
            _extensions=self._extensions + [(name, value)],
        )

    def sign(self, private_key: SSHCertPrivateKeyTypes) -> SSHCertificate:
        if not isinstance(
            private_key,
            (
                ec.EllipticCurvePrivateKey,
                rsa.RSAPrivateKey,
                ed25519.Ed25519PrivateKey,
            ),
        ):
            raise TypeError("Unsupported private key type")

        if self._public_key is None:
            raise ValueError("public_key must be set")

        # Not required
        serial = 0 if self._serial is None else self._serial

        if self._type is None:
            raise ValueError("type must be set")

        # Not required
        key_id = b"" if self._key_id is None else self._key_id

        # A zero length list is valid, but means the certificate
        # is valid for any principal of the specified type. We require
        # the user to explicitly set valid_for_all_principals to get
        # that behavior.
        if not self._valid_principals and not self._valid_for_all_principals:
            raise ValueError(
                "valid_principals must be set if valid_for_all_principals "
                "is False"
            )

        if self._valid_before is None:
            raise ValueError("valid_before must be set")

        if self._valid_after is None:
            raise ValueError("valid_after must be set")

        if self._valid_after > self._valid_before:
            raise ValueError("valid_after must be earlier than valid_before")

        # lexically sort our byte strings
        self._critical_options.sort(key=lambda x: x[0])
        self._extensions.sort(key=lambda x: x[0])

        key_type = _get_ssh_key_type(self._public_key)
        cert_prefix = key_type + _CERT_SUFFIX

        # Marshal the bytes to be signed
        nonce = os.urandom(32)
        kformat = _lookup_kformat(key_type)
        f = _FragList()
        f.put_sshstr(cert_prefix)
        f.put_sshstr(nonce)
        kformat.encode_public(self._public_key, f)
        f.put_u64(serial)
        f.put_u32(self._type.value)
        f.put_sshstr(key_id)
        fprincipals = _FragList()
        for p in self._valid_principals:
            fprincipals.put_sshstr(p)
        f.put_sshstr(fprincipals.tobytes())
        f.put_u64(self._valid_after)
        f.put_u64(self._valid_before)
        fcrit = _FragList()
        for name, value in self._critical_options:
            fcrit.put_sshstr(name)
            fcrit.put_sshstr(value)
        f.put_sshstr(fcrit.tobytes())
        fext = _FragList()
        for name, value in self._extensions:
            fext.put_sshstr(name)
            fext.put_sshstr(value)
        f.put_sshstr(fext.tobytes())
        f.put_sshstr(b"")  # RESERVED FIELD
        # encode CA public key
        ca_type = _get_ssh_key_type(private_key)
        caformat = _lookup_kformat(ca_type)
        caf = _FragList()
        caf.put_sshstr(ca_type)
        caformat.encode_public(private_key.public_key(), caf)
        f.put_sshstr(caf.tobytes())
        # Sigs according to the rules defined for the CA's public key
        # (RFC4253 section 6.6 for ssh-rsa, RFC5656 for ECDSA,
        # and RFC8032 for Ed25519).
        if isinstance(private_key, ed25519.Ed25519PrivateKey):
            signature = private_key.sign(f.tobytes())
            fsig = _FragList()
            fsig.put_sshstr(ca_type)
            fsig.put_sshstr(signature)
            f.put_sshstr(fsig.tobytes())
        elif isinstance(private_key, ec.EllipticCurvePrivateKey):
            hash_alg = _get_ec_hash_alg(private_key.curve)
            signature = private_key.sign(f.tobytes(), ec.ECDSA(hash_alg))
            r, s = asym_utils.decode_dss_signature(signature)
            fsig = _FragList()
            fsig.put_sshstr(ca_type)
            fsigblob = _FragList()
            fsigblob.put_mpint(r)
            fsigblob.put_mpint(s)
            fsig.put_sshstr(fsigblob.tobytes())
            f.put_sshstr(fsig.tobytes())

        else:
            assert isinstance(private_key, rsa.RSAPrivateKey)
            # Just like Golang, we're going to use SHA512 for RSA
            # https://cs.opensource.google/go/x/crypto/+/refs/tags/
            # v0.4.0:ssh/certs.go;l=445
            # RFC 8332 defines SHA256 and 512 as options
            fsig = _FragList()
            fsig.put_sshstr(_SSH_RSA_SHA512)
            signature = private_key.sign(
                f.tobytes(), padding.PKCS1v15(), hashes.SHA512()
            )
            fsig.put_sshstr(signature)
            f.put_sshstr(fsig.tobytes())

        cert_data = binascii.b2a_base64(f.tobytes()).strip()
        # load_ssh_public_identity returns a union, but this is
        # guaranteed to be an SSHCertificate, so we cast to make
        # mypy happy.
        return typing.cast(
            SSHCertificate,
            load_ssh_public_identity(b"".join([cert_prefix, b" ", cert_data])),
        )
