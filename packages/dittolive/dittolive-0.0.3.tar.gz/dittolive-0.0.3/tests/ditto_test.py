from dittolive import Ditto, OfflinePlayground

from utils import TEST_LICENSE, create_offline_ditto

def test_restart_ditto():
    ditto = create_offline_ditto(working_dir = "/tmp/dittorestartsync")
    ditto.start_sync()
    ditto.stop_sync()
    del ditto
    ditto = create_offline_ditto(working_dir = "/tmp/dittorestartsync")

    ditto.start_sync()
    ditto.stop_sync()

def test_start_sync():
    ditto = create_offline_ditto(working_dir = "/tmp/dittostartsync")

    ditto.start_sync()
    ditto.start_sync()
    ditto.stop_sync()
    ditto.stop_sync()
    ditto.start_sync()
    ditto.stop_sync()