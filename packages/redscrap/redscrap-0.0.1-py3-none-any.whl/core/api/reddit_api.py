import logging
from typing import Optional, Dict, Union
from loguru import logger       # type: ignore
import requests     # type: ignore

from common.exceptions import SubredditNotFoundException, UserNotFoundException     # type: ignore
from common.logging.logging_setup import LoggingSetup   # type: ignore
from common.constants import ConstantsNamespace     # type: ignore
from common.exceptions import TokenErrorException   # type: ignore


class RedditApi:
    """
        A class that provides functions to access Reddit API.

    Attributes:

    Methods:
        def generate_headers(self, token: str) -> Dict[str, str]:
            Generates headers for a Reddit API request.
        def generate_reddit_api_token(self, verbose: bool = False) -> str:
             Generate a Reddit API token using the user's credentials.
        get_logged_user_profile(self, verbose: bool) -> Union[Dict, None]:
            Retrieve the logged-in user's profile information.
        def generate_params_for_reddit_api_req(
        self, after: Optional[str], before: Optional[str], count: Optional[int],
        limit: Optional[int], show: Optional[str], sr_detail: Optional[bool]
        ) -> Dict[str, str]:
            Generate a dictionary of parameters to be used in a Reddit API request.

    """
    def __init__(self, client_id, secret_token, username, password):
        self.logging_setup = LoggingSetup()
        self.main_constants = ConstantsNamespace()
        self.client_id = client_id
        self.secret_token = secret_token
        self.username = username
        self.password = password

    def generate_headers(self, token: str) -> Dict[str, str]:
        """
        Generates headers for a Reddit API request.

        Args:
            token (str): A Reddit API access token.

        Returns:
            Dict[str, str]: A dictionary of headers with authorization token added.
        """
        headers: dict[str, str] = {**self.main_constants.reddit_headers, **{"Authorization": "bearer {}".format(token)}}
        return headers

    # noinspection PyUnresolvedReferences
    def generate_reddit_api_token(self, verbose: bool = False) -> str:
        """Generate a Reddit API token using the user's credentials.

        Args:
            verbose (bool, optional): Whether to log additional debug information. Defaults to False.

        Raises:
            TokenErrorException: If the request to obtain the token fails.

        Returns:
            str: The generated Reddit API token.
        """

        auth = requests.auth.HTTPBasicAuth(self.client_id, self.secret_token)
        data = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password,
        }
        headers = self.main_constants.reddit_headers

        res = requests.post(
            "https://www.reddit.com/api/v1/access_token",
            auth=auth,
            data=data,
            headers=headers,
        )

        if not res.ok:
            if verbose:
                logger.exception("Request failed with code {}".format(res.status_code))
            raise TokenErrorException("Failed to obtain Reddit API token")

        token = res.json()["access_token"]
        msg = "Generated Reddit API token: {}".format(token)
        logger.exception(msg)
        return token

    def get_logged_user_profile(self, verbose: bool) -> Union[Dict, None]:
        """
        Retrieve the logged-in user's profile information.

        Args:
            verbose (bool): If True, prints the API request information and response.

        Returns:
            Union[Dict, None]: Returns a dictionary of the user profile information if successful,
            otherwise returns None.

        Raises:
            UserNotFoundException: If the user profile is unavailable or could not be reached.
        """
        # Generating the URL leading to the desired subreddit
        url = "https://oauth.reddit.com/api/v1/me"
        token = self.generate_reddit_api_token(verbose)
        headers = {**self.main_constants.reddit_headers, **{"Authorization": "bearer {}".format(token)}}

        response = None

        try:
            res = requests.get(url, headers=headers)

            if res.ok:
                response = res.json()

        except UserNotFoundException as exc:
            msg = (
                "Your user profile is unavailable or couldn't be reached at this moment"
            )
            logging.exception(msg)
            raise UserNotFoundException(msg) from exc

        return response

    def generate_params_for_reddit_api_req(
        self, after: Optional[str], before: Optional[str], count: Optional[int],
        limit: Optional[int], show: Optional[str], sr_detail: Optional[bool]
    ) -> Dict[str, str]:
        """
        Generate a dictionary of parameters to be used in a Reddit API request.

        Args:
            after (str or None): The fullname of the post to start after.
            before (str or None): The fullname of the post to start before.
            count (int or None): The number of items in the listing to skip.
            limit (int or None): The maximum number of items to return.
            show (str or None): The types of items to show.
            sr_detail (bool or None): Whether to return details about the subreddit.

        Returns:
            A dictionary containing the specified parameters for a Reddit API request.
        """
        params = {
            "after": after if after is not None else "",
            "before": before if before is not None else "",
            "count": count if count is not None else "",
            "limit": limit if limit is not None else "",
            "show": show if show is not None else "",
            "sr_detail": sr_detail if sr_detail is not None else "",
        }

        return params
