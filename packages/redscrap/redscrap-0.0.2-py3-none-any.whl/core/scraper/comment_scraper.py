import typing
from typing import List, Dict, Tuple, Any

import bs4
from bs4 import BeautifulSoup
from loguru import logger  # type: ignore
import validators  # type: ignore

from common.logging.logging_setup import LoggingSetup  # type: ignore
from common.common_constants import CommonConstants  # type: ignore
from common.image_downloader import ImageDownloader  # type: ignore
from common.logging.utils.loguru_wrappers import logger_wraps  # type: ignore
from common.validations.url_validations import UrlValidations  # type: ignore
from core.scraper.scraper_helper import ScraperHelper


class CommentScraper:
    """
    A class for scraping comments and replies from a given HTML element.

    Attributes:
        logging_funcs (LoggingSetup): An instance of LoggingSetup for logging purposes.
        constants (CommonConstants): An instance of ConstantsNamespace for constants.
        validations (UrlValidations): An instance of UrlValidations for validating URLs.
        image_downloader (ImageDownloader): An instance of ImageDownloader for downloading images.
        scraper_helper (ScraperHelper): An instance of ScraperHelper for helper methods.

    Methods:
        def scrape_comments(soup): Scrape comments from the given comments' element.
        def scrape_replies(reply_divs): Scrapes the replies from the given reply divs and returns a list of dictionaries
        representing each reply.
    """

    def __init__(self) -> None:
        super().__init__()
        self.logging_funcs = LoggingSetup()
        self.constants = CommonConstants()
        self.validations = UrlValidations()
        self.image_downloader = ImageDownloader()
        self.scraper_helper = ScraperHelper()
        self.processed_comments = []

    # noinspection PyUnresolvedReferences
    @logger_wraps()
    def scrape_comments(self, soup: BeautifulSoup) -> Tuple[List[Dict[str, any]], List[str]]:
        """
        Scrape comments from the given comments' element.

        Args:
            soup (bs4.BeautifulSoup): A BeautifulSoup object representing the HTML or XML source.

        Returns:
            (Tuple[List[Dict[str, any]], List[str]]):
                A tuple containing two items:
                    - A list of dictionaries representing each comment, where each dictionary contains the following
                      keys:
                        - 'text': A string representing the text content of the comment.
                        - 'author': A dictionary representing the author of the comment.
                        - 'rating': A dictionary representing the rating of the comment, where each key is a rating
                            category
                            (e.g. 'score_likes') and the value is the score for that category.
                        - 'datetime': A dictionary representing the datetime information of the comment, where each
                            key is a datetime category (e.g. 'time_since_posting') and the value is the corresponding
                            datetime information.
                        - 'numChildren': An integer representing the number of children replies for the given reply.
                        - 'hasChildren': A boolean indicating whether the given reply has children replies or not.
                        - 'urls': A list of strings representing the URLs found in the given comment.
                        - 'replies': A list of nested dictionaries representing the children replies for the given
                            reply.
                    - A list of strings representing the URLs of any images found in the comments.
        """

        comments: List[Dict[str, any]] = []
        img_urls: List[str] = []
        self.processed_comments: List[str] = []

        comment_area: bs4.element.Tag = soup.find("div", attrs={"class": "commentarea"})
        comments_link_listing: bs4.element.Tag = comment_area.find("div", attrs={"class", "sitetable"})

        for comment_ele in comments_link_listing:
            c_ele: bs4.element.PageElement = comment_ele
            if "thing" in c_ele.attrs["class"]:
                if c_ele.attrs["data-permalink"] not in self.processed_comments:
                    comment = {"text": c_ele.find("div", class_="md").text.strip(),
                               "author": self.scraper_helper.construct_author_dict(c_ele),
                               "rating": self.scraper_helper.construct_rating_dict(c_ele),
                               "datetime": self.scraper_helper.construct_time_dict(c_ele),
                               "url": c_ele.attrs["data-permalink"]
                               }

                    comment_has_children, comment_num_children = self.scraper_helper.define_children_fields(c_ele)

                    comment["hasChildren"] = comment_has_children
                    comment["numChildren"] = comment_num_children

                    urls = self.scraper_helper.construct_urls_list(c_ele)
                    img_urls = img_urls + urls
                    comment["urls"] = urls

                    comment["replies"] = []
                    child_div = c_ele.find("div", attrs={"class", "child"})
                    reply_divs = child_div.find_all("div", attrs={"class", "comment"})

                    self.processed_comments.append(c_ele.attrs["data-permalink"])

                    if reply_divs:
                        replies, img_urls = self.scrape_replies(reply_divs)
                        processed_replies: List[Dict[str, Any]] = self.scraper_helper.remove_empty_lists(replies)
                        comment["replies"] = processed_replies
                    comments.append(comment)

        logger.debug("Processed Replies: {}".format(len(self.processed_comments)))

        return comments, list(set(img_urls))

    # noinspection PyUnresolvedReferences
    @logger_wraps()
    def scrape_replies(self, reply_divs: List[Any]) -> Tuple[List[Dict[str, Any]], List[str]]:
        """
        Scrapes the replies from the given reply divs and returns a list of dictionaries representing each reply.

        Args:
            reply_divs: A list of reply divs to scrape from.

        Returns:
            (Tuple[List[Dict[str, Any]], List[str]]):
                A tuple containing:
                    - A list of dictionaries representing each reply, where each dictionary contains the following keys:
                        - 'text': A string representing the text content of the reply.
                        - 'author': A dictionary representing the author of the reply.
                        - 'rating': A dictionary representing the rating of the reply, where each key is a rating
                        category (e.g. 'score_likes') and the value is the score for that category.
                        - 'datetime': A dictionary representing the datetime information of the reply, where each key
                            is a datetime category (e.g. 'time_since_posting') and the value is the corresponding
                            datetime information.
                        - 'numChildren': An integer representing the number of children replies for the given reply.
                        - 'hasChildren': A boolean indicating whether the given reply has children replies or not.
                        - 'urls': A list of strings representing the URLs found in the given reply.
                        - 'replies': A list of nested dictionaries representing the children replies for the given
                            reply.
                    - A list of unique URLs found in the scraped replies.
        """

        replies: List[Dict[str, typing.Any]] = []
        img_urls: List[str] = []

        for reply_div in reply_divs:
            if reply_div.attrs["data-permalink"] not in self.processed_comments:
                reply = {"text": reply_div.find("div", class_="md").text.strip(),
                         "author": self.scraper_helper.construct_author_dict(reply_div),
                         "rating": self.scraper_helper.construct_rating_dict(reply_div),
                         "datetime": self.scraper_helper.construct_time_dict(reply_div),
                         "url": reply_div.attrs["data-permalink"]}

                reply_has_children, reply_num_children = self.scraper_helper.define_children_fields(reply_div)
                reply["hasChildren"] = reply_has_children
                reply["numChildren"] = reply_num_children

                urls = self.scraper_helper.construct_urls_list(reply_div)
                reply["urls"] = urls
                img_urls = img_urls + urls
                reply["replies"] = []

                self.processed_comments.append(reply_div.attrs["data-permalink"])

                nested_reply_divs = reply_div.find_all('div', class_='comment')
                if nested_reply_divs:
                    processed_replies, img_urls = self.scrape_replies(nested_reply_divs)
                    post_processed_replies: List[Dict[str, Any]] = \
                        self.scraper_helper.remove_empty_lists(processed_replies)
                    reply['replies'] = post_processed_replies

                replies.append(reply)

        return replies, list(set(img_urls))
