"""Mutable documents."""

import cbor2

from _dittoffi import lib
from dittolive._utils import bytes_from_boxed

from .document_id import DocumentId
from .mutable_document_path import MutableDocumentPath

class MutableDocument:
    """TODO."""
    def __init__(self, doc_ptr, doc_id: DocumentId):
        """Create a new mutable document."""
        self.__doc_ptr = doc_ptr
        self.__doc_id = doc_id
        self.results = []

    def __getitem__(self, key:str):
        """Get mutable path in the document.

        Args:
            key (str): _description_.
        """
        return MutableDocumentPath(self.__doc_ptr, self.__doc_ptr, key, self.results)

    def __setitem__(self, key, value):
        """Set value.

        Args:
            key (_type_): path to the field
            value (_type_): value to be set
        """
        self[key].value = value

    @property
    def value(self) -> dict:
        """Get the document's inner value."""
        cbor = lib.ditto_document_cbor(self.__doc_ptr)
        cbor_bytes = bytes_from_boxed(cbor)

        return cbor2.loads(cbor_bytes)
