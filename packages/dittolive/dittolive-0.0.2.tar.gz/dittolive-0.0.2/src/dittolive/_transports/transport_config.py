
DEFAULT_TCP_IPV6 = "[::]"
NO_PREFERRED_ROUTE_HINT = 0

class TransportConfig:
    def __init__(self):
        self.peer_to_peer = PeerToPeer()
        self.connect = Connect()
        self.listen = Listen()
        self._global_config = Global()

    @property
    def bluetooth_enabled(self) -> bool:
        """Return True if bluetooth is enabled.

        Returns:
            bool: bluetooth is enabled
        """
        return self.peer_to_peer.ble.enabled

    @bluetooth_enabled.setter
    def bluetooth_enabled(self, enabled:bool):
        """Set if bluetooth is enabled or not.

        Args:
            enabled (bool): enable Bluetooth or not
        """
        self.peer_to_peer.ble.enabled = enabled

    @property
    def sync_group(self) -> int:
        """Return sync group number.

        Returns:
            int: SyncGroup
        """
        return self._global_config.sync_group

    @sync_group.setter
    def sync_group(self, sync_group:int):
        """Set sync group.

        Args:
            sync_group (int): Sync group
        """
        self._global_config.sync_group = sync_group

class PeerToPeer:
    def __init__(self):
        self.ble = BluetoothLEConfig()
        self.lan = LanConfig()

class BluetoothLEConfig:
    def __init__(self):
        self.enabled = False

class LanConfig:
    def __init__(self):
        self.enabled = False
        self.mdns_enabled = True
        self.multicast_enabled = True

class Connect:
    def __init__(self):
        self.tcp_servers = set()
        self.websocket_urls = set()
        # duration in seconds
        self.retry_interval = 5

class Listen:
    def __init__(self):
        self.tcp = TcpConfig()
        self.http = HttpListenConfig()

class TcpConfig:
    def __init__(self):
        self.enabled = False
        self.interface_ip = DEFAULT_TCP_IPV6
        self.port = 4040

class HttpListenConfig:
    def __init__(self):
        self.enabled = False
        self.interface_ip = DEFAULT_TCP_IPV6
        self.port = 80
        self.static_content_path = None
        self.websocket_sync = True
        self.tls_key_path = None
        self.tls_certificate_path = None

class Global:
    def __init__(self):
        self.sync_group = 0
        self.routing_hint = NO_PREFERRED_ROUTE_HINT
