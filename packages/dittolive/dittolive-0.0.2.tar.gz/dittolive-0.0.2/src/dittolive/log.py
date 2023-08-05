"""Log module."""

from enum import Enum

class LogLevel(Enum):
    """Log level."""
    ERROR = 1
    WARNING = 2
    INFO = 3
    DEBUG = 4
    VERBOSE = 5
