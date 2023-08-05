import pytest

from dittolive import *
from utils import create_offline_ditto
from dittolive.store.update_result import UpdateResultSet, UpdateResultRemoved

def test_document_id():
    ditto = create_offline_ditto()
    collection = ditto.store["test"]
    doc_id = collection.upsert({"key": "value"})

    doc = collection.find_by_id(doc_id).exec()

    assert doc.id() == doc_id

def test_document_value():
    ditto = create_offline_ditto()
    collection = ditto.store["test"]

    doc_id = b"documentId"
    content = {"_id": doc_id, "key" : "value", "other": 3, "array": [1, "two", '𒊺']}
    doc_id = collection.upsert(content)

    doc = collection.find_by_id(doc_id).exec()
    assert doc.value == content

def test_document_path():
    ditto = create_offline_ditto()
    collection = ditto.store["test"]
    content = {"key" : "value"}
    doc_id = collection.upsert(content)
    doc = collection.find_by_id(doc_id).exec()
    assert "value" == doc["key"].value

def test_composed_document_path():
    ditto = create_offline_ditto()
    collection = ditto.store["test"]
    content = {"key" : {"sub_key": "value"}}
    doc_id = collection.upsert(content)
    doc = collection.find_by_id(doc_id).exec()
    assert "value" == doc["key"]["sub_key"].value

def test_update_new_key():
    ditto = create_offline_ditto()
    collection = ditto.store["test"]
    content = {"key" : {"sub_key": "value"}}
    doc_id = collection.upsert(content)

def test_remove_path_from_document():
    ditto = create_offline_ditto()
    collection = ditto.store["test"]
    content = {"key" : {"sub_key": "value"}}
    doc_id = collection.upsert(content)
    updater = lambda mut_doc: mut_doc["key"].remove()
    collection.find_by_id(doc_id).update(updater)

    doc = collection.find_by_id(doc_id).exec()
    assert doc["key"].value is None

def test_remove_non_existing_path_from_document():
    ditto = create_offline_ditto()
    collection = ditto.store["test"]
    content = {"key" : "value"}
    doc_id = collection.upsert(content)

    updater = lambda mut_doc: mut_doc["potatoes"].remove()
    collection.find_by_id(doc_id).update(updater)

    doc = collection.find_by_id(doc_id).exec()
    assert doc["key"].value == "value"
    assert doc["potatoes"].value is None

def test_update_result():
    ditto = create_offline_ditto()
    collection = ditto.store["test"]
    content = {"key" : "value"}
    doc_id = collection.upsert(content)

    def updater(mut_doc):
        assert len(mut_doc.results) == 0
        mut_doc["key"] = 3
        mut_doc["other_key"] = "perlinpinpin"
        mut_doc["key"].remove()
        assert len(mut_doc.results) == 3
        assert isinstance(mut_doc.results[0], UpdateResultSet)
        assert mut_doc.results[0].value == 3
        assert mut_doc.results[0].path == "key"
        assert isinstance(mut_doc.results[1], UpdateResultSet)
        assert mut_doc.results[1].value == "perlinpinpin"
        assert mut_doc.results[1].path == "other_key"
        assert isinstance(mut_doc.results[1], UpdateResultSet)
        assert isinstance(mut_doc.results[2], UpdateResultRemoved)

    collection.find_by_id(doc_id).update(updater)

    doc = collection.find_by_id(doc_id).exec()
    assert doc["key"].value is None
    assert doc["other_key"].value == "perlinpinpin"