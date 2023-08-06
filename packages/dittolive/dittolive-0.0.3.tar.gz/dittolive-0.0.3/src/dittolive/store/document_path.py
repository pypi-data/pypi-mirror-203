"""Path in a document."""

from .abstract_document_path import AbstractDocumentPath
class DocumentPath(AbstractDocumentPath):
    """Read only view of a Document at specified path."""
    def get_attachment_token(self):
        """Get inner attachment token.

        Returns the value at the previously specified key in the document as
        an `AttachmentToken`. If the key was invalid the return is `None`.
        """
        raise NotImplementedError

    def get_counter(self):
        """Get inner counter.

        Returns the value at the previously specified key in the document as
        a `DittoCounter`. If the key is invalid or the value is not a `DittoCounter`
        the return is `None`.
        """
        raise NotImplementedError

    def get_register(self):
        """Get inner register.

        Returns the value at the previously specified key in the document as
        a `DittoRegister`. If the key is invalid or the value is not a `DittoRegister`
        the return is `None`.
        """
        raise NotImplementedError
