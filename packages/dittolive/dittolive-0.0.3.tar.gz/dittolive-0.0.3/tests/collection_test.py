from dittolive import *
from utils import create_offline_ditto

def test_find_by_id_document():
    ditto = create_offline_ditto()
    collection = ditto.store["test"]
    doc_id = collection.upsert({"key": "value"})

    doc = collection.find_by_id(doc_id).exec()
    assert doc != None