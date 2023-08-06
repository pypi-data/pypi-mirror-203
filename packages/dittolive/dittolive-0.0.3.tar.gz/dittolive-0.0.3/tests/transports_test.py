from dittolive import Ditto
from dittolive import TransportConfig

from utils import create_offline_ditto, create_online_ditto

def test_enable_ble():
    transport_config = TransportConfig()
    transport_config.ble_enabled = True
    ditto = create_offline_ditto(transport_config=transport_config)
    ditto.start_sync()
    with ditto.open_transport_config() as config:
        config.bluetooth_enabled = False

def test_edit_lan():
    transport_config = TransportConfig()
    transport_config.lan_enabled = True
    ditto = create_offline_ditto(transport_config=transport_config)
    ditto.start_sync()
    with ditto.open_transport_config() as config:
        config.lan_enabled = False

def test_edit_tcp():
    transport_config = TransportConfig()
    transport_config.tcp_enabled = True
    transport_config.listen.tcp.interface_ip = "127.0.0.1"
    transport_config.listen.tcp.port = "16042"
    transport_config.connect.tcp_servers.add("127.0.0.1:16041")
    ditto = create_offline_ditto(transport_config=transport_config)
    ditto.start_sync()
    with ditto.open_transport_config() as config:
        config.tcp_enabled = False

def test_edit_ws():
    transport_config = TransportConfig()
    ditto = create_online_ditto(transport_config=transport_config)
    ditto.start_sync()
    with ditto.open_transport_config() as config:
        config.connect.websocket_urls.add("wss://brand_new_websocket.ditto.live")

    with ditto.open_transport_config() as config:
        config.connect.websocket_urls.remove("wss://brand_new_websocket.ditto.live")

    ditto.stop_sync()
