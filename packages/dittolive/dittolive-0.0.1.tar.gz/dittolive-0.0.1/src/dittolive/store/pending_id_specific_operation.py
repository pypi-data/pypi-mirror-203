"""PendingIdSpecificOperation."""

from typing import List, Callable

from _dittoffi import lib

from .document import Document
from .__transaction import WriteTransaction
from .document_id import DocumentId
from .mutable_document import MutableDocument
from dittolive.exceptions import FfiException, DocumentNotFoundException,\
    NOT_FOUND_ERROR_CODE
from dittolive._utils import char_p
from .live_query import LiveQuery
from .subscription import Subscription
from .update_result import UpdateResult


class _SingleDocumentLiveQueryEvent:
    def __init__(self, is_initial:bool, old_document:Document = None):
        self.is_initial = is_initial
        self.old_document = old_document

LiveQuerySingleDocumentCallback = Callable[[MutableDocument,
                                            _SingleDocumentLiveQueryEvent], None]

class PendingIdSpecificOperation:
    """_summary_."""

    def __init__(self, raw_ditto, collection_name:bytes, doc_id:DocumentId):
        """Create a new PendingIdSpecificOperation.

        Args:
            raw_ditto (_type_): handle to CDitto
            collection_name (bytes): Collection name in char_p ~ bytes
            doc_id (DocumentId): DocId
        """
        self.__raw_ditto = raw_ditto
        self.__collection_name = collection_name
        self.__doc_id = doc_id

    def __query(self) -> bytes:
        """Return a char_p repr of the inner query.

        Returns:
            bytes: char_p of the specific id query
        """
        query = f" _id == {str(self.__doc_id)!r}"
        return char_p(query)

    def subscribe(self) -> Subscription:
        """Create new subscription.

        Returns:
            Subscription: _description_
        """
        return Subscription(self.__raw_ditto, self.__collection_name, self.__query())

    def remove(self):
        """Remove selected document.

        Raises:
            FfiException: The document could not be removed
        """
        with WriteTransaction(self.__raw_ditto) as write_txn:
            was_removed = lib.ditto_collection_remove(
                self.__raw_ditto,
                self.__collection_name,
                write_txn,
                self.__doc_id._raw()[0],
            )
            if not was_removed:
                lib.ditto_write_transaction_rollback(self.__raw_ditto, write_txn)
                raise FfiException

    def evict(self):
        """Evict selected document.

        Raises:
            NotImplementedError: _description_
        """
        with WriteTransaction(self.__raw_ditto) as write_txn:
            was_removed = lib.ditto_collection_evict(
                self.__raw_ditto,
                self.__collection_name,
                write_txn,
                self.__doc_id._raw()[0],
            )

            if not was_removed:
                lib.ditto_write_transaction_rollback(self.__raw_ditto, write_txn)
                raise FfiException

    def exec(self) -> Document:
        """Get selected document.

        Raises:
            FfiException: _description_
            DocumentNotFoundException: _description_

        Returns:
            Document: _description_
        """
        doc_ptr = self._exec()
        return Document(doc_ptr)

    def _exec(self):
        """Internal exec.

        Return document pointer
        """
        read_txn = lib.ditto_read_transaction(self.__raw_ditto).txn

        result = lib.ditto_collection_get(
            self.__raw_ditto,
            self.__collection_name,
            self.__doc_id._raw()[0],
            read_txn
        )

        # TODO : not found error code
        if result.status_code == NOT_FOUND_ERROR_CODE:
            raise DocumentNotFoundException
        elif result.status_code != 0:
            raise FfiException

        return result.document

    def observe(self, callback: LiveQuerySingleDocumentCallback) -> LiveQuery:
        """Observe selected document.

        Raises:
            NotImplementedError: _description_

        Returns:
            LiveQuery: _description_
        """

        def lq_doc_event_handler(documents, event):
            """Callback for LiveQuery. Wrap the user callback.

            Args:
                documents (_type_): List of raw Documents
                event (_type_): LiveQueryEvent
                signal_next (_type_): Next signal
            """
            old_document = None
            new_document = None

            if not event.is_initial and len(event.old_documents) == 1:
                old_document = event.old_documents[0]

            if len(documents) == 0:
                ...
            elif len(documents) == 1:
                new_document = documents[0]
            else:
                return

            event = _SingleDocumentLiveQueryEvent(old_document=old_document,
                                                is_initial=event.is_initial)

            callback(new_document, event)

        return LiveQuery(self.__raw_ditto, self.__query(),
            self.__collection_name, lq_doc_event_handler)

    def update(self, updater: LiveQuerySingleDocumentCallback) -> List[UpdateResult]:
        """Update selected document with given callback.

        Raises:
            NotImplementedError: _description_

        Returns:
            List[UpdateResult]: _description_
        """
        doc_ptr = self._exec()
        doc = MutableDocument(doc_ptr, self.__doc_id)

        with WriteTransaction(self.__raw_ditto) as write_txn:
            updater(doc)

            lib.ditto_collection_update(self.__raw_ditto, self.__collection_name,
                                        write_txn, doc_ptr)

        return doc.results
