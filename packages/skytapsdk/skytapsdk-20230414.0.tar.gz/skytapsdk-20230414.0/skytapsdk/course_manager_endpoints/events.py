"""Events Class for calling "events" API endpoints."""
import requests
from restfly.endpoint import APIEndpoint


class Events(APIEndpoint):
    """
    "Events" API endpoint
    """

    _path = "events"

    def get(
        self,
        event_id: str = None,
    ) -> requests.Response:
        if event_id:
            self._path = f"{self._path}/{event_id}"
        return self._get(verify=False)

    def get_participants(
        self,
        event_id: str,
        participant_id: str = None,
    ) -> requests.Response:
        pass  # FIXME: This doesn't work yet.
        # self._path = f"{self._path}/{event_id}"
        # parameters = {
        #     "tab": "participants-tab",
        # }
        # return self._get(verify=False, params=parameters,)

        # self._path = f"{self._path}/{event_id}/students"
        # if participant_id:
        #     self._path = f"{self._path}/{participant_id}"
        # return self._get(verify=False)

    def update_participants(
        self,
        event_id: str,
        participant_id: str,
        payload: dict,
    ) -> requests.Response:
        self._path = f"{self._path}/{event_id}/event_participants/{participant_id}"
        return self._patch(
            json=payload,
            verify=False,
        )
