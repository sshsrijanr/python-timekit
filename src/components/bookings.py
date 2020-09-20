import requests
from components.base import *
__all__ = ["Booking"]


class Group(APIBaseMethod):
    def __init__(self, app_token):
        APIBaseMethod.__init__(self, app_token)
        self.url = "{}/bookings/groups".format(self.url)

    def list(self, limit=1000, page=1, search=None) -> Response:
        request_url = "{}?limit={}&page={}&search={}".format(
            self.url, limit, page, search)
        response = requests.get(request_url,
                                auth=self.auth,
                                headers=self.headers)
        return handle_response(response)

    def retrieve(self, booking_id) -> Response:
        request_url = "{}/{}".format(self.url, booking_id)
        response = requests.get(request_url,
                                auth=self.auth,
                                headers=self.headers)
        return handle_response(response)


class Booking(APIBaseMethod):
    def __init__(self, app_token):
        APIBaseMethod.__init__(self, app_token)
        self.url = "{}/bookings".format(self.url)
        self.groups = Group(app_token)

    def create(self, data, dynamic_includes=[]) -> Response:
        includes = ""
        if dynamic_includes != [] and type(dynamic_includes) is list:
            includes = ",".join(dynamic_includes)
        request_url = "{}?include={}".format(self.url, includes)
        response = requests.post(request_url,
                                 json=data,
                                 headers=self.headers,
                                 auth=self.auth)
        return handle_response(response)

    def list(self,
             limit=1000,
             page=1,
             dynamic_includes=[],
             search=None,
             order_by=None,
             sorted_by=None) -> Response:
        includes = ""
        if dynamic_includes != [] and type(dynamic_includes) is list:
            includes = ",".join(dynamic_includes)
        request_url = "{}?limit={}&page={}include={}".format(
            self.url, limit, page, includes)
        if search:
            request_url = '{}&search={}'.format(request_url, search)
        if order_by:
            request_url = '{}&orderBy={}'.format(request_url, order_by)
        if sorted_by:
            request_url = '{}&sortedBy={}'.format(request_url, sorted_by)
        response = requests.get(request_url,
                                json=None,
                                headers=self.headers,
                                auth=self.auth)
        return handle_response(response)

    def confirm(self, booking_id) -> Response:
        response = requests.put("{}/{}/confirm".format(self.url, booking_id),
                                auth=self.auth,
                                headers=self.headers)
        return handle_response(response)

    def decline(self, booking_id, data) -> Response:
        response = requests.put("{}/{}/decline".format(self.url, booking_id),
                                auth=self.auth,
                                headers=self.headers)
        return handle_response(response)

    def cancel(self, booking_id, data) -> Response:
        response = requests.put("{}/{}/cancel".format(self.url, booking_id),
                                auth=self.auth,
                                headers=self.headers)
        return handle_response(response)

    def cancel_by_owner(self, booking_id, data) -> Response:
        response = requests.put("{}/{}/cancel_by_owner".format(
            self.url, booking_id),
                                json=data,
                                auth=self.auth,
                                headers=self.headers)
        return handle_response(response)

    def update_meta(self, booking_id, data) -> Response:
        response = requests.put("{}/{}".format(self.url, booking_id),
                                json=data,
                                auth=self.auth,
                                headers=self.headers)
        return handle_response(response)

    def create_in_bulk(self, data) -> Response:
        response = requests.post("{}".format(self.url),
                                 json=data,
                                 auth=self.auth,
                                 headers=self.headers)
        return handle_response(response)

    def update_in_bulk(self, data) -> Response:
        response = requests.put("{}".format(self.url),
                                json=data,
                                auth=self.auth,
                                headers=self.headers)
        return handle_response(response)