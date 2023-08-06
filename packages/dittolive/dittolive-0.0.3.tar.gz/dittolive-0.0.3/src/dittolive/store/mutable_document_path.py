"""Path of a MutableDocument."""
from _dittoffi import lib
from .abstract_document_path import AbstractDocumentPath
from dittolive._utils import char_p, cbor_slice_ref_uint8
from dittolive.exceptions import FfiException
from .update_result import UpdateResultSet, UpdateResultRemoved

class MutableDocumentPath(AbstractDocumentPath):
    """Mutable Document path."""

    def __init__(self, doc_ptr, doc_id, key, results):
        """init."""
        super().__init__(doc_ptr, doc_id, key)
        self.results = results

    """Path of a MutableDocument."""
    def get_attachment_token(self):
        """Get attachment token.

        Returns the value at the previously specified key in the document as
        an `AttachmentToken`. If the key was invalid the return is `None`.
        """
        raise NotImplementedError

    def get_counter(self):
        """Get mutable counter.

        Returns the value at the previously specified key in the document as
        a `DittoCounter`. If the key is invalid or the value is not a `DittoCounter`
        the return is `None`.
        """
        raise NotImplementedError

    def get_register(self):
        """Get mutable register.

        Returns the value at the previously specified key in the document as
        a `DittoRegister`. If the key is invalid or the value is not a `DittoRegister`
        the return is `None`.
        """
        raise NotImplementedError

    @AbstractDocumentPath.value.setter
    def value(self, value):
        """Set a value to the current path.

        Args:
            value (_type_): Should be cbor serializable
        """
        self.set(value)

    def set(self, value, is_default:bool = False):
        """Set value at current path.

        Set a value at the document's key defined by the preceding
        subscripting.
        """
        cbor_slice = cbor_slice_ref_uint8(value)
        path = char_p(self._path)

        if is_default:
            res = lib.ditto_document_set_cbor_with_timestamp(self._doc_ptr,
                    path,
                    cbor_slice[0],
                    0)
        else:
            res = lib.ditto_document_set_cbor(self._doc_ptr, path, cbor_slice[0])

        if res != 0:
            raise FfiException

        self.results.append(UpdateResultSet(self._doc_id, self._path, value))

    def remove(self):
        """Remove value at current path.

        Remove a value at the document's key defined by the preceding
        subscripting.
        """
        lib.ditto_document_remove(self._doc_ptr, char_p(self._path))
        self.results.append(UpdateResultRemoved(self._doc_id, self._path))

    def __setitem__(self, key, value):
        """Set value.

        Args:
            key (_type_): path to the field
            value (_type_): value to be set
        """
        self[key].value = value
