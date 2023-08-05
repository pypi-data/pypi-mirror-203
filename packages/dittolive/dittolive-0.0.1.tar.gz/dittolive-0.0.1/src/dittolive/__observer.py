from abc import ABC, abstractmethod

class Observer(ABC):
    def __init__(self):
        self.__observer_closed = False

    def __del__(self):
        self.close()

    @abstractmethod
    def _close_callback(self):
        """Stop the observer."""

    def close(self):
        """Stop the observer."""
        if not self.__observer_closed:
            self._close_callback()
            self.__observer_closed = True
