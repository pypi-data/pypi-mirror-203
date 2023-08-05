import datetime
from collections import defaultdict
from pathlib import Path
import os


class ConstantsNamespace:
    """A class that contains constants used throughout the application.

    Attributes:
        old_reddit_url (str): Old reddit base url.
        reddit_api_base_url (str): Reddit API base url.
        resolutions (defaultdict): Resolutions for the most popular resolutions.
        default_logger_format (str): Default logger format.
        default_logger_date_format (str): Default logger date format.
        attrs (dict): Default attributes for scraping reddit posts.
        possible_urls (list): Valid possible url prefixes that may appear during scraping.
        invalid_urls (list): Invalid possible url prefixes that may appear during scraping.
        match_url (str): Regex that match urls in the format https://subdomain.domain.
        domain_regex (str): Regex for validating domains.
    """

    @property
    def client_id(self):
        """
        Returns: str - User API KEY

        """
        return os.environ.get("REDDIT_API_KEY")

    @property
    def secret_token(self):
        """
        Returns: str - User API secret

        """
        return os.environ.get("REDDIT_API_SECRET")

    @property
    def username(self):
        """
        Returns: str - User reddit username

        """
        return os.environ.get("REDDIT_USERNAME")

    @property
    def password(self):
        """
        Returns: str - User reddit password

        """
        return os.environ.get("REDDIT_PASSWORD")

    @property
    def user_subreddits_list(self):
        """
        Returns: str - subreddit user list. A string of comma separated subreddits

        """
        return os.environ.get("SUBREDDIT_USER_LIST")

    @property
    def user_subreddits_sort_method(self):
        """
        Returns: str - subreddit user list. A string of comma separated subreddits

        """
        return os.environ.get("SUBREDDIT_SORT_METHOD")

    @property
    def subreddit_directory(self):
        return "output/subreddit"

    @property
    def user_directory(self):
        return "output/user"

    @property
    def reddit_headers(self):
        """
        Sets up the header info, which gives reddit a brief description of the app
        @return:
        """
        return {
            "User-Agent": "Mozilla/5.0:com.martimdlima.redscrappy:v0.0.1 (by /u/mdlima__)"
        }

    @property
    def check_mark_symbol(self):
        """
        Returns: str - check mark symbol

        """
        return "\N{CHECK MARK}"

    @property
    def cross_symbol(self):
        """
        Returns: str - cross symbol

        """
        return "\N{BALLOT X}"

    @property
    def reddit_url(self):
        """
         New reddit base url
        """
        return "https://www.reddit.com"

    @property
    def old_reddit_url(self):
        """
        Old reddit base url
        """
        return "https://old.reddit.com"

    @property
    def reddit_api_base_url(self):
        """
        reddit API base url
        """
        return "https://oauth.reddit.com"

    @property
    def output_path(self):
        return Path("./subreddit/")

    @property
    def resolutions(self):
        """
        Resolutions for the most popular resolutions
        """
        return defaultdict(
            lambda: "other",
            {
                (0, 0, 1280, 720): "720p",
                (1281, 721, 1920, 1080): "1080p",
                (1921, 1081, 2560, 1440): "1440p",
                (2561, 1441, 3840, 2160): "2160p",
                (3841, 2161, 7680, 4320): "4k",
                (7681, 4321, float("inf"), float("inf")): "8k",
            },
        )

    @property
    def user_agent(self):
        return {"User-Agent": "Mozilla/5.0"}

    @property
    def attrs(self):
        """
        Default attrs for scrapping reddit posts
        """
        return {"class": "thing"}

    @property
    def possible_urls(self):
        """
        Valid possible url prefixes that may appear during scraping
        """
        return [
            "ze-robot.com/dl/",
            "preview.redd.it",
            "i.redd.it/",
            "static.greatbigcanvas.com",
            "external-preview.redd.it/"
            #"https://preview.redd.it/",
            #"https://ze-robot.com",
            #"https://i.redd.it/",
            #"https://old.reddit.com/r/",
            #"https://static.greatbigcanvas.com",
            #"https://external-preview.redd.it/"
        ]

    @property
    def invalid_url_prefixes(self):
        """
        Invalid possible url prefixes that may appear during scraping
        """
        return [
            "/u/ze-robot/",
            "https://ze-robot.com/#faq",
            "https://www.wallpaperflare.com/",
            "https://www.reddit.com/message/compose/",
            "https://old.reddit.com/user",
        ]

    @property
    def match_url(self):
        """
        Regex that match urls in the format https://subdomain.domain
        """
        reg = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+/[-\w./?%&=]*"
        return reg

    @property
    def domain_regex(self):
        """
        Regex for validating domains
        The first regular expression uses a positive lookahead to assert that the string contains between 1 and 254
        characters ((?=^.{1,254}$)). Then it uses a capturing group to match one or more repetitions of a subpattern
        that consists of one or more characters that are not a digit followed by an optional dot.
        Finally, it uses a non-capturing group to match two or more
        alphabetical characters ((?:[a-zA-Z]{2,})$). In summary, this regex matches a string that consists of one
        or more non-digit characters followed by an optional dot, and ends with two or more alphabetical
        characters. This would match a domain name such as "example.com".

        The second regular expression is a simplified version of the first one, and it only matches domain names
        that consist of one or more subdomains separated by dots, followed by a top-level domain.
        The regex starts by using a capturing group to match one or more repetitions of a subpattern that consists
         of a letter or digit ([a-zA-Z0-9]), followed by an optional subpattern that consists of between 0 and 61
         characters that are either a letter, digit, or a hyphen (([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?),
         followed by a dot. This pattern is repeated one or more times, followed by a subpattern that matches
        two or more alphabetical characters ([a-zA-Z]{2,}). In summary, this regex matches a string that consists
        of one or more subdomains separated by dots, followed by a top-level domain. This would match a domain
        name such as "sub.example.com".
        """
        # reg"(?=^.{1,254}$)(^(?:(?!\d+\.)[a-zA-Z0-9_\-]{1,63}\.?)+(?:[a-zA-Z]{2,})$)"
        reg = r"^([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$"
        return reg

    @property
    def path_regex(self):
        """
        Regex for validating paths
        """
        return r"^\/[\/\.a-zA-Z0-9\-]+$"

    @property
    def path_regex_with_query_params(self):
        """
        Regex for validating paths with query params
        """
        reg = r"^(\/\w+)+(\.)?\w+(\?(\w+=[\w\d]+(&\w+=[\w\d]+)*)+){0,1}$"
        return reg

    @property
    def validate_and_split_string_regex(self):
        """
        validate if a string is composed of values separated by commas or semicolons and only contains plus signs,
        underscores, and alphanumeric characters
        """
        # pattern = r'[^\w\s,;]+'
        # pattern = r"^[a-zA-Z0-9+\s]*([,;][a-zA-Z0-9+\s]*)*$"
        # pattern = ^[a-zA-Z0-9+\s]*([,;][a-zA-Z0-9+\s]*)*$

        # Check if the string contains any special characters besides commas and semicolons
        pattern = r"^[a-zA-Z0-9+_]*([,;][a-zA-Z0-9+_]*)*$"
        return pattern

    @property
    def extract_num_children(self):
        pattern = r"\d+\.\d+|\d+"
        return pattern

    @property
    def current_date(self):
        now = datetime.datetime.now()
        formatted_date = now.strftime("%d_%m_%Y_%H_%M_%S")
        return formatted_date
