"""LiveQuery are used to monitore documents changes."""

from typing import Callable, List

from dittolive.__observer import Observer
from dittolive._utils import empty_slice_ref_uint8, empty_order_slice_ref
from dittolive.exceptions import FfiException
from _dittoffi import ffi, lib
from .document import Document

UNASSIGNED_ID_SENTINEL: int = -1

class LiveQueryMove():
    """Live Query Move.

    Describes the index in a list of documents that a document was previously found at
    `origin` and the index that it can now be found at `to`.
    """
    def __init__(self, origin, to):
        """Creates a new LiveQuery move."""
        self._left = origin
        self._right = to

class _LiveQueryEvent():
    def __init__(self,*, is_initial = False) -> None:
        self._is_initial = is_initial

    def is_initial(self) -> bool:
        return self._is_initial
class _LiveQueryInitial(_LiveQueryEvent):
    def __init__(self) -> None:
        super().__init__(is_initial = True)

class _LiveQueryUpdate(_LiveQueryEvent):
    def __init__(self, c_cb_params):
        super().__init__(is_initial = False)
        #TODO : Params here are not ready to be used

        raw_vec_documents = c_cb_params.old_documents
        docs_ptr = raw_vec_documents.ptr
        docs_number = raw_vec_documents.len
        self.old_documents = [Document(docs_ptr[i]) for i in range(docs_number)]

        #TODO
        # self.insertions = c_cb_params.insertions
        # self.deletions = c_cb_params.deletions
        # self.updates = c_cb_params.updates
        # self.moves = [LiveQueryMove(left, right) for (left,right)
        #   in groupby(c_cb_params.moves, 2)] # TODO

# TODO: This should be an event callback list
# WITH the list of Documents inside
LiveQueryDocumentCallback = Callable[[List[Document], _LiveQueryEvent], None]

@ffi.callback("void(void*, c_cb_params_t)")
def c_live_query_event_handler(live_query_ptr, params):
    """C callback for live query. This is passed to the Rust core through the FFi."""
    live_query = ffi.from_handle(live_query_ptr)
    #compute documents
    raw_vec_documents = params.documents
    docs_ptr = raw_vec_documents.ptr
    docs_number = raw_vec_documents.len
    documents = [Document(docs_ptr[i]) for i in range(docs_number)]

    # handle event
    if params.is_initial:
        live_query.callback(documents, _LiveQueryInitial())
    else:
        event = _LiveQueryUpdate(params)
        live_query.callback(documents, event)
        lib.ditto_only_vec_documents_free(params.old_documents)

    lib.ditto_free_indices(params.insertions)
    lib.ditto_free_indices(params.deletions)
    lib.ditto_free_indices(params.updates)
    lib.ditto_free_indices(params.moves)
    lib.ditto_only_vec_documents_free(params.documents)

    #TODO Free fields in params

class LiveQuery(Observer):
    """LiveQuery."""
    def __init__(self, raw_ditto, query: bytes, coll_name: bytes,
                 callback: LiveQueryDocumentCallback,
                 *, query_args=None, order_by=None,
                 limit: int = -1, offset: int = 0,
                 availability=lib.LIVE_QUERY_AVAILABILITY_ALWAYS):
        """Creates a new LiveQuery.

        Args:
            raw_ditto (_type_): _description_
            query (bytes): _description_
            coll_name (bytes): _description_
            callback (LiveQueryDocumentCallback): _description_
            query_args (_type_, optional): _description_. Defaults to None.
            order_by (_type_, optional): _description_. Defaults to None.
            limit (int, optional): _description_. Defaults to -1.
            offset (int, optional): _description_. Defaults to 0.
            availability (_type_, optional): _description_.
                Defaults to lib.LIVE_QUERY_AVAILABILITY_ALWAYS.

        Raises:
            FfiException: _description_
        """
        super().__init__()
        handle = ffi.new_handle(self)

        self.__raw_ditto = raw_ditto
        self.__query = query
        self.__collection_name = coll_name,
        self.callback = callback
        self.__handle =handle

        args = empty_slice_ref_uint8()
        order_by = empty_order_slice_ref()

        res = lib.ditto_live_query_register_str(
            raw_ditto,
            coll_name,
            query,
            args[0],  # args params
            order_by[0],  # Order by
            limit,
            offset,
            availability,
            handle,  # ptr to self
            # TODO: add proper retain/release mechanism
            ffi.NULL,  # retain
            ffi.NULL,  # release
            c_live_query_event_handler  # c callback
        )

        if res.status_code != 0:
            raise FfiException

        self.__id = res.i64

        if self.__id == UNASSIGNED_ID_SENTINEL:
            raise ValueError("Not a valid LiveQuery ID")
            # LiveQuery was not given a valid id
        else:
            pass
            # TODO : log this
            # Log valid query id

        lib.ditto_live_query_start(raw_ditto, self.__id)

    def _close_callback(self):
        """Drop the live query."""
        # TODO : log this
        lib.ditto_live_query_stop(self.__raw_ditto, self.__id)
