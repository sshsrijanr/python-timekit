import requests
__all__ = ["APIBaseMethod", "Response", "handle_response"]

BASE_URL_V2 = "https://api.timekit.io/v2"


class Response:
    def __init__(self, data, status):
        self.data = data
        self.status = status


def handle_response(response):
    if response.status_code in range(200, 206):
        try:
            return Response(response.json(), response.status_code)
        except:
            return Response({}, response.status_code)
    else:
        try:
            return Response(response.json(), response.status_code)
        except:
            if response.status_code == 401:
                return Response({"error": "Invalid credentials supplied"},
                                response.status_code)
            elif response.status_code == 422:
                return Response(
                    {
                        "error":
                        "A POST data JSON key or alike is malformed or missing"
                    }, response.status_code)
            else:
                return Response({"error": "response is not json serializable"},
                                response.status_code)


class APIBaseMethod:
    def __init__(self, app_token):
        self.headers = {'Content-Type': 'application/json'}
        self.auth = requests.auth.HTTPBasicAuth('', app_token)
        self.url = BASE_URL_V2

    def list(self, limit=50, page=1, search="") -> Response:
        """
        limit: integer(1000 max),
        page: integer,
        search: string,
        Refer timekit API documentation for search
        https://developers.timekit.io/reference#getting-started
        """
        request_url = '{}?limit={}&page={}&search={}'.format(
            self.url, limit, page, search)
        response = requests.get(request_url,
                                json=None,
                                headers=self.headers,
                                auth=self.auth)
        return handle_response(response)

    def create(self, data) -> Response:
        """
        data: json object
        Refer timekit API documentation for json data structure
        https://developers.timekit.io/reference#getting-started
        """
        response = requests.post(self.url,
                                 json=data,
                                 headers=self.headers,
                                 auth=self.auth)
        return handle_response(response)

    def retrieve(self, id, data=None) -> Response:
        """
        id: string(id generated by timekit)
        """
        response = requests.get("{}/{}".format(self.url, id),
                                json=None,
                                headers=self.headers,
                                auth=self.auth)
        return handle_response(response)

    def update(self, id, data) -> Response:
        """
        id: string(id generated by timekit),
        data: json object
        Refer timekit API documentation for json data structure
        https://developers.timekit.io/reference#getting-started
        """
        response = requests.put("{}/{}".format(self.url, id),
                                json=data,
                                headers=self.headers,
                                auth=self.auth)
        return handle_response(response)

    def partial_update(self, id, data) -> Response:
        """
        id: string(id generated by timekit),
        data: json object
        Refer timekit API documentation for json data structure
        https://developers.timekit.io/reference#getting-started
        """
        response = requests.patch("{}/{}".format(self.url, id),
                                  json=data,
                                  headers=self.headers,
                                  auth=self.auth)
        return handle_response(response)

    def delete(self, id) -> Response:
        """
        id: string(id generated by timekit)
        """
        response = requests.delete("{}/{}".format(self.url, id),
                                   json=None,
                                   headers=self.headers,
                                   auth=self.auth)
        return handle_response(response)
