import requests
from timekit.components.base import *
__all__ = ["Project"]


class Project(APIBaseMethod):
    def __init__(self, app_token):
        APIBaseMethod.__init__(self, app_token)
        self.url = "{}/projects".format(self.url)

    def add_resources(self, id, data) -> Response:
        response = requests.post("{}/{}/resources".format(self.url, id),
                                 json=data,
                                 headers=self.headers,
                                 auth=self.auth)
        return handle_response(response)

    def set_resources(self, id, data) -> Response:
        response = requests.put("{}/{}/resources".format(self.url, id),
                                json=data,
                                headers=self.headers,
                                auth=self.auth)
        return handle_response(response)

    def remove_resources(self, id, resource_id) -> Response:
        response = requests.delete("{}/{}/resources/{}".format(
            self.url, id, resource_id),
                                headers=self.headers,
                                auth=self.auth)
        return handle_response(response)

    def get_resources(self, id) -> Response:
        response = requests.get("{}/{}/resources".format(self.url, id),
                                headers=self.headers,
                                auth=self.auth)
        return handle_response(response)
