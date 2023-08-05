"""Ditto module."""

import platform
import os
from _dittoffi import lib

from .identity import Identity
from .log import LogLevel
from .store import Store
from ._utils import char_p
from .exceptions import NotActivatedException, ConfigException, LicenseException
from ._transports import TransportConfig, TransportSync
from contextlib import contextmanager

def _sanitize_working_dir(working_dir:os.path):
    """Compute the effective Ditto working directory."""
    platform_name = platform.system()
    if not working_dir:
        if platform_name in ("Linux", "Darwin"):
            home = os.environ.get("HOME")
            working_dir = home + "/Documents/"
        elif platform_name == "Windows":
            raise NotImplementedError
        else:
            # Not supported platform
            raise NotImplementedError
    elif platform_name in ("Linux", "Darwin"):
        working_dir += "/"
    elif platform_name == "Windows":
        working_dir += "\\"
    else:
        # Not supported platform
        raise NotImplementedError
    working_dir += "ditto"
    return working_dir

class Ditto:
    """Ditto entry point."""
    def __init__(self, identity:Identity, *, working_dir:str = "",
            transport_config: TransportConfig = None):
        """Create a new Ditto instance.

        Args:
            identity (Identity): Identity used to identify the Ditto peer
            working_dir (str, optional): Directory where Ditto will persist data.
                Defaults to "".
            transport_config (TransportConfig, optional): _description_.
                Defaults to TransportConfig().
        """
        # Get local folder for Linux
        working_dir = _sanitize_working_dir(working_dir)

        # create uninitialized ditto
        uninitialized_ditto = lib.uninitialized_ditto_make(char_p(working_dir))
        # get auth client from identity
        identity._authenticate(working_dir)
        auth_client = identity.auth_client()
        # create real raw handle to ditto
        raw_ditto = lib.ditto_make(uninitialized_ditto, auth_client,
            lib.HISTORY_TRACKING_DISABLED)

        self.__activated = not identity.requires_offline_license_token()
        self.__store = Store(raw_ditto)
        if transport_config is None:
            transport_config = TransportConfig()

        if identity._is_online():
            transport_config.connect.websocket_urls.add(identity._sync_url())

        self.__transports = TransportSync(transport_config, raw_ditto, identity)
        self.__identity = identity
        self.__raw_ditto = raw_ditto

    def __del__(self):
        """Delete the ditto instance."""
        self.close()
        lib.ditto_free(self.__raw_ditto)

    def close(self):
        """Close the current ditto instance."""
        self.__identity.close()
        lib.ditto_stop_tcp_server(self.__raw_ditto)
        lib.ditto_shutdown(self.__raw_ditto)

    def set_license_from_env(self, var_name:str):
        """Load the license from a environment variable."""
        license_token = os.environ.get(var_name)

        if not license_token:
            raise ConfigException

        self.set_offline_only_license_token(license_token)

    def set_offline_only_license_token(self, license_token:str):
        """Set offline license token.

        Args:
            license_token (str): Content of the license

        Raises:
            LicenseException: Explain why license has been refused
        """
        # We are not interested in error messages for now

        err_msg = []
        c_license_token = char_p(license_token)

        result = lib.verify_license(c_license_token, err_msg )

        if result == lib.LICENSE_VERIFICATION_RESULT_LICENSE_OK:
            self.__activated = True
            return

        raise LicenseException

    def start_sync(self):
        """Start sync with other peers."""
        if not self.__activated and self.__identity.requires_offline_license_token():
            raise NotActivatedException
        self.__transports.start_sync()

    def stop_sync(self):
        """Stop sync with other peers."""
        self.__transports.stop_sync()

    def is_sync_active(self) -> bool:
        """Returns a flag indicating whether sync is active.

        Use `start_sync` to activate sync and `stop_sync` to deactivate sync.
        """
        raise NotImplementedError

    def authenticator(self):
        """Provides access to Authenticator.

        Use it for information and methods for logging on to Ditto Cloud.
        """

    def presence(self):
        """Provides access to the SDK's presence functionality."""
        raise NotImplementedError

    def disk_usage(self):
        """Provides access to the SDK's disk usage."""
        raise NotImplementedError

    @property
    def transport_config(self) -> TransportConfig:
        """Returns the current transport config."""
        return self.__transports.transport_config

    @contextmanager
    def open_transport_config(self):
        """Assign a new transports configuration.

        By default peer-to-peer transports (Bluetooth and WiFi, where available)
        are enabled.

        You may use this method to alter the configuration at any time. Sync will
        not begin until @ref start_sync is called.
        """
        try:
            yield self.transport_config
        finally:
            self.__transports._update()

    @property
    def store(self):
        """Give access to the Store."""
        return self.__store

    def is_logging_enabled(self) -> bool:
        """Gets whether or not logging is enabled for Ditto."""
        raise NotImplementedError

    def set_logging_enabled(self, enabled: bool):
        """Sets whether or not logging is enabled for Ditto."""
        raise NotImplementedError

    def emoji_log_level_headings_enabled(self) -> bool:
        """Gets whether emoji log level headings are enabled for Ditto."""
        raise NotImplementedError

    def set_emoji_log_level_heading_enabled(self, enabled: bool):
        """Sets whether emoji log level headings are enabled for Ditto."""
        raise NotImplementedError

    def minimum_log_level(self) -> LogLevel:
        """Gets the minimum log level at which logs will be emitted for Ditto."""
        raise NotImplementedError

    def set_minimum_log_level(self, log_level: LogLevel):
        """Sets the minimum log level at which logs should be emitted for Ditto."""
        raise NotImplementedError

    def app_id(self) -> str:
        """Gets the Ditto application Id."""
        raise NotImplementedError

    def persistence_directory(self) -> str:
        """Gets the persistence directory used by Ditto to persist data."""
        raise NotImplementedError
