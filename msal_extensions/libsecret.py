"""Implements a TokenCache that works in Linux and Unix environments with access to LibSecret."""

import ctypes as _ctypes


class SecretSchemaAttributeType(object):
    STRING = _ctypes.c_int(0)
    INTEGER = _ctypes.c_int(1)
    BOOLEAN = _ctypes.c_int(2)


class SecretSchemaFlags(object):
    NONE = 0
    DONT_MATCH_NAME = 1 << 1


_LIBSECRET = _ctypes.CDLL('libsecret-1.so.0')

_SECRET_SCHEMA_NEW =_LIBSECRET.secret_schema_new
_SECRET_SCHEMA_NEW.argtypes = (
    _ctypes.c_char_p,  # name
    _ctypes.c_int,  # flags
    _ctypes.c_char_p,  # attribute 1
    _ctypes.c_int,  # attribute 1 type
    _ctypes.c_char_p,  # attribute 2
    _ctypes.c_int,  # attribute 2 type
    _ctypes.c_void_p,  # end
)
_SECRET_SCHEMA_NEW.restype = _ctypes.c_void_p

# _SECRET_PASSWORD_STORE_SYNC = _LIBSECRET.secret_password_store_sync()
#
# _SECRET_PASSWORD_LOOKUP_SYNC = _LIBSECRET.secret_password_lookup_sync
#
# _SECRET_PASSWORD_CLEAR_SYNC = _LIBSECRET.secret_password_clear_sync


class Schema:

class LibSecret:
    """Wraps the C functions that are provided by libsecret here:
    https://developer.gnome.org/libsecret/0.18
    """
    def __init__(self):
        self._schema =

    def __enter__(self):
        pass

    def __exit__(self, *args):


    def store(self, password):
        # type: (str) -> None
        pass

    def lookup(self):
