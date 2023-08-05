import logging
import time
from typing import Any, Optional, Dict, Union
import requests  # type: ignore
from loguru import logger  # type: ignore
from bs4 import BeautifulSoup, ResultSet

from common.exceptions import TokenErrorException  # type: ignore
from common.logging.logging_setup import LoggingSetup  # type: ignore
from common.constants import ConstantsNamespace  # type: ignore
from common.logging.utils.loguru_wrappers import logger_wraps  # type: ignore
from common.validations.url_validations import UrlValidations  # type: ignore
from common.request_manager import RequestManager  # type: ignore
from common.image_downloader import ImageDownloader  # type: ignore
from common.io_operations import IOOperations  # type: ignore
from core.scrapper.comment_scrapper import CommentScrapper  # type: ignore
from core.api.reddit_api import RedditApi  # type: ignore
from core.scrapper.scraper_helper import ScraperHelper  # type: ignore


class ThreadScrapper:
    """
    A class that provides methods to scrape threads from subreddits or users

    Attributes:

    Methods:
        - def scrape_threads(self, subreddit_or_user: str, sort: str, scrape_mode: str, verbose: bool,
            max_counter: Optional[int] = None ) -> Dict[str, Union[Dict[str, Union[Dict[str, Any], Dict[str, Any],
            ResultSet[Any], Dict[str, Any], Any]], Any]]:
            Scrape threads from a subreddit or user and return the results.
        - def scrape_single_thread(self, link: str, verbose: bool):
            Scrapes the given Reddit thread URL and returns a tuple containing a list of image URLs and a dictionary of
            comments.
    """

    def __init__(self) -> None:
        super().__init__()
        self.logging_funcs = LoggingSetup()
        self.constants = ConstantsNamespace()
        self.validations = UrlValidations()
        self.comment_scrapper = CommentScrapper()
        self.request_manager = RequestManager()
        self.io_operations = IOOperations()
        self.image_downloader = ImageDownloader()
        self.scraper_helper = ScraperHelper()
        self.reddit_api = RedditApi(self.constants.client_id, self.constants.secret_token, self.constants.username,
                                    self.constants.password)

    def scrape_threads(self, subreddit_or_user: str, sort: str, scrape_mode: str, verbose: bool,
                       max_counter: Optional[int] = None
                       ) -> Dict[
        str, Union[Dict[str, Union[Dict[str, Any], Dict[str, Any], ResultSet[Any], Dict[str, Any], Any]], Any]]:
        """
        Scrape threads from a subreddit or user and return the results.

        Args:
            subreddit_or_user (str): The name of the subreddit or user from which to scrape threads.
            sort (str): The method to sort the threads, such as "hot" or "top".
            scrape_mode (str): The mode in which to scrape threads, either "subreddit" or "user".
            verbose (bool): A flag indicating whether to log verbose output.
            max_counter (Optional[int], optional): The maximum number of threads to scrape. Defaults to None.

        Returns:
            Dict[str, Union[ Dict[str, Union[Dict[str, Any], Dict[str, Any], ResultSet[Any], Dict[str, Any], Any]],
                Any]]:
                A dictionary of thread URLs and their corresponding information, such as their author, datetime,
                 rating, URLs, and comments.
        """
        params: Optional[Dict[str, Any]] = None

        if scrape_mode == "subreddit":
            endpoint = "/r/{}/{}".format(subreddit_or_user, sort)
            url = "{}{}".format(self.constants.old_reddit_url, endpoint)
        else:
            # Generating the URL leading to the desired subreddit
            endpoint = "/user/{}/{}".format(subreddit_or_user, "submitted")
            url = "{}{}".format(self.constants.old_reddit_url, endpoint)
            params = self.reddit_api.generate_params_for_reddit_api_req(None, None, None, None, "all", None)

        req = self.request_manager.request_page(
            url,
            self.constants.user_agent,
            params if params is not None else None
        )

        threads_urls: Dict[
            str, Union[Dict[str, Union[Dict[str, Any], Dict[str, Any], ResultSet[Any], Dict[str, Any], Any]], Any]
        ] = {}  # noqa comments
        thread_img_urls = {}

        counter = 1
        full = False
        if req.status_code == 200:
            msg = "\nCollecting information for {}....".format(url)
            logger.info(msg) if verbose else None

            soup = BeautifulSoup(req.text, "html.parser")

            if scrape_mode == "subreddit":
                soup = BeautifulSoup(req.text, "html.parser")
                threads_list_element = soup.find(
                    "div", attrs={"class": "sitetable linklisting"})
                threads = threads_list_element.find_all(
                    "div", attrs={"data-subreddit-prefixed": "r/{}".format(subreddit_or_user)})
            else:
                threads_list_element = soup.find("div", attrs={"class": "sitetable linklisting"})
                threads = threads_list_element.find_all("div", attrs={"data-author": subreddit_or_user})

            max_count = (int(max_counter) if max_counter is not None else len(threads))

            while full is not True:
                for thread in threads:
                    try:
                        msg = "\nCollecting information from thread {} of {}...".format(counter, max_count)
                        logger.info(msg) if verbose else None

                        thread_details_path = thread.attrs["data-permalink"]
                        thread_url = self.constants.old_reddit_url + thread_details_path

                        thread_comments, img_urls = self.scrape_single_thread(
                            thread_details_path, verbose
                        )

                        current_thread = "{}".format(thread_url)
                        thread_img_urls[current_thread] = {
                            "author": self.scraper_helper.construct_author_dict(thread),
                            "datetime": self.scraper_helper.construct_time_dict(thread),
                            "rating": self.scraper_helper.construct_thread_rating_dict(thread),
                            "thread_url": thread_url,
                            "urls": img_urls,
                            "comments": thread_comments
                        }

                        msg = "Finished scrapping images for thread {}. {} images where scraped".format(
                            thread_url, len(list(set(img_urls))))
                        logger.info(msg) if verbose else None

                        if counter == max_count:
                            full = True
                            break
                        time.sleep(2)
                        counter += 1
                    except AttributeError:
                        continue
                if full:
                    break

                try:
                    next_button = soup.find("span", class_="next-button")
                    next_page_link = next_button.find("a").attrs["href"]  # type: ignore

                    req = requests.get(next_page_link, headers=self.constants.user_agent, timeout=10)
                    soup = BeautifulSoup(req.text, "html.parser")
                except TokenErrorException as exc:
                    self.logging_funcs.print_exception_log(str(exc), verbose)
                    break

            threads_urls[subreddit_or_user] = thread_img_urls

            logger.debug("[5] FINISHED SCRAPING STEP", verbose)
        else:
            message = "Error fetching results.. Try again!"
            self.logging_funcs.print_exception_log(message, verbose)

        return threads_urls

    @logger_wraps()
    def scrape_single_thread(self, link: str, verbose: bool):
        """
        Scrapes the given Reddit thread URL and returns a tuple containing a list of image URLs and a dictionary of
         comments.

        Args:
            link (str): The URL of the Reddit thread to be scraped.
            verbose (bool): Whether to print verbose logging messages.

        Returns:
            tuple[Any, dict[str, dict[str, Any]]]: A tuple containing a list of image URLs and a dictionary of comments.
        """
        msg = "Scraping thread: {}{}".format(self.constants.old_reddit_url, link)
        logger.info(msg) if verbose else None

        # Using a user-agent to mimic browser activity
        req = self.request_manager.request_page(self.constants.old_reddit_url + link, self.constants.user_agent)

        if req is not None:
            # Parsing through the web page for obtaining the right html tags
            # and scraping the details required
            soup = BeautifulSoup(req.text, "html.parser")

            thread_images = []

            thread_img_ele = soup.find("div", attrs={"class", "expando"})

            if thread_img_ele is not None:
                thread_image_a_tags = thread_img_ele.find_all("a", attrs={"class", "may-blank"})
                thread_iframe_tag = thread_img_ele.find("iframe", attrs={"class", "media-embed"})

                if thread_image_a_tags is not None and len(thread_image_a_tags) >= 1:
                    for thread_image_a_tag in thread_image_a_tags:
                        logging.debug(thread_image_a_tag.attrs["href"])
                        if self.validations.validate_if_url_is_a_valid_img_link(
                                thread_image_a_tag.attrs["href"], self.constants.possible_urls):
                            thread_images.append(thread_image_a_tag.attrs["href"])

                        img_tag = thread_img_ele.find("img", attrs={"class", "preview"})

                        if img_tag is not None:
                            logging.debug(img_tag.attrs["src"])
                            if self.validations.validate_if_url_is_a_valid_img_link(
                                    img_tag.attrs["src"], self.constants.possible_urls):
                                thread_images.append(img_tag.attrs["src"])

                if thread_iframe_tag is not None:
                    logging.debug(thread_iframe_tag.attrs["src"])
                    if self.validations.validate_image_url(
                            self.constants.possible_urls, thread_iframe_tag.attrs["src"]):
                        thread_images.append(thread_iframe_tag.attrs["src"])

            thread_images = list(set(thread_images))

            thread_comments, img_urls = self.comment_scrapper.scrape_comments(soup)

            # Remove all elements from thread_images that contain the value "crop=smart"
            thread_images = [x for x in thread_images if "crop=smart" not in x]

            logging.debug(thread_images)
            logging.debug(len(thread_images))

            img_urls = img_urls + thread_images
            return thread_comments, img_urls
