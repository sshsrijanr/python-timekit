import requests
from components.base import *
__all__ = ["Project"]


class Project(APIBaseMethod):
    def __init__(self, app_token):
        APIBaseMethod.__init__(self, app_token)
        self.url = "{}/projects".format(self.url)

    def list_all(self, limit=50) -> Response:
        response = requests.get("{}?limit={}".format(self.url, limit),
                                auth=self.auth,
                                headers=self.headers)
        return handle_response(response)

    def add_resources(self, project_id, data) -> Response:
        response = requests.post("{}/{}/resources".format(
            self.url, project_id),
                                 json=data,
                                 headers=self.headers,
                                 auth=self.auth)
        return handle_response(response)

    def set_resources(self, project_id, data) -> Response:
        response = requests.put("{}/{}/resources".format(self.url, project_id),
                                json=data,
                                headers=self.headers,
                                auth=self.auth)
        return handle_response(response)
