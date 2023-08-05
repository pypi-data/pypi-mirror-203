import logging

from restfly.session import APISession

from .course_manager_endpoints import Events, SelfLearners


class CourseManager(APISession):
    """A controller to access Endpoints in the Skytap Course Manager API."""

    BASE_URL = "https://zscaler.skytap-portal.com/api/v1"

    def __init__(
        self,
        token: str = None,
        secret: str = None,
        **kwargs,
    ):
        """
        Create a Skytap object for managing interactions with the Skytap API.

        Args:
            token: Username for API auth
            secret: Token for API auth (preferred over password)
            kwargs: Various settable values
                api_version (int) Defaults to self.API_VERSION.
        """

        self._token = token
        self._secret = secret
        self._url = self.BASE_URL

        super(CourseManager, self).__init__(
            token=self._token,
            secret=self._secret,
            **kwargs,
        )
        self.login()

    def login(self) -> None:
        self._session.auth = (
            self._token,
            self._secret,
        )

    def logout(self):
        self._session.auth = None

    @property
    def self_learners(self) -> SelfLearners:
        return SelfLearners(self)

    @property
    def events(self) -> Events:
        return Events(self)
