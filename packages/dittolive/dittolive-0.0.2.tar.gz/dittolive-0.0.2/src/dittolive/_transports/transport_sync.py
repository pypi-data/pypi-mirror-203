from _dittoffi import lib
from .transport_config import TransportConfig, LanConfig, TcpConfig
from .sync_state import SyncState
from dittolive.identity import Identity
from dittolive._utils import char_p

class TransportSync:
    """Transport sync."""
    def __init__(self, config : TransportConfig, ditto, identity: Identity):

        self.__requested_state = SyncState(config, identity)
        self.__effective_state = SyncState(TransportConfig(), identity)

        self.__ws_clients = dict()

        self.mdns_client_transporter = None
        self.mdns_server_advertiser = None

        self.ble_client_transport = None
        self.ble_server_transport = None

        self.__raw_ditto = ditto

    def _update(self):
        """Update Transport layer using provided parameter.

        Afterward, it also update the effective configuration
        and applies changes.
        """
        future_state = self.__requested_state.compute_effective_state()
        self.apply_transport_state(future_state, self.__effective_state)
        self.apply_transport_global_state(future_state, self.__effective_state)
        self.__effective_state = future_state

    def apply_transport_state(self, future:SyncState, old: SyncState):
        self.__update_peer_to_peer_bluetooth_le(future, old)
        self.__update_peer_to_peer_lan(future, old)
        self.__update_listen_tcp(future, old)
        self.__update_listen_http(future, old)
        self.__update_connect_tcp_servers(future, old)
        self.__update_connect_websocket_url(future, old)
        self.__update_connect_retry_interval(future, old)

    def start_sync(self):
        """Start sync in the config."""
        self.__requested_state.sync = True
        self._update()

    def stop_sync(self):
        """Stop sync."""
        self.__requested_state.sync = False
        self._update()

    @property
    def transport_config(self):
        return self.__requested_state.transport_config

    def apply_transport_global_state(self, future: SyncState, old:SyncState):
        new_sync_group = future.transport_config.sync_group
        old_sync_group = old.transport_config.sync_group

        if new_sync_group != old_sync_group:
            lib.ditto_set_sync_group(self.__raw_ditto, new_sync_group)

    def __update_peer_to_peer_lan(self, future:SyncState, old:SyncState):
        """Apply changes in the lan config."""

    def __update_peer_to_peer_bluetooth_le(self, future:SyncState, old:SyncState):
        """Apply changes in the BLE config."""

    def __update_listen_tcp(self, future:SyncState, old:SyncState):
        """Apply changes in the TCP config."""

    def __update_listen_http(self, future:SyncState, old:SyncState):
        """Apply changes in the HTTP config."""

    def __update_connect_tcp_servers(self, future:SyncState, old:SyncState):
        """Apply changes in the TCP servers config."""

    def __update_connect_websocket_url(self, future:SyncState, old:SyncState):
        """Apply changes in the websocket url."""
        old_addresses = old.transport_config.connect.websocket_urls
        new_addresses = future.transport_config.connect.websocket_urls
        for address in old_addresses.difference(new_addresses):
            self.__stop_ws(address)

        routing_hint = self.transport_config._global_config.routing_hint
        for address in new_addresses.difference(old_addresses):
            self.__start_ws(address, routing_hint)

    def __stop_ws(self, address):
        handle = self.__ws_clients.pop(address)
        lib.websocket_client_free_handle(handle)

    def __start_ws(self, address:str, routing_hint:int):
        handle = lib.ditto_add_websocket_client(self.__raw_ditto,
                                                char_p(address), routing_hint)
        self.__ws_clients[address] = handle

    def __update_connect_retry_interval(self, future:SyncState, old:SyncState):
        """Apply changes in connect retry interval."""
