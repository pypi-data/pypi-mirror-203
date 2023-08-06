from utils import create_offline_ditto

def test_get_collection():
    ditto = create_offline_ditto()
    store = ditto.store
    store.collection("collection_name")
    store["collection_name"]

def test_collections():
    ditto = create_offline_ditto()
    store = ditto.store
    store.collection("collection_name1")
    store.collection("collection_name2")
    store.collection("collection_name3")