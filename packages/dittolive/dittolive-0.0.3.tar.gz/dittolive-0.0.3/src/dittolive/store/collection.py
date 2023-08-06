"""Collection module."""

from typing import Callable
from _dittoffi import lib, ffi

from .types import WriteStrategy
from .document_id import DocumentId
from .pending_id_specific_operation import PendingIdSpecificOperation
from dittolive._utils import (cbor_slice_ref_uint8, empty_slice_ref_uint8,
    bytes_from_boxed)
from dittolive.exceptions import FfiException

class Collection:
    """Manage documents from here."""

    def __init__(self, ditto, char_p_collection_name:bytes):
        """Create a new Collection."""
        self.__raw_ditto = ditto
        self.__collection_name = char_p_collection_name

    def name(self) -> str:
        """Return a str reprensentation of the collection name."""
        str.encode(self.__collection_name)

    def find_all(self):
        """Find all collections in the store.

        Generates a DittoPendingCursorOperation that can be used to find all
        documents in the collection at a point in time or you can chain a call
        to observe_local or subscribe if you want to get updates about documents
        in the collection over time. It can also be used to update, remove, or
        evict documents.
        """
        raise NotImplementedError

    def find(self, query:str):
        """Find documents that match the given query.

        Generates a DittoPendingCursorOperation with the provided query that can
        be used to find the documents matching the query at a point in time or
        you can chain a call to observe_local or subscribe if you want to get
        updates about documents matching the query as they occur. It can also be
        used to update, remove, or evict documents.
        """
        raise NotImplementedError

    def find_with_args(self, query: str, args):
        """Find documents that match the given query and args.

        Generates a DittoPendingCursorOperation with the provided query and
        query arguments that can be used to find the documents matching the
        query at a point in time or you can chain a call to observe_local or
        subscribe if you want to get updates about documents matching the query
        as they occur. It can also be used to update, remove, or evict
        documents.

        This is the recommended function to use when performing queries on a
        collection if you have any dynamic data included in the query string. It
        allows you to provide a query string with placeholders, in the form of
        `$args.my_arg_name`, along with an accompanying dictionary of arguments,
        in the form of `{ "my_arg_name": "some value" }`, and the placeholders
        will be appropriately replaced by the matching provided arguments from
        the dictionary. This includes handling things like wrapping strings in
        quotation marks and arrays in square brackets, for example.
        """
        raise NotImplementedError

    def find_by_id(self, doc_id: DocumentId):
        """Find the document with the given doc_id.

        Generates a DittoPendingIDSpecificOperation with the provided document
        ID that can be used to find the document at a point in time or you can
        chain a call to observe_local or subscribe if you want to get updates
        about the document over time. It can also be used to update, remove, or
        evict the document.
        """
        return PendingIdSpecificOperation(self.__raw_ditto, self.__collection_name,
                                        doc_id)

    def upsert(self, content, *,
            write_strategy: WriteStrategy = WriteStrategy.Merge)-> DocumentId:
        """Inserts a new document into the collection and returns its ID.

        If the document already exists, the provided document content will be merged
        with the existing document's content.
        """
        data = cbor_slice_ref_uint8(content)

        id_res = lib.ditto_collection_insert_value(
            self.__raw_ditto,
            self.__collection_name,
            data[0],
            empty_slice_ref_uint8()[0], #doc id
            write_strategy.value, #Write Strategy Merge TODO
            ffi.NULL, #hint
            ffi.NULL, #Write txn
        )

        if id_res.status_code != 0:
            raise FfiException

        return DocumentId(bytes_from_boxed(id_res.id))

    def new_attachment(self, path:str, metadata:dict):
        """Creates a new attachment, which can then be inserted into a document.

        The file residing at the provided path will be copied into the
        Ditto’s store. The DittoAttachment object that is returned is what you
        can then use to insert an attachment into a document.

        You can provide metadata about the attachment, which will be replicated
        to other peers alongside the file attachment.

        Below is a snippet to show how you can use the new_attachment
        functionality to insert an attachment into a document.
        """
        raise NotImplementedError

    def fetch_attachment(self, token, on_change: Callable[[str],None]):
        """Fetch the attachment corresponding to the provided attachment token.

        Args:
            token (_type_): Attachment token
            on_change (Callable[[str],None]): A closure that will be called when the
                status of the request to fetch the attachment has changed.
                If the attachment is already available then this will be called almost
                immediatly with a completed status value.
        """
        raise NotImplementedError
