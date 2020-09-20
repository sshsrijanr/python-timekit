import requests
from timekit.components.base import *
__all__ = ["App"]


class App(APIBaseMethod):
    def __init__(self, app_token):
        APIBaseMethod.__init__(self, app_token)
        self.url = "{}/app".format(self.url)

    def get(self) -> Response:
        request_url = "{}".format(self.url)
        response = requests.get(request_url,
                                headers=self.headers,
                                auth=self.auth)
        return handle_response(response)

    def invite(self, data) -> Response:
        request_url = "{}/invite".format(self.url)
        response = requests.post(request_url,
                                 json=data,
                                 headers=self.headers,
                                 auth=self.auth)
        return handle_response(response)
