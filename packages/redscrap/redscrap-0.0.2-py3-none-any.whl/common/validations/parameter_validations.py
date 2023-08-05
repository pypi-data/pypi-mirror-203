from typing import List, Optional
from loguru import logger        # type: ignore
import re
import requests      # type: ignore

from common.exceptions import SubredditNotFoundException         # type: ignore
from common.logging.logging_setup import LoggingSetup        # type: ignore
from common.common_constants import CommonConstants      # type: ignore
from common.logging.utils.loguru_wrappers import logger_wraps        # type: ignore
from core.api.reddit_api import RedditApi        # type: ignore


class ParameterValidations:
    """
        A class that provides method to validate the application parameters

        Methods:
            def validate_subreddits_parameter(self, input_str: str) -> list[str]:
                Validates that input string only contains commas and semicolons, and splits it into a list of values
                separated by those characters. Returns the list of values.

            def validate_user(self, token: str, reddit_user: str) -> Optional[bool]:
                Checks if the given username exists on Reddit API.

            def validate_user_v2(self, reddit_user: str) -> Optional[bool]:
                Checks if the given username exists on Reddit API.

    """

    def __init__(self) -> None:
        super().__init__()
        self.logging_setup = LoggingSetup()
        self.main_constants = CommonConstants()
        self.reddit_api = RedditApi(self.main_constants.client_id, self.main_constants.secret_token,
                                    self.main_constants.username, self.main_constants.password)

    @logger_wraps()
    def validate_subreddits_parameter(self, input_str: str) -> list[str]:
        """
        Validates that input string only contains commas and semicolons, and splits it into a list of values separated
        by those characters. Returns the list of values.

        Args:
            input_str (str): The string to be validated and split.

        Returns:
            list or str: If the input string contains only alphanumeric characters, it returns the input string.
                Otherwise, it returns a list of strings that are split by the special character present in the
                input string.

        Raises:
            ValueError: If the input string contains special characters other than commas and semicolons, or
                if the input string contains both commas and semicolons.
        """
        logger.debug("[2] VALIDATING PARAMS SET")

        # Remove white spaces
        sanitized_string = input_str.replace(" ", "")

        # Replace consecutive commas or semicolons with a single comma
        sanitized_string = re.sub(r"[,;]+", ",", sanitized_string)

        # Remove any remaining empty groups
        sanitized_string = re.sub(r"(^,)|(,$)|(^;)|(;$)|,{2,}", "", sanitized_string)

        # Check if the string contains any special characters
        pattern = self.main_constants.validate_and_split_string_regex
        if bool(re.match(pattern, sanitized_string)) is False:
            raise ValueError(
                "Input string contains special characters other than commas and semicolons."
            )

        if "," in input_str and ";" in input_str:
            # The string cannot contain both commas and semicolons
            raise ValueError("Input string contains both commas and semicolons.")

        values: List[str] = []

        if "," in input_str:
            values = input_str.split(",")
        elif ";" in input_str:
            values = input_str.split(";")
        else:
            return [input_str]

        # Remove any leading or trailing whitespace from the values
        values = [value.strip() for value in values]

        # Remove any empty values from the list
        values = [value for value in values if value]

        return values

    @logger_wraps()
    def validate_user(self, token: str, reddit_user: str) -> Optional[bool]:
        """Checks if the given username exists on Reddit API.

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
        """Checks if the given username exists on Reddit API.

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
