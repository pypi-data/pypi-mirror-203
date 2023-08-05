"""Document module."""
import cbor2

from .document_path import DocumentPath
from .document_id import DocumentId
from _dittoffi import lib
from dittolive._utils import bytes_from_boxed
class Document:
    """Document."""
    def __init__(self, doc_ptr):
        """Create a new Document."""
        self.__doc_ptr = doc_ptr

    def __del__(self):
        """Delete the document and release ressources."""
        lib.ditto_document_free(self.__doc_ptr)

    def id(self) -> DocumentId:
        """Get the document's Id."""
        boxed_slice = lib.ditto_document_id(self.__doc_ptr)
        doc_id = bytes_from_boxed(boxed_slice)
        return DocumentId(doc_id)

    @property
    def value(self) -> dict:
        """Get the document's inner value."""
        cbor = lib.ditto_document_cbor(self.__doc_ptr)
        cbor_bytes = bytes_from_boxed(cbor)

        return cbor2.loads(cbor_bytes)

    def get(self, key:str) -> DocumentPath:
        """Follow path in a document.

        Use to specify a path to a key in the document that you can
        subscript further to access a nested key in the document.
        """
        return DocumentPath(self.__doc_ptr, self.id(), key)

    def __getitem__(self, key:str) -> DocumentPath:
        """Follow path in a document.

        Use to specify a path to a key in the document that you can
        subscript further to access a nested key in the document.
        """
        return self.get(key)
