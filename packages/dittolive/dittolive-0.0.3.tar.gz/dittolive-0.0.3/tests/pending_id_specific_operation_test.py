import pytest
import time

from dittolive import *
from utils import create_offline_ditto
from dittolive.exceptions import DocumentNotFoundException
from asyncio.futures import Future
import asyncio

def test_subscribe():
    ditto = create_offline_ditto()
    collection = ditto.store["test"]
    doc_id = collection.upsert({"content": "value"})
    sub = collection.find_by_id(doc_id).subscribe()
    assert sub
    sub.close()

@pytest.mark.asyncio
async def test_observe_lambda():
    ditto = create_offline_ditto()
    collection = ditto.store["test"]
    doc_id = collection.upsert({"content": "value"})
    future = Future()

    callback = lambda doc, event : future.set_result(True)
    live_query = collection.find_by_id(doc_id).observe(callback)
    doc_id = collection.upsert({"_id": str(doc_id), "content": "New value"})
    await future
    live_query.close()

@pytest.mark.asyncio
async def test_observe_scoped_function_by_upsert():
    future = Future()
    counter = 0
    def scoped_function(doc, event):
        nonlocal counter
        if counter == 0:
            counter += 1
        else:
            future.set_result(True)

    ditto = create_offline_ditto()
    collection = ditto.store["test"]
    doc_id = collection.upsert({"content": "value"})

    live_query = collection.find_by_id(doc_id).observe(scoped_function)

    doc_id = collection.upsert({"_id": str(doc_id), "content": "New value"})
    while not future.done(): # Directly calling `await future` locks the thread
        await asyncio.sleep(0.01)
    live_query.close()

@pytest.mark.asyncio
async def test_observe_scoped_function_by_update():
    future = Future()
    counter = 0

    def scoped_function(doc, event):
        nonlocal counter
        if counter == 0:
            counter += 1
        else:
            future.set_result(True)

    ditto = create_offline_ditto()
    collection = ditto.store["test"]
    doc_id = collection.upsert({"content": "value"})

    live_query = collection.find_by_id(doc_id).observe(scoped_function)

    updater = lambda mut_doc: mut_doc["new_content"].set("BrandNewSDK")
    collection.find_by_id(doc_id).update(updater)

    while not future.done(): # Directly calling `await future` locks the thread
        await asyncio.sleep(0.01)
    live_query.close()

def test_remove():
    ditto = create_offline_ditto()
    collection = ditto.store["test"]

    doc_id = collection.upsert({"content": "value"})
    doc = collection.find_by_id(doc_id).exec()

    collection.find_by_id(doc_id).remove()

    with pytest.raises(DocumentNotFoundException):
        doc = collection.find_by_id(doc_id).exec()

    collection.find_by_id(doc_id).remove()

def test_evict():
    ditto = create_offline_ditto()
    collection = ditto.store["test"]

    doc_id = collection.upsert({"content": "value"})
    doc = collection.find_by_id(doc_id).exec()

    collection.find_by_id(doc_id).evict()
    with pytest.raises(DocumentNotFoundException):
        doc = collection.find_by_id(doc_id).exec()
    collection.find_by_id(doc_id).evict()

def test_exec():
    ditto = create_offline_ditto()
    collection = ditto.store["test"]

    doc_id = collection.upsert({"content": "value"})
    doc = collection.find_by_id(doc_id).exec()
    doc != None

def test_update_lambda():
    ditto = create_offline_ditto()
    collection = ditto.store["test"]
    doc_id = collection.upsert({"content": "value"})
    doc = collection.find_by_id(doc_id).exec()
    assert doc["content"].value == "value"
    cb = lambda mut_doc : mut_doc["content"].set(3)
    result = collection.find_by_id(doc_id).update(cb)

    #TODO result
    doc = collection.find_by_id(doc_id).exec()
    assert doc["content"].value == 3

def test_update_function():
    ditto = create_offline_ditto()
    collection = ditto.store["test"]

    def updater(mut_doc):
        mut_doc["content"] = 3

    doc_id = collection.upsert({"content": "value"})
    doc = collection.find_by_id(doc_id).exec()
    assert doc["content"].value == "value"
    result = collection.find_by_id(doc_id).update(updater)

    #TODO result
    doc = collection.find_by_id(doc_id).exec()
    assert doc["content"].value == 3