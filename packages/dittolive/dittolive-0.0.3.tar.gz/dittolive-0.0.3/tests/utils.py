from dittolive import *
from dittolive import TransportConfig
from dittolive.identity import OfflinePlayground, OnlinePlayground

import tempfile
import uuid

APP_ID = "1eea99ab-0d02-4f6f-8b33-c8c8fff74d60"

PLAYGROUND_TOKEN = "e7b5606a-4574-43f3-8caa-2baff0889837"

TEST_LICENSE: str = "\
    o2d1c2VyX2lkc2ludGVybmFsQGRpdHRvLmxpdmVmZXhwaXJ5dDIwMjUtMTItMzFUMDA\
    6MDA6MDBaaXNpZ25hdHVyZXhYSnZlcDBWT1JwSXdHY2l5REZKaVBUUEJaTVlaN0lZR\
    XhGUFNVc2I3OTRwcjhwVjdlNjRQUkRJQ1NFNjRWeGozZFc0em5QU3Z2THBxMHBkZmh\
    kOFc4YlE9PQ==\
"

def create_offline_ditto(*, working_dir :str = None, identity = OfflinePlayground("AppId", 42), transport_config: TransportConfig = TransportConfig()):
    """"
    Create an offline ditto instance
    """

    if not working_dir:
        tmp_path = tempfile.gettempdir()
        random_folder = str(uuid.uuid4())
        working_dir = f"{tmp_path}/{random_folder}/ditto"

    ditto = Ditto(identity, working_dir = working_dir, transport_config = transport_config)
    ditto.set_offline_only_license_token(TEST_LICENSE)

    return ditto

def create_online_ditto(*, working_dir :str = None, 
                        app_id: str = APP_ID,
                        token:str = PLAYGROUND_TOKEN,
                        transport_config: TransportConfig = TransportConfig()):
    """"
    Create an online playground ditto instance
    """

    identity = OnlinePlayground(app_id, token, cloud_sync_enabled = True)

    if not working_dir:
        tmp_path = tempfile.gettempdir()
        random_folder = str(uuid.uuid4())
        working_dir = f"{tmp_path}/{random_folder}/ditto"

    ditto = Ditto(identity, working_dir = working_dir, transport_config = transport_config)
    ditto.set_offline_only_license_token(TEST_LICENSE)

    return ditto
