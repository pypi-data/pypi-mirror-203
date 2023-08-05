"""Document Id class."""


from _dittoffi import lib
from dittolive._utils import slice_ref_uint8, string

class DocumentId():
    """Document id class."""
    def __init__(self, id_bytes) -> None:
        """Creates a new DocumentId with the given bytes value."""
        self.__bytes = id_bytes

    def _raw(self):
        """Returns a raw representation of the DocumentId for the FFI."""
        return slice_ref_uint8(self.__bytes)

    def __str__(self) -> str:
        """Return a query compatible string view of the DocumentId."""
        doc_id_slice = self._raw()
        raw_bytes = lib.ditto_document_id_query_compatible(doc_id_slice[0],
                                    lib.STRING_PRIMITIVE_FORMAT_WITHOUT_QUOTES)

        return string(raw_bytes)

    def __eq__(self, other: object) -> bool:
        """Return True is two DocumentId are equal.

        Args:
            other (object): Any object

        Returns:
            bool: True if the DocumentId are equal.
        """
        if not isinstance(other, DocumentId):
            return False
        return self.__bytes == other.__bytes
