import requests
from timekit.components.base import *
__all__ = ["Availability"]


class Availability(APIBaseMethod):
    def __init__(self, app_token):
        APIBaseMethod.__init__(self, app_token)
        self.url = "{}/availability".format(self.url)

    def list(self, data) -> Response:
        request_url = "{}".format(self.url)
        response = requests.post(request_url,
                                json=data,
                                headers=self.headers,
                                auth=self.auth)
        return handle_response(response)

