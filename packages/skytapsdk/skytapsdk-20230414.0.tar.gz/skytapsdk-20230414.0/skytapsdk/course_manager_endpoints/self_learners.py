"""SelfLearners Class for calling "self_learners" API endpoints."""
import requests
from restfly.endpoint import APIEndpoint


class SelfLearners(APIEndpoint):
    """
    "SelfLearners" API endpoint
    """

    _path = "/self_learners"

    def create(
        self,
        payload: dict,
    ) -> requests.Response:
        return self._post(json=payload, verify=False)
