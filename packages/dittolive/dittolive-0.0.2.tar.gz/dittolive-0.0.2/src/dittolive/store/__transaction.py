from _dittoffi import lib, ffi
from dittolive.exceptions import FfiException

class WriteTransaction:
    """Write transaction class.

    Use it with the `with` keyword to have a scoped transaction.
    """
    def __init__(self, raw_ditto):
        self.__raw_ditto = raw_ditto

        res = lib.ditto_write_transaction(self.__raw_ditto, ffi.NULL)
        if res.status_code != 0:
            raise FfiException

        self.__txn = res.txn

    def __enter__(self):
        return self.__txn

    def __exit__(self, exc_type, exc_value, exc_traceback):
        status = lib.ditto_write_transaction_commit(self.__raw_ditto, self.__txn)
        if status != 0:
            raise FfiException
