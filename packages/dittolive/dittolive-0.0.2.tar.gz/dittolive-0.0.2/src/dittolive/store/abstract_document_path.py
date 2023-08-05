"""Abstract Document Path.

This centralize the duplicated logic between DocumentPath and MutableDocumentPath.
"""

from abc import ABC, abstractmethod
import cbor2
from typing import Union

from _dittoffi import lib
from dittolive.exceptions import FfiException
from dittolive._utils import char_p, bytes_from_boxed
from .document_id import DocumentId

class AbstractDocumentPath(ABC):
    """Path in a document."""
    def __init__(self, doc_ptr, doc_id: DocumentId, key):
        """Init a document path."""
        self._path = key
        self._doc_id = doc_id
        self._doc_ptr = doc_ptr

    # use key: str | int when upgrading to Python 3.10
    def get(self, key: Union[int, str]):
        """Get subpath.

        Use to specify a path to a key in the document that you can
        subscript further to access a nested key in the document.
        """
        if isinstance(key, int):
            self._path += f"[{key}]"
        else:
            if not key:
                return self
            self._path += f".{key}"

        return self

    # use key: str | int when upgrading to Python 3.10
    def __getitem__(self, key):
        """Get subpath.

        Use to specify a path to a key in the document that you can
        subscript further to access a nested key in the document.
        """
        return self.get(key)

    def __value_with_type(self, path_type: int) -> dict:
        cbor_res = lib.ditto_document_get_cbor_with_path_type(self._doc_ptr,
                                                char_p(self._path),
                                                path_type)

        if cbor_res.status_code != 0:
            raise FfiException

        cbor_bytes = bytes_from_boxed(cbor_res.cbor)
        if cbor_bytes is None:
            return None

        return cbor2.loads(cbor_bytes)

    @property
    def value(self) -> dict:
        """Return value at given path.

        Returns:
            object: dict representation of your object.
            None: if the path doesn't exist

        Raises:
            FfiException
        """
        return self.__value_with_type(lib.PATH_ACCESSOR_TYPE_ANY)

    @abstractmethod
    def get_attachment_token(self) -> dict:
        """Get inner attachment token.

        Returns the value at the previously specified key in the document as
        an `AttachmentToken`. If the key was invalid the return is `None`.
        """
        return self.__value_with_type(lib.PATH_ACCESSOR_TYPE_ATTACHMENT)

    @abstractmethod
    def get_counter(self) -> dict :
        """Get inner counter.

        Returns the value at the previously specified key in the document as
        a `DittoCounter`. If the key is invalid or the value is not a `DittoCounter`
        the return is `None`.
        """
        return self.__value_with_type(lib.PATH_ACCESSOR_TYPE_COUNTER)

    @abstractmethod
    def get_register(self) -> dict :
        """Get inner register.

        Returns the value at the previously specified key in the document as
        a `DittoRegister`. If the key is invalid or the value is not a `DittoRegister`
        the return is `None`.
        """
        return self.__value_with_type(lib.PATH_ACCESSOR_TYPE_REGISTER)
