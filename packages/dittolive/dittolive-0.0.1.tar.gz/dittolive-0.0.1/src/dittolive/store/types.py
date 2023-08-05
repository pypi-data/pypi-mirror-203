"""Types alias for the store module."""

from enum import Enum

from _dittoffi import lib

_FIND_ALL_QUERY = "true"

class WriteStrategy(Enum):
    """Write Strategy enum."""
    Merge = lib.WRITE_STRATEGY_RS_MERGE
    InsertIfAbsent = lib.WRITE_STRATEGY_RS_INSERT_IF_ABSENT
    InsertDefaultIfAbsent = lib.WRITE_STRATEGY_RS_INSERT_DEFAULT_IF_ABSENT
