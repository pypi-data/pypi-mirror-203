"""OfflinePlayground is an Identity target for development."""
from _dittoffi import lib

from .identity import Identity
from dittolive._utils import char_p
from dittolive.exceptions import FfiException

class OfflinePlayground(Identity):
    """OfflinePlayground is an Identity target for development."""
    def __init__(self, app_id: str, site_id: int):
        """Init an Offline playground."""
        super().__init__(app_id)
        self.__site_id = site_id

    def _authenticate(self, working_dir:str):
        """Authenticate the offline playground.

        Args:
            working_dir (str): Working dir path

        Raises:
            FfiException: Raised if auth fails
        """
        working_dir_bytes = char_p(working_dir)
        app_id_bytes = char_p(self.app_id())
        result = lib.ditto_auth_client_make_for_development(
            working_dir_bytes,
            app_id_bytes,
            self.__site_id)

        if result.status_code != 0:
            raise FfiException

        self._auth_client = result.auth_client

    def _requires_offline_license_token(self) -> bool:
        """Return if the offline license is required.

        Returns:
            bool : True if license is required
        """
        return True
