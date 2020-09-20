import requests
from timekit.components.base import *
__all__ = ["Resource"]


class Resource(APIBaseMethod):
    def __init__(self, app_token):
        APIBaseMethod.__init__(self, app_token)
        self.url = "{}/resources".format(self.url)

    def retrieve(self, id, dynamic_includes=[]) -> Response:
        includes = ''
        if dynamic_includes != []:
            includes = ','.join(dynamic_includes)
        response = requests.get("{}/{}?include={}".format(
            self.url, id, includes),
                                json=None,
                                headers=self.headers,
                                auth=self.auth)
        return handle_response(response)

    def availability_constraints(self, id, data) -> Response:
        response = requests.put("{}/{}".format(self.url, id),
                                json=data,
                                headers=self.headers,
                                auth=self.auth)
        return handle_response(response)
