"""Subscription to Ditto Documents."""

from dittolive.__observer import Observer
from _dittoffi import lib
from dittolive._utils import empty_order_slice_ref, empty_slice_ref_uint8
from dittolive.exceptions import FfiException
class Subscription(Observer):
    """Subscription class.

    Subscriptions are used to register interest in receiving updates
    for specified documents.
    """
    def __init__(self, ditto_raw, collection_name:bytes, query:bytes, *,
                 query_args=None, order_by=None, limit:int=-1, offset:int=0):
        """Create a new Subscription.

        Keep this alive for as long as you want
        to receive updates on the specified documents.

        Args:
            ditto_raw (_type_): raw pointer to Ditto
            collection_name (bytes): char_p pointer to the collection name
            query (bytes): char_p to the query string
            query_args (_type_): _description_
            order_by (_type_): _description_
            limit (int, optional): Maximum number of documents. Defaults to -1.
            offset (int, optional): Offset of the document to retrieve. Defaults to 0.
        """
        super().__init__()
        self.__raw_ditto = ditto_raw
        self.__collection_name = collection_name
        self.__query = query

        # TODO: handle query_args and order_by when we add the new `Collection::find`
        # API for DQL
        query_args = empty_slice_ref_uint8()
        order_by = empty_order_slice_ref()

        self.__query_args = query_args
        self.__order_by = order_by
        self.__limit = limit
        self.__offset = offset

        res = lib.ditto_add_subscription(self.__raw_ditto, self.__collection_name,
                        self.__query, self.__query_args[0],
                        self.__order_by[0], self.__limit, self.__offset)

        if res != 0:
            raise FfiException

    def _close_callback(self):
        res = lib.ditto_remove_subscription(self.__raw_ditto, self.__collection_name,
                        self.__query, self.__query_args[0],
                        self.__order_by[0], self.__limit, self.__offset)
        if res != 0:
            raise FfiException
