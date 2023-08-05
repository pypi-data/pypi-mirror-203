from typing import Optional
from loguru import logger       # type: ignore
import requests     # type: ignore
import json

from common.exceptions import SubredditNotFoundException, UserNotFoundException     # type: ignore
from common.logging.logging_setup import LoggingSetup   # type: ignore
from common.constants import ConstantsNamespace     # type: ignore
from common.exceptions import TokenErrorException   # type: ignore
from core.api.reddit_api import RedditApi


class RedditApiValidations:
    """
    A class that provides a number of methods to expose the reddit API


    Attributes:

    Methods:
        - def validate_subreddits_list(self, subreddits):
            Validates a list of subreddits
        - def validate_subreddit(self, subreddit):
            Validates if a subreddit exists
        - def check_if_subreddit_exists(self, token: str, subreddit: str) -> Optional[bool]:
            Checks if the given username exists on Reddit API.
        - def validate_reddit_user(self, reddit_user: str, verbose: bool) -> Optional[bool]:
            Checks if the given username exists on Reddit API.
        - def validate_user(self, token: str, reddit_user: str) -> Optional[bool]:
            Checks if the given username exists on Reddit API.
        - def validate_user_v2(self, reddit_user: str) -> Optional[bool]:
            Checks if the given username exists on Reddit API.
    """


    def __init__(self):
        self.logging_setup = LoggingSetup()
        self.main_constants = ConstantsNamespace()
        self.reddit_api = RedditApi(self.main_constants.client_id, self.main_constants.secret_token,
                                    self.main_constants.username, self.main_constants.password)

    def validate_subreddits_list(self, subreddits):
        """
        Validates a list of subreddits
        Args:
            subreddits:

        Returns:

        """
        logger.debug("[4] VALIDATE SUBREDDITS STEP")

        for sub_red in subreddits:
            if self.validate_subreddit(sub_red) is False:
                message = "The provided subreddit {} was not found. Please provide a valid one".format(sub_red)
                raise SubredditNotFoundException(message)

    def validate_subreddit(self, subreddit):
        """
        Validates if a subreddit exists
        Args:
            subreddit:

        Returns:

        """
        url = "https://www.reddit.com/r/{}.json".format(subreddit)
        response = requests.get(url, headers=self.main_constants.user_agent)
        is_valid = None
        if response.status_code == 200:
            try:
                data = response.json()
                if len(data["data"]["children"]) > 0:
                    msg = "SUBREDDIT {}: {}".format(subreddit, self.main_constants.check_mark_symbol)
                    logger.debug(msg)
                    is_valid = True
            except ValueError:
                pass
        else:
            msg = "SUBREDDIT {}: {}".format(subreddit, self.main_constants.cross_symbol)
            logger.debug(msg)
            is_valid = False
        return is_valid

    def check_if_subreddit_exists(self, token: str, subreddit: str) -> Optional[bool]:
        """
        Checks if the given subreddit exists on Reddit API.

        Args:
            token (str): The OAuth token for Reddit API.
            subreddit (str): The name of the subreddit to check.

        Returns:
            bool: True if the subreddit exists, False otherwise.

        Notes:
            According to Reddit's API rules changed the client's User-Agent string to something unique and descriptive,
            including the target platform, a unique application identifier, a version string, and your username
            as contact information, in the following format
        """

        # add authorization to our headers dictionary
        headers = self.reddit_api.generate_headers(token)
        url = "https://oauth.reddit.com/r/{}/about".format(subreddit)
        res = requests.get(url, headers=headers)
        exists = None
        if res.status_code == 200:
            res_dict = json.loads(res.text)
            res_data = res_dict["data"]

            if res_data.get("url") is not None:
                logger.debug(
                    "SUBREDDIT {}: {}".format(subreddit, self.main_constants.check_mark_symbol))
                exists = True
            else:
                logger.debug(
                    "SUBREDDIT {}: {}".format(subreddit, self.main_constants.cross_symbol))
                exists = False
        return exists

    def validate_reddit_user(self, reddit_user: str, verbose: bool) -> Optional[bool]:
        """
        Checks if the given username exists on Reddit API.

        Args:
            reddit_user (str): The name of the user to check.
            verbose (bool): If True, logs the result of the check to the console.

        Returns:
            bool: True if the user exists, False otherwise.

        Notes:
            According to Reddit's API rules changed the client's User-Agent string to something unique and descriptive,
            including the target platform, a unique application identifier, a version string, and your username
            as contact information, in the following format

            This validation can also be accomplished by targeting this endpoints:
                url = "{constants.reddit_api_base_url}/api/v1/user/{username}/trophies"
                url: str = "https://www.reddit.com/user/{reddit_user}/about.json"
        """

        is_valid = False

        token = self.reddit_api.generate_reddit_api_token(verbose)

        # add authorization to our headers dictionary
        headers: dict[str, str] = self.reddit_api.generate_headers(token)

        url: str = "{}/api/username_available?user={}".format(self.main_constants.reddit_api_base_url, reddit_user)

        logger.debug("REQUESTING URL: {}".format(url))
        res = requests.get(url, headers=headers)

        if res.status_code == 200:
            # If the enpoint returns False, it means the username isn't available and as such the user exists
            logger.debug("USER {} EXISTS: {}".format(reddit_user, self.main_constants.check_mark_symbol))
            is_valid = True

        logger.debug("STATUS_CODE: {}, IS_VALID: {}".format(res.status_code, is_valid))

        if res.status_code == 403:
            raise UserNotFoundException("Reddit User not Found")

        return is_valid

    def validate_user(self, token: str, reddit_user: str) -> Optional[bool]:
        """
        Checks if the given username exists on Reddit API.

        Args:
            token (str): The OAuth token for Reddit API.
            reddit_user (str): The name of the user to check.

        Returns:
            bool: True if the user exists, False otherwise.

        Notes:
            According to Reddit's API rules changed the client's User-Agent string to something unique and descriptive,
            including the target platform, a unique application identifier, a version string, and your username
            as contact information, in the following format

            this check can also be accomplished by targeting this endpoint:
                url = "{constants.reddit_api_base_url}/api/v1/user/{username}/trophies"
        """

        url: str = "{}/api/username_available?user={}".format(self.main_constants.reddit_api_base_url, reddit_user)

        # add authorization to our headers dictionary
        headers = self.reddit_api.generate_headers(token)

        res = requests.get(url, headers=headers)
        exists = None
        if res.status_code == 200:
            if res is False:
                # If the enpoint returns False, it means the username isn't available and as such the user exists
                msg = "USER {} EXISTS: {}".format(reddit_user, self.main_constants.check_mark_symbol)
                logger.debug(msg)
                exists = True
            else:
                msg = "USER {} DOESN'T EXISTS: {}".format(reddit_user, self.main_constants.cross_symbol)
                logger.debug(msg)
                exists = False
        return exists

    def validate_user_v2(self, reddit_user: str) -> Optional[bool]:
        """
        Checks if the given username exists on Reddit API.

        Args:
            reddit_user (str): The name of the user to check.

        Returns:
            bool: True if the user exists, False otherwise.
        """
        url: str = "https://www.reddit.com/user/{}/about.json".format(reddit_user)
        headers: dict[str, str] = {
            "User-Agent": "Mozilla/5.0:com.martimdlima.redscrappy:v0.0.1 (by /u/mdlima__)"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            logger.debug("USER EXISTS", True)
            # User exists
            exists = True
        else:
            logger.debug("USER DOESN'T EXIST", True)
            # User does not exist
            exists = False
        return exists
