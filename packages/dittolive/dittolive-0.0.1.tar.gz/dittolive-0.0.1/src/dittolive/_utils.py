"""Bunch of utilitary functions for dittolive.

If this file grows too much, feel free to split it in a new module.
"""
import weakref

from _dittoffi import ffi, lib
from cbor2 import encoder

global_weakkeydict = weakref.WeakKeyDictionary()

def char_p(string: str) -> bytes:
    """FFI utils function.

    Args:
        string: the string to convert to bytes
    Returns: a char* representation of a Python String with UTF-8 encoding.
    """
    bytes = string.encode("utf-8")
    if 0 in bytes[:-1]:
        raise ValueError("Inner null byte in string")
    return bytes

def empty_char_p():
    return ffi.cast("char*", ffi.NULL)

def string(charp) -> str:
    """Turn char pointer into regular Python string.

    Args:
        charp (_type_): pointer to C utf-8 string

    Returns:
        str: Python valid string
    """
    return ffi.string(charp).decode()

def bytes_from_boxed(slice_boxed_uint8_t) -> bytes:
    """Create a Python `bytes` from a slice_boxed_uint8_t.

    Args:
        slice_boxed_uint8_t : boxed slice return by the FFI

    Returns:
        bytes: Python byte repr
    """
    length = slice_boxed_uint8_t.len
    ptr = slice_boxed_uint8_t.ptr
    # CHECKME(Ronan) this seems a questionnable solution, almost
    # looking like an HACK

    if ptr == ffi.NULL:
        return None

    slice = bytes([ptr[i] for i in range(0,length)])
    lib.ditto_c_bytes_free(slice_boxed_uint8_t)
    return slice

def slice_ref_uint8(data:bytes):
    # CHECKME : use it with `with slice(data) as ...`
    # to avoid cbor getting gargabe collected early
    """Return a FFI slice.

    You need to add [0] to access the value.
    """
    slice_ref = ffi.new("slice_ref_uint8_t*")
    length = len(data)
    data = ffi.new("uint8_t[]", data)
    slice_ref.ptr = data
    slice_ref.len = length
    return slice_ref

def cbor_slice_ref_uint8(data:object):
    """Return a non empty FFI slice representing CBOR data.

    You need to add [0] to access the value.
    """
    # CHECKME : use it with `with slice(data) as ...`
    # to avoid cbor getting gargabe collected early
    """Return a FFI slice."""
    cbor = encoder.dumps(data)
    return slice_ref_uint8(cbor)

def empty_slice_ref_uint8(pointer = ffi.NULL):
    """Return a FFI slice."""
    slice_ref = ffi.new("slice_ref_uint8_t*", dict(
        len = 0,
        ptr = pointer
    ))
    return slice_ref

def empty_cbor_slice_ref_uint8():
    """Return a FFI slice.

    You need to add [0] to access the value.
    """
    return empty_slice_ref_uint8(ffi.cast("uint8_t*", 0xbad000))

def empty_order_slice_ref():
    """Return a FFI slice.

    You need to add [0] to access the value.
    """
    slice_ref = ffi.new("slice_ref_COrderByParam_t*", dict(
        len = 0,
        ptr = ffi.cast("COrderByParam_t*" ,0xbad000)
    ))
    return slice_ref
