import requests     # type: ignore
from typing import Optional, Mapping, Union


class RequestManager:
    """
    The RequestManager class is used to send HTTP GET requests to URLs and receive the response.

    Attributes:

    Methods:
    - request_page(link: str):
        sends an HTTP GET request to a given URL and returns the response if the request is
        successful. If the request fails, an exception is raised. The method has one parameter, link, which is the URL
        to send the request to. The method includes a user-agent in the request headers to mimic browser activity, and
        has a timeout of 10 seconds for the request.
    """

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def request_page(endpoint: str,
                     headers: Optional[Mapping[str, Union[str, bytes]]],
                     params: Optional[dict] = None,
                     timeout: int = 10):
        """
        The request_page method sends an HTTP GET request to a given URL and returns the response if the request is
        successful. A user-agent is included in the request headers to mimic browser activity. The method has one
        parameter, link, which is the URL to send the request to. If the request is successful (status code 200),
        the response object is returned. If the request fails, an exception is raised. The method has a timeout of 10
        seconds for the request.

        Parameters:
            endpoint: str - url to make the request
            headers: str - headers to use in the request
            params:
            timeout: int - time to wait before request timeout

        Returns:
            None
        """

        # Using a user-agent to mimic browser activity
        req = requests.get(
            url=endpoint,
            headers=headers if headers else None,
            params=params if params else None,
            timeout=timeout,
        )

        if req.status_code == 200:
            return req
