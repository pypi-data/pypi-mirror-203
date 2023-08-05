"""All exceptions of the dittolive package."""
from _dittoffi import lib, ffi

from dittolive._utils import string
class DittoException(Exception):
    """Superclass of all dittolive exceptions.

    It will never be raised directly.
    """

class FfiException(DittoException):
    """Something went wrong on the other side of the FFI."""
    def __init__(self):
        """Create a new FfiException."""
        message = lib.ditto_error_message()
        if message == ffi.NULL:
            super().__init__("Error across the FFI")
        else :
            str_message = string(message)
            super().__init__(f"Error across the FFI : {str_message}")

NOT_FOUND_ERROR_CODE = -30798
class DocumentNotFoundException(DittoException):
    """Document was not found."""

class ConfigException(DittoException):
    """Bad config."""

class LicenseException(DittoException):
    """License was not validated for some reason."""

class NotAuthentifiedException(DittoException):
    """The current instance is not authentified."""

class NotActivatedException(DittoException):
    """Ditto requires a valid license."""
