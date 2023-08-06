"""OnlinePlayground for testing sync."""

from _dittoffi import lib

from .identity import Identity
from dittolive._utils import char_p
from dittolive.exceptions import FfiException

class OnlinePlayground(Identity):
    """Class OnlinePlayground."""
    def __init__(self, app_id: str, shared_token:str, *, custom_auth_url:str=None,
                cloud_sync_enabled:bool = False):
        """Create a new OnlinePlayground.

        Args:
            app_id (str): application id, as an UUID string
            shared_token (str): Token shared between apps
            custom_auth_url (str, optional): Custom URL for authentication.
                Defaults to None.
            cloud_sync_enabled (bool, optional): Should this peer sync with Ditto cloud.
                Default to False
        """
        super().__init__(app_id=app_id)
        self.__shared_token = shared_token
        self.__custom_auth_url = custom_auth_url
        self.__cloud_sync_enabled = cloud_sync_enabled

    def _authenticate(self, working_dir: str):
        working_dir_bytes = char_p(working_dir)
        app_id_bytes = char_p(self.app_id())
        shared_token_bytes = char_p(self.__shared_token)

        if self.__custom_auth_url:
            url_bytes = char_p(self.__custom_auth_url)
        else:
            url_bytes = char_p(self._auth_url())

        result = lib.ditto_auth_client_make_anonymous_client(
            working_dir_bytes,
            app_id_bytes,
            shared_token_bytes,
            url_bytes)

        if result.status_code != 0:
            raise FfiException

        self._auth_client = result.auth_client

    def is_cloud_sync_enabled(self):
        """Return true is the connection with Ditto cloud is enabled."""
        return self.__cloud_sync_enabled

    def _is_online(self):
        """Return true is the connection with Ditto cloud is enabled."""
        return True
