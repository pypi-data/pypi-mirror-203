import glob
from pathlib import Path
from typing import Any, Optional, List, Iterable
from loguru import logger  # type: ignore
from bs4 import ResultSet

from common.image_downloader import ImageDownloader  # type: ignore
from common.io_operations import IOOperations  # type: ignore
from common.logging.loguru_setup import LoguruSetup  # type: ignore
from common.logging.logging_constants import LoggingConstants  # type: ignore
from common.common_constants import CommonConstants  # type: ignore
from common.validations.parameter_validations import ParameterValidations  # type: ignore
from common.validations.reddit_api_validations import RedditApiValidations  # type: ignore
from core.api.reddit_api import RedditApi  # type: ignore
from core.scraper.thread_scraper import ThreadScraper  # type: ignore
from core.scraper.scraper_helper import ScraperHelper   # type: ignore


class MainHelper:
    """
    A class that provides helper functions for the main application.

    Methods:
        export_threads_detailed_information(user_or_subreddit: str, export_mode: str,
            threads_list: dict[str, dict[str, dict[str, Any] | ResultSet | Any] | Any], verbose: bool) -> None:
            Writes all the image URLs to a JSON file, sorted by subreddit and post.

        scrape_user(reddit_user: str, verbose: bool, number_results: int) -> None:
            Scrapes a Reddit user's submissions, downloads the images, and exports detailed thread information.

        scrape_subreddit(subreddits: Optional[List[str]], sorting_type: str, number_results: Optional[int],
            details: bool, verbose: bool) -> None:
            Scrapes posts and comments from a subreddit.

    """

    def __init__(self) -> None:
        super().__init__()
        self.parameter_validations = ParameterValidations()
        self.image_downloader = ImageDownloader()
        self.io_operations = IOOperations()
        self.log_constants = LoggingConstants()
        self.main_constants = CommonConstants()
        self.reddit_api = RedditApi(
            self.main_constants.client_id,
            self.main_constants.secret_token,
            self.main_constants.username,
            self.main_constants.password,
        )
        self.thread_scraper = ThreadScraper()
        self.reddit_api_validations = RedditApiValidations()
        self.scraper_helper = ScraperHelper()

    def export_threads_detailed_information(self,
                                            user_or_subreddit: str,
                                            export_mode: str,
                                            threads_list: dict[str, dict[str, dict[str, Any] | ResultSet | Any] | Any],
                                            output_directory: str,
                                            verbose: Optional[bool]) -> None:
        """Write all the img urls to a json file, sorted by subreddit and post.

        Args:
            output_directory (str): Directory to output thread detailed information
            user_or_subreddit (str): The name of the user or subreddit to export data for.
            export_mode (str): The export mode, which can be "single", "multiple", or "user".
            threads_list (List[dict]): A list of dictionaries containing thread information.
            verbose (Optional[bool]): Whether to print verbose output.
        """

        detailed_report = ""

        match export_mode:
            case "single":
                detailed_report = "{}/reports/subreddits/{}_{}_summary.{}".format(
                    output_directory, self.main_constants.current_date, user_or_subreddit, "json")
            case "multiple":
                detailed_report = "{}/reports/subreddits/{}_{}_summary.{}".format(
                    output_directory, self.main_constants.current_date, user_or_subreddit, "json")
            case "user":
                detailed_report = "{}/reports/users/{}_{}_summary.{}".format(
                    output_directory, self.main_constants.current_date, user_or_subreddit, "json")

        self.io_operations.write_detailed_post_information(
            threads_list, "w", detailed_report, verbose)

    def scrape_user(self, reddit_user: str, sort: str, number_results: int, output_directory: str,
                    verbose: Optional[bool]) -> None:
        """
        Scrape a Reddit user's submissions, download the images, and export detailed thread information.

        Args:
            reddit_user (str): The name of the Reddit user to scrape.
            sort:  (str): The type of posts to be scraped: hot, new, top
            verbose (Optional[bool]): Whether to print verbose output.
            output_directory: (str): Directory to output the downloaded files and reports
            number_results (int): The number of results to scrape.

        Returns:
            None
        """
        # validate reddit user
        is_user_valid = self.reddit_api_validations.validate_reddit_user(reddit_user, verbose)

        if is_user_valid:
            # Scrape user submissions
            user_threads = self.thread_scraper.scrape_threads(reddit_user, sort, "user", verbose, number_results)

            # Downloads scraped img urls
            self.image_downloader.download_img_url_list(
                reddit_user, user_threads, "user", output_directory, verbose)

            img_output_dir = Path("{}/downloads/user/{}".format(output_directory, reddit_user))

            image_files = self.scraper_helper.generate_list_of_img_files_in_dir(img_output_dir)

            # If the image list size is bigger than 0, sort the downloaded images by mime type and resolution
            if len(image_files) > 0:
                self.io_operations.sort_by_mime_type_and_resolution(
                    img_output_dir,
                    img_output_dir,
                    True,
                    verbose,
                )

            self.export_threads_detailed_information(reddit_user, "user", user_threads, output_directory, verbose)

        logger.info("Finished scraping threads for subreddits: {}".format(reddit_user)) if verbose else None

    def scrape_subreddit(self, subreddits: Iterable[str], sorting_type: str, number_results: Optional[int],
                         details: bool, output_directory: str, verbose: bool) -> None:
        """
        Scrape posts and comments from a subreddit.

        Args:

            subreddits (List[str], optional): A list of subreddits to scrape. If None, the user's subreddits will
                    be used.
            sorting_type (str): A string indicating how to sort the posts. Valid values: 'hot', 'new', 'top',
                'controversial', 'rising'.
            number_results (int, optional): The maximum number of posts to scrape. If None, all posts will be scraped.
            details (bool): If True, exports detailed information about each post to a JSON file.
            output_directory: (str): Directory to output the downloaded files and reports
            verbose (bool): If True, displays logging information during the scraping process.
        """

        user_subreddits_list = self.main_constants.user_subreddits_list

        if subreddits is None and user_subreddits_list is not None:
            subreddits = user_subreddits_list
        elif (subreddits is not None and user_subreddits_list is not None or subreddits is not None
              and user_subreddits_list is None):
            subreddits = subreddits

        # Validate Args
        subreddits = self.parameter_validations.validate_subreddits_parameter(subreddits)

        # Validate Subreddit
        self.reddit_api_validations.validate_subreddits_list(subreddits)

        subreddits_detailed_information_dict: dict = {}

        # Scrape posts and comments
        for subreddit in subreddits:
            # Scrapes n number of threads for the given subreddits, according to provided parameter max_count
            subreddit_threads_list = self.thread_scraper.scrape_threads(
                subreddit, sorting_type, "subreddit", verbose, number_results if number_results is not None else None)

            subreddits_detailed_information_dict = {**subreddits_detailed_information_dict,
                                                    **subreddit_threads_list}

            img_output_dir = Path("{}/downloads/subreddit/{}".format(output_directory, subreddit))

            # Downloads scraped img urls
            self.image_downloader.download_img_url_list(
                subreddit, subreddit_threads_list, "subreddit", output_directory, verbose)

            image_files = glob.glob(str(img_output_dir) + "/*.jpg") + glob.glob(
                str(img_output_dir) + "/*.png") + glob.glob(
                str(img_output_dir) + "/*.gif")

            # If the image list size is bigger than 0, sort the downloaded images by mime type and resolution
            if len(image_files) > 0:
                self.io_operations.sort_by_mime_type_and_resolution(
                    img_output_dir,
                    img_output_dir,
                    True,
                    verbose,
                )

            # If the user wants to export all subreddit data to one file or multiple files, can pass the detail option
            if details:
                self.export_threads_detailed_information(subreddit, "single",
                                                         subreddit_threads_list, output_directory, verbose)

        if not details:
            self.export_threads_detailed_information(' '.join(map(str, subreddits)).replace(" ", "_"), "multiple",
                                                     subreddits_detailed_information_dict, output_directory, verbose)

        logger.info("Finished scraping threads for subreddits: {}".format(" ".join(map(str, subreddits)))) \
            if verbose else None
