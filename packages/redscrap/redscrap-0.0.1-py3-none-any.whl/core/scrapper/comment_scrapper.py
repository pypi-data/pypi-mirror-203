from loguru import logger  # type: ignore
import validators  # type: ignore

from common.logging.logging_setup import LoggingSetup  # type: ignore
from common.constants import ConstantsNamespace  # type: ignore
from common.image_downloader import ImageDownloader  # type: ignore
from common.logging.utils.loguru_wrappers import logger_wraps  # type: ignore
from common.validations.url_validations import UrlValidations  # type: ignore
from core.scrapper.scraper_helper import ScraperHelper


class CommentScrapper:
    """
    A class for scraping comments and replies from a given HTML element.

    Attributes:
        logging_funcs (LoggingSetup): An instance of LoggingSetup for logging purposes.
        constants (ConstantsNamespace): An instance of ConstantsNamespace for constants.
        validations (UrlValidations): An instance of UrlValidations for validating URLs.
        image_downloader (ImageDownloader): An instance of ImageDownloader for downloading images.
        scraper_helper (ScraperHelper): An instance of ScraperHelper for helper methods.

    Methods:
        scrape_comments(soup): Scrape comments from the given comments' element.
        scrape_replies(reply_divs): Scrapes the replies from the given reply divs and returns a list of dictionaries
        representing each reply.
    """

    def __init__(self) -> None:
        super().__init__()
        self.logging_funcs = LoggingSetup()
        self.constants = ConstantsNamespace()
        self.validations = UrlValidations()
        self.image_downloader = ImageDownloader()
        self.scraper_helper = ScraperHelper()
        self.processed_comments = []

    @logger_wraps()
    def scrape_comments(self, soup):
        """
        Scrape comments from the given comments' element.

        Args:
            soup:

        Returns:
            A list of dictionaries representing each comment, where each dictionary contains the following keys:
            - 'text': A string representing the text content of the comment.
            - 'author': A string representing the author of the comment.
            - 'rating': A dictionary representing the rating of the comment, where each key is a rating category
               (e.g. 'score_likes') and the value is the score for that category.
            - 'datetime': A dictionary representing the datetime information of the comment, where each key is a
               datetime category (e.g. 'time_since_posting') and the value is the corresponding datetime information.
            - 'numChildren': An integer representing the number of children replies for the given reply.
            - 'hasChildren': A boolean indicating whether the given reply has children replies or not.
            - 'urls': A list of strings representing the URLs found in the given comment.
            - 'replies': A list of nested dictionaries representing the children replies for the given reply.
        """
        comments = []
        img_urls = []
        self.processed_comments = []

        comment_area = soup.find("div", attrs={"class": "commentarea"})
        link_listing = comment_area.find("div", attrs={"class", "sitetable"}).children

        comments_link_listing = comment_area.find("div", attrs={"class", "sitetable"})

        for element in comments_link_listing:
            if "thing" in element.attrs["class"]:
                if element.attrs["data-permalink"] not in self.processed_comments:
                    comment = {"text": element.find("div", class_="md").text.strip(),
                               "author": self.scraper_helper.construct_author_dict(element),
                               "rating": self.scraper_helper.construct_rating_dict(element),
                               "datetime": self.scraper_helper.construct_time_dict(element),
                               "url": element.attrs["data-permalink"]
                               }

                    comment_has_children, comment_num_children = self.scraper_helper.define_children_fields(element)

                    comment["hasChildren"] = comment_has_children
                    comment["numChildren"] = comment_num_children

                    urls = self.scraper_helper.construct_urls_list(element)
                    img_urls = img_urls + urls
                    comment["urls"] = urls

                    comment["replies"] = []
                    child_div = element.find("div", attrs={"class", "child"})
                    reply_divs = child_div.find_all("div", attrs={"class", "comment"})

                    self.processed_comments.append(element.attrs["data-permalink"])

                    if reply_divs:
                        replies = self.scrape_replies(reply_divs)
                        replies = self.scraper_helper.remove_empty_lists(replies)
                        comment["replies"] = replies
                    comments.append(comment)

        logger.debug("Processed Replies: {}".format(len(self.processed_comments)))

        return comments, list(set(img_urls))

    @logger_wraps()
    def scrape_replies(self, reply_divs):
        """
        Scrapes the replies from the given reply divs and returns a list of dictionaries representing each reply.

        Args:
        reply_divs: A list of reply divs to scrape from.

        Returns:
        A list of dictionaries representing each reply, where each dictionary contains the following keys:
        - 'text': A string representing the text content of the reply.
        - 'author': A string representing the author of the reply.
        - 'rating': A dictionary representing the rating of the reply, where each key is a rating category
           (e.g. 'score_likes') and the value is the score for that category.
        - 'datetime': A dictionary representing the datetime information of the reply, where each key is a
           datetime category (e.g. 'time_since_posting') and the value is the corresponding datetime information.
        - 'numChildren': An integer representing the number of children replies for the given reply.
        - 'hasChildren': A boolean indicating whether the given reply has children replies or not.
        - 'urls': A list of strings representing the URLs found in the given reply.
        - 'replies': A list of nested dictionaries representing the children replies for the given reply.

        Raises:
        None
        """

        replies = []
        img_urls = []

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
                    processed_replies = self.scrape_replies(nested_reply_divs)
                    processed_replies = self.scraper_helper.remove_empty_lists(processed_replies)
                    reply['replies'] = processed_replies

                replies.append(reply)

        return replies, list(set(img_urls))
