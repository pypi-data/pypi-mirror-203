"""State of TransportConfig."""

from .transport_config import TransportConfig
from dittolive.identity import Identity
import copy
class SyncState:
    def __init__(self, config: TransportConfig, identity: Identity):
        self.__sync_active = False
        self.__web_valid = identity.is_web_valid()
        self.__x509_valid = identity.is_x509_valid()
        self.__identity = identity
        self.transport_config = config

    @property
    def sync(self):
        self.__sync_active()

    @sync.setter
    def sync(self, activated: bool):
        self.__sync_active = activated

    @property
    def x509_valid(self) -> bool:
        return self.__x509_valid

    @x509_valid.setter
    def x509_valid(self, valid:bool):
        self.__x509_valid = valid

    @property
    def web_valid(self) -> bool:
        return self.__web_valid

    @web_valid.setter
    def web_valid(self, valid:bool):
        self.__web_valid = valid

    @property
    def sync(self) -> bool :
        return self.__sync_active

    @sync.setter
    def sync(self, activated:bool) -> bool:
        self.__sync_active = activated

    def compute_effective_state(self):
        patched_config = copy.deepcopy(self.transport_config)

        if not self.__sync_active or not self.__x509_valid:
            patched_config.peer_to_peer.ble.enabled = False
            patched_config.peer_to_peer.lan.enabled = False
            patched_config.listen.tcp.enabled = False
            patched_config.connect.tcp_servers = set()

        if not self.__sync_active or not self.__web_valid:
            patched_config.listen.http.enabled = False

        if (self.__identity.is_cloud_sync_enabled() and
                self.__sync_active):
            cloud_url = self.__identity._sync_url()
            patched_config.connect.websocket_urls.add(cloud_url)

        if (patched_config.peer_to_peer.lan.enabled and
                not patched_config.listen.tcp.enabled):
            patched_config.listen.tcp.enabled = True
            patched_config.listen.tcp.interface_ip = "[::]"
            patched_config.listen.tcp.port = 0

        return SyncState(patched_config, self.__identity)
