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
        **kwargs,
    ) -> requests.Response:
        if event_id:
            self._path = f"{self._path}/{event_id}"
        return self._get(**kwargs)

    def get_participants(
        self,
        event_id: str,
        **kwargs,
    ) -> list:
        """This uses the event.get() to get the events and then returns just the "students" list from the return."""
        result = self.get(
            event_id=event_id,
            **kwargs,
        )
        return result.json().get(
            "students",
            [],
        )

    def update_participant(
        self,
        event_id: str,
        participant_id: str,
        payload: dict,
        **kwargs,
    ) -> requests.Response:
        self._path = f"{self._path}/{event_id}/event_participants/{participant_id}"
        return self._patch(
            json=payload,
            **kwargs,
        )
