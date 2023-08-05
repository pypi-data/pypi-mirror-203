import glob
from pathlib import Path
from typing import Any, Optional, List
from loguru import logger  # type: ignore
from bs4 import ResultSet

from common.image_downloader import ImageDownloader  # type: ignore
from common.io_operations import IOOperations  # type: ignore
from common.logging.loguru_setup import LoggingSetup  # type: ignore
from common.logging.logging_constants import LoggingConstantsNamespace  # type: ignore
from common.constants import ConstantsNamespace  # type: ignore
from common.validations.parameter_validations import ParameterValidations  # type: ignore
from common.validations.reddit_api_validations import RedditApiValidations
from core.api.reddit_api import RedditApi  # type: ignore
from core.scrapper.thread_scrapper import ThreadScrapper  # type: ignore
from core.scrapper.scraper_helper import ScraperHelper

parameter_validations = ParameterValidations()
image_downloader = ImageDownloader()
io_operations = IOOperations()
log_constants = LoggingConstantsNamespace()
main_constants = ConstantsNamespace()
reddit_api = RedditApi(
    main_constants.client_id,
    main_constants.secret_token,
    main_constants.username,
    main_constants.password,
)
thread_scraper = ThreadScrapper()
reddit_api_validations = RedditApiValidations()
scraper_helper = ScraperHelper()


class MainHelper:
    """
    A class that provides helper functions for the main application.

    Attributes:

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

    def export_threads_detailed_information(self,
                                            user_or_subreddit: str,
                                            export_mode: str,
                                            threads_list: dict[str, dict[str, dict[str, Any] | ResultSet | Any] | Any],
                                            verbose: bool) -> None:
        """Write all the img urls to a json file, sorted by subreddit and post.

        Args:
            user_or_subreddit (str): The name of the user or subreddit to export data for.
            export_mode (str): The export mode, which can be "single", "multiple", or "user".
            threads_list (List[dict]): A list of dictionaries containing thread information.
            verbose (bool): Whether to print verbose output.

        Returns:
            None
        """

        detailed_report = ""

        match export_mode:
            case "single":
                detailed_report = "./reports/subreddits/{}_{}_summary.{}".format(
                    main_constants.current_date, user_or_subreddit, "json")
            case "multiple":
                detailed_report = "./reports/subreddits/{}_{}_summary.{}".format(
                    main_constants.current_date, user_or_subreddit, "json")
            case "user":
                detailed_report = "./reports/users/{}_{}_summary.{}".format(
                    main_constants.current_date, user_or_subreddit, "json")

        io_operations.write_detailed_post_information(
            threads_list, "w", detailed_report, verbose)

    def scrape_user(self, reddit_user: str, sort: str, number_results: int, verbose: bool) -> None:
        """
        Scrape a Reddit user's submissions, download the images, and export detailed thread information.

        Args:
            reddit_user (str): The name of the Reddit user to scrape.
            sort:  (str): The type of posts to be scraped: hot, new, top
            verbose (bool): Whether to print verbose output.
            number_results (int): The number of results to scrape.

        Returns:
            None
        """
        # validate reddit user
        is_user_valid = reddit_api_validations.validate_reddit_user(reddit_user, verbose)

        if is_user_valid:
            # Scrape user submissions
            user_threads = thread_scraper.scrape_threads(reddit_user, sort, "user", verbose, number_results)

            # Downloads scraped img urls
            image_downloader.download_img_url_list(
                reddit_user, user_threads, main_constants.user_directory, "user", verbose)

            img_output_dir = Path("./{}/{}".format(main_constants.user_directory, reddit_user))

            image_files = scraper_helper.generate_list_of_img_files_in_dir(img_output_dir)

            # If the image list size is bigger than 0, sort the downloaded images by mime type and resolution
            if len(image_files) > 0:
                io_operations.sort_by_mime_type_and_resolution(
                    img_output_dir,
                    img_output_dir,
                    True,
                    verbose,
                )

            self.export_threads_detailed_information(reddit_user, "user", user_threads, verbose)

        logger.info("Finished scraping threads for subreddits: {}".format(reddit_user)) if verbose else None

    def scrape_subreddit(self, subreddits: Optional[List[str]], sorting_type: str, number_results: Optional[int],
                         details: bool, verbose: bool) -> None:
        """
        Scrape posts and comments from a subreddit.

        Args:
            subreddits (List[str], optional): A list of subreddits to scrape. If None, the user's subreddits will
                    be used.
            sorting_type (str): A string indicating how to sort the posts. Valid values: 'hot', 'new', 'top',
                'controversial', 'rising'.
            number_results (int, optional): The maximum number of posts to scrape. If None, all posts will be scraped.
            details (bool): If True, exports detailed information about each post to a JSON file.
            verbose (bool): If True, displays logging information during the scraping process.
        """

        user_subreddits_list = main_constants.user_subreddits_list

        if subreddits is None and user_subreddits_list is not None:
            subreddits = user_subreddits_list
        elif (subreddits is not None and user_subreddits_list is not None or subreddits is not None
              and user_subreddits_list is None):
            subreddits = subreddits

        # Validate Args
        subreddits = parameter_validations.validate_subreddits_parameter(subreddits)

        # Validate Subreddit
        reddit_api_validations.validate_subreddits_list(subreddits)

        subreddits_detailed_information_dict = {}

        # Scrape posts and comments
        for subreddit in subreddits:
            # Scrapes n number of threads for the given subreddits, according to provided parameter max_count
            subreddit_threads_list = thread_scraper.scrape_threads(
                subreddit, sorting_type, "subreddit", verbose, number_results if number_results is not None else None)

            subreddits_detailed_information_dict = {**subreddits_detailed_information_dict,
                                                    **subreddit_threads_list}

            img_output_dir = Path("./{}/{}".format(main_constants.subreddit_directory, subreddit))

            # Downloads scraped img urls
            image_downloader.download_img_url_list(
                subreddit, subreddit_threads_list, main_constants.subreddit_directory, "subreddit", verbose)

            image_files = glob.glob(str(img_output_dir) + "/*.jpg") + glob.glob(
                str(img_output_dir) + "/*.png") + glob.glob(
                str(img_output_dir) + "/*.gif")

            # If the image list size is bigger than 0, sort the downloaded images by mime type and resolution
            if len(image_files) > 0:
                io_operations.sort_by_mime_type_and_resolution(
                    img_output_dir,
                    img_output_dir,
                    True,
                    verbose,
                )

            # If the user wants to export all subreddit data to one file or multiple files, can pass the detail option
            if details:
                self.export_threads_detailed_information(subreddit, "single",
                                                         subreddit_threads_list, verbose)

        if not details:
            self.export_threads_detailed_information(' '.join(map(str, subreddits)).replace(" ", "_"), "multiple",
                                                     subreddits_detailed_information_dict, verbose)

        logger.info("Finished scraping threads for subreddits: {}".format(" ".join(map(str, subreddits)))) \
            if verbose else None
