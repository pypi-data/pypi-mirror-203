"""Result returned when updating a document."""

from enum import Enum
from .document_id import DocumentId

class UpdateResultType(Enum):
    """Type of the update."""
    Set = 0,
    Removed = 1,

class UpdateResult:
    """Generic update result."""
    def __init__(self, doc_id: DocumentId, path:str, operation_type: UpdateResultType):
        """Create a new UpdateResult."""
        self.doc_id = doc_id
        self.path = path
        self.operation_type = operation_type

class UpdateResultSet(UpdateResult):
    """Result returned when setting a value in a mutable document."""
    def __init__(self, doc_id: DocumentId, path: str, value):
        """Create a new UpdateResultSet."""
        super().__init__(doc_id, path, UpdateResultType.Set)
        self.value = value

class UpdateResultRemoved(UpdateResult):
    """Result returned when removing a value from a mutable document."""
    def __init__(self, doc_id: DocumentId, path: str):
        """Create a new UpdateResultRemoved."""
        super().__init__(doc_id, path, UpdateResultType.Removed)
