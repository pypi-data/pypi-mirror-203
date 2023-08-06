"""Store module."""

from _dittoffi import lib

from dittolive._utils import char_p
from .collection import Collection

class Store:
    """Database for ditto."""

    def __init__(self, ditto):
        """Initialize store."""
        self.__raw_ditto = ditto

    def collection(self, collection_name: str) -> Collection:
        """Return collection named 'collection_name'."""
        byted_collection_name = char_p(collection_name)

        status = lib.ditto_collection(self.__raw_ditto, byted_collection_name)

        if status != 0:
            raise KeyError(collection_name)

        return Collection(self.__raw_ditto, byted_collection_name)

    def __getitem__(self, collection_name: str) -> Collection:
        """Return collection named 'collection_name'."""
        return self.collection(collection_name)

    def write(self, query: str):
        """Write transaction."""
        raise NotImplementedError

    def collections(self):
        """Returns  a PendingCollectionsOperation."""
        raise NotImplementedError
