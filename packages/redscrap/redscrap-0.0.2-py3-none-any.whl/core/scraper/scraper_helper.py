import glob
import re
from pathlib import Path
from typing import Dict, Tuple, List, Any
import bs4
import validators

from common.common_constants import CommonConstants  # type: ignore
from common.validations.url_validations import UrlValidations  # type: ignore


class ScraperHelper:
    """
    This class provides helper methods for web scraping comments and threads from forums.

    Methods:
    - def construct_author_dict(self, div_ele: BeautifulSoup) -> Dict[str, str]:
        Constructs a dictionary with the author's username and profile URL.
    - def construct_rating_dict(self, div_ele: BeautifulSoup) -> Dict[str, str]:
        Constructs a dictionary with the comment's rating scores.
    - def construct_thread_rating_dict(self, div_ele: BeautifulSoup) -> Dict[str, str]:
        Constructs a dictionary with the thread's rating scores.
    - def construct_time_dict(self, div_ele: BeautifulSoup) -> Dict[str, str]:
        Constructs a dictionary with the time information of the comment or thread.
    - def define_children_fields(self, div_ele: BeautifulSoup) -> Tuple[bool, int]:
        Defines the number of children and whether a comment or thread has children.
    - def construct_urls_list(self, div_ele: BeautifulSoup) -> List[str]:
        Constructs a list of URLs from the div element that contains the URLs.
    """

    def __init__(self) -> None:
        super().__init__()
        self.constants = CommonConstants()
        self.validations = UrlValidations()

    # noinspection PyUnresolvedReferences
    def construct_author_dict(self, div_ele: bs4.element.PageElement) -> Dict[str, str]:
        """
        Constructs a dictionary with the author's username and profile URL.

        Args:
            div_ele: A BeautifulSoup object representing a div element that contains the author's information.

        Returns:
            A dictionary with the author's username and profile URL.

        """
        author_el = div_ele.find("a", class_="author")

        author_username = author_el.text.strip()
        profile = author_el["href"]

        author = {"username": author_username, "profile": profile}

        return author

    # noinspection PyUnresolvedReferences
    def construct_rating_dict(self, div_ele: bs4.element.PageElement) -> Dict[str, str]:
        """
        Constructs a dictionary with the comment's rating scores.

        Args:
            div_ele: A BeautifulSoup object representing a div element that contains the comment's rating scores.

        Returns:
            A dictionary with the comment's rating scores.
        """
        rating = {}

        score_dislikes = div_ele.find("span", attrs={"class": "dislikes"})
        score_unvoted = div_ele.find("span", attrs={"class": "unvoted"})
        score_likes = div_ele.find("span", attrs={"class": "likes"})

        if score_dislikes is not None:
            parent_comment_author_score_dislikes = score_dislikes.text
            rating["score_dislikes"] = parent_comment_author_score_dislikes

        if score_unvoted is not None:
            parent_comment_author_score_unvoted = score_unvoted.text
            rating["score_unvote"] = parent_comment_author_score_unvoted

        if score_likes is not None:
            parent_comment_author_score_likes = score_likes.text
            rating["score_likes"] = parent_comment_author_score_likes

        return rating

    # noinspection PyUnresolvedReferences
    def construct_thread_rating_dict(self, div_ele: bs4.element.PageElement) -> Dict[str, str]:
        """
        Constructs a dictionary with the thread's rating scores.

        Args:
            div_ele: A BeautifulSoup object representing a div element that contains the thread's rating scores.

        Returns:
            A dictionary with the thread's rating scores.

        """
        rating = {}

        score_dislikes = div_ele.find("div", attrs={"class": "dislikes"})
        score_unvoted = div_ele.find("div", attrs={"class": "unvoted"})
        score_likes = div_ele.find("div", attrs={"class": "likes"})

        if score_dislikes is not None:
            parent_comment_author_score_dislikes = score_dislikes.text
            rating["score_dislikes"] = parent_comment_author_score_dislikes

        if score_unvoted is not None:
            parent_comment_author_score_unvoted = score_unvoted.text
            rating["score_unvote"] = parent_comment_author_score_unvoted

        if score_likes is not None:
            parent_comment_author_score_likes = score_likes.text
            rating["score_likes"] = parent_comment_author_score_likes

        return rating

    # noinspection PyUnresolvedReferences
    def construct_time_dict(self, div_ele: bs4.element.PageElement) -> Dict[str, str]:
        """
        Constructs a dictionary with the time information of the comment or thread.

        Args:
            div_ele: A BeautifulSoup object representing a div element that contains the time information.

        Returns:
            A dictionary with the time information of the comment or thread.

        """
        time = {}

        time_el = div_ele.find("time", attrs={"class": ["live-timestamp"]})

        if time_el is not None:
            time["time"] = time_el.attrs["title"]
            time["datetime"] = time_el.attrs["datetime"]
            time["time_since_posting"] = time_el.text

        return time

    # noinspection PyUnresolvedReferences
    def define_children_fields(self, div_ele: bs4.element.PageElement) -> Tuple[bool, int]:
        """
        Defines the number of children and whether a comment or thread has children.

        Args:
            div_ele: A BeautifulSoup object representing a div element that contains the information about children.

        Returns:
            A tuple with the boolean value indicating whether the comment or thread has children, and the number of
            children (an integer) if there are any.

        """
        num_children_el = div_ele.find("a", attrs={"class": ["numchildren"]})

        num_children = None
        has_children = None

        if num_children_el is not None:
            pattern = self.constants.extract_num_children
            num_children = re.findall(pattern, num_children_el.text)[0]
            num_children = int(num_children)
            has_children = True if num_children > 0 else False

        return has_children, num_children

    # noinspection PyUnresolvedReferences

    def construct_urls_list(self, div_ele: bs4.element.PageElement) -> List[str]:
        """
        Constructs a list of URLs from the div element that contains the URLs.

        Args:
            div_ele: A BeautifulSoup object representing a div element that contains URLs.

        Returns:
            A list of URLs that are valid image links.
        """
        urls = []
        for url in div_ele.find_all("a", href=True):
            if (validators.url(url["href"]) and self.validations.validate_if_url_is_a_valid_img_link(
                    url["href"], self.constants.possible_urls)):
                urls.append(url["href"])
        return urls

    def remove_empty_lists(self, lst: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Recursively remove empty lists from a nested list.

        Args:
            lst (list): A list to remove empty lists from.

        Returns:
            list: A new list with all empty lists removed.
        """

        result = []
        for elem in lst:
            if isinstance(elem, list):
                elem = self.remove_empty_lists(elem)
                if elem:
                    result.append(elem)
            else:
                result.append(elem)
        return result

    def generate_list_of_img_files_in_dir(self, directory: Path) -> List[str]:
        """Generate a list of image files in a directory.

        Args:
            directory (pathlib.Path): The directory to search for image files.

        Returns:
            list: A list of image file paths.
        """

        image_files = glob.glob(str(directory) + "/*.jpg") + glob.glob(str(directory) + "/*.png") \
                      + glob.glob(str(directory) + "/*.gif")
        return image_files
