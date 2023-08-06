"""Module identity."""

from abc import ABC, abstractmethod
from _dittoffi import lib

class Identity(ABC):
    """Abstract class for all identities."""

    def __init__(self, app_id:str):
        """Init motherclass of all Identities."""
        self.__app_id = app_id
        self._auth_client = None

    def app_id(self):
        """Returns the AppId currently in use by this peer."""
        return self.__app_id

    def site_id(self):
        """Returns the current SiteId identifying the Ditto peer."""
        raise NotImplementedError

    def auth_client(self):
        """Returns a shared reference to the underlying AuthClient."""
        if self._auth_client is None :
            raise ValueError("No `auth_client` available")
        return self._auth_client

    @abstractmethod
    def _authenticate(self, working_dir: str):
        """Auth a given type of Identity."""

    def is_web_valid(self) -> bool:
        """Returns if the current web auth token is valid."""
        return lib.ditto_auth_client_is_web_valid(self.auth_client()) == 1

    def is_x509_valid(self) -> bool:
        """Returns if the configured x509 certificate is valid."""
        return lib.ditto_auth_client_is_x509_valid(self.auth_client()) == 1

    def close(self):
        """Close the identity."""
        if self._auth_client is None:
            return

        lib.ditto_auth_client_free(self._auth_client)
        self._auth_client = None

    def requires_offline_license_token(self):
        """Return true if the Identity requires an offline license token."""
        return False

    def is_cloud_sync_enabled(self):
        """Return true is the connection with Ditto cloud is enabled."""
        return False

    def _is_online(self):
        """Return true is the Identity should have an access to Ditto cloud."""
        return False

    def _sync_url(self) -> str:
        return f"wss://{self.app_id()}.cloud.ditto.live"

    def _auth_url(self) -> str:
        return f"https://{self.app_id()}.cloud.ditto.live"
