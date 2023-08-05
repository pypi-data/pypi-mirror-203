import glob
import json
import mimetypes
import os
import shutil
import sys
from pathlib import Path
from typing import Any
from loguru import logger       # type: ignore
from tqdm import tqdm
from PIL import Image       # type: ignore

from common.constants import ConstantsNamespace     # type: ignore
from common.logging.logging_setup import LoggingSetup       # type: ignore


class IOOperations:
    """
    The IOOperations class provides methods for input-output operations, including writing detailed post information,
    validating directories, sorting files by MIME type and resolution, and deleting original files.

    This class requires access to the ConstantsNamespace and LoggingSetup classes from the common package, as well as
    the PIL library for image processing.

    Methods:
        - def write_detailed_post_information(payload: Any, operation: str, filename) -> None:
            Writes payload to a file with the given filename, using the specified operation mode. The file format is
            determined by the extension of the filename. output_post_detailed_information(payload): Writes all image
            URLs in payload to a JSON file named src/output/image_urls.json, sorted by subreddit and post.
        - def validate_directories(input_dir):
            Checks if the input_dir directory exists. If it does not exist, logs an
            error message and exits the program.
        - def sort_by_mime_type_and_resolution(input_dir: Path, output_dir: Path, remove: bool):
            Sorts all files in the input_dir directory by MIME type and resolution. The sorted files are copied to the
            corresponding folders in the output_dir directory, and original files are deleted if the remove flag is set
             to True.
        -def delete_original_files(input_dir, remove): Deletes all original files in the input_dir directory if the
        remove flag is set to True.
    """

    def __init__(self) -> None:
        super().__init__()
        self.logging_funcs = LoggingSetup()
        self.constants = ConstantsNamespace()

    def init_directory(self, path):
        """
        Checks if a directory exists at the given path and creates it if it does not exist.

        Args:
        path (str): The path to the directory to check/create.
        """
        if not os.path.exists(path):
            os.makedirs(path)
            msg = "Directory created at {}".format(path)
            logger.debug(msg)
        else:
            msg = "Directory already exists at {}".format(path)
            logger.debug(msg)

    def init_directories(self):
        self.init_directory("./reports/users")
        self.init_directory("./reports/subreddits")
        self.init_directory("./subreddit/")
        self.init_directory("./logs/")

    def validate_directory(self, input_dir):
        """Check if the input directory exists and exit if it does not.

        Args:
            input_dir: The path to the input directory.

        Returns:
            None
        """
        # Checking if input directory exists
        input_dir_path = Path(input_dir)
        if not input_dir_path.exists():
            logger.error("Input directory does not exist")
            sys.exit()

    def write_detailed_post_information(self, payload: Any, operation: str, filename: str, verbose: bool) -> None:
        """Write payload to a file in the specified format.

        Args:
            payload: The data to be written to the file.
            operation: The file operation mode ('w' for write, 'a' for append, etc.).
            filename: The path and filename of the file to write to.
            verbose: Boolean flag that controls the verbosity output

        Returns:
            None
        """
        logger.debug("[9] STARTED WRITING SUBREDDIT REPORT INFORMATION STEP", verbose)

        extension = Path(filename).suffixes[-1]

        with open(filename, operation, encoding="utf-8") as file:
            if extension == ".txt":
                file.write(payload)
            elif extension == ".json":
                json_str = json.dumps(payload, indent=4)
                file.write(json_str)

        logger.debug("[9] FINISHED WRITING SUBREDDIT REPORT INFORMATION STEP", verbose)

    def create_output_folder_and_move_files(
            self, file_path: Path, output_dir: Path, matching_value: str, mimetype: str):
        """
        Creates the output folder and then moves the files to said folder
        Args:
            file_path:
            output_dir:
            matching_value:
            mimetype:

        Returns:

        """
        destination_path = os.path.join(
            output_dir, matching_value, mimetype.split("/")[1]
        )

        os.makedirs(destination_path, exist_ok=True)
        shutil.copy2(file_path, destination_path)
        msg = "Copied {} to {}".format(file_path, destination_path)
        logger.debug(msg)

    def delete_original_files(self, input_dir, remove, verbose):
        """Delete the original files from the input directory if `remove` is True.

        Args:
            verbose:
            input_dir: The path to the input directory.
            remove: Whether to remove the original files.

        Returns:
            None
        """
        logger.debug("[8] STARTED CLEANUP STEP", verbose)
        if remove:
            input_dir_path = Path(input_dir)
            for file in input_dir_path.iterdir():
                if file.is_file():
                    file.unlink()

        logger.debug("[8] FINISHED CLEANUP STEP", verbose)

    def sort_by_mime_type_and_resolution(self, input_dir: Path, output_dir: Path, remove: bool, verbose):
        """Sort image files in the input directory by MIME type and resolution and save them to the
        output directory.

        Args:
            verbose:
            input_dir: The path to the input directory.
            output_dir: The path to the output directory.
            remove: Whether to remove the original files after copying.

        Returns:
            None
        """
        logger.debug("[7] STARTED FILE SORTING STEP", verbose)

        msg = "Sorting downloaded images"
        logger.info(msg) if verbose else None

        image_files = glob.glob(str(input_dir) + "/*.jpg") + glob.glob(str(input_dir) + "/*.png") + glob.glob(
            str(input_dir) + "/*.gif")

        # Wrapping the loop with tqdm and customize the appearance of the progress bar
        with tqdm(
                total=len(image_files),
                desc="Sorting images",
                ncols=100,
                colour="green",
                unit_scale=True,
                dynamic_ncols=True) as pbar:
            for file_path in Path(input_dir).glob("*.*"):
                try:
                    with Image.open(file_path) as img:
                        width, height = img.size
                        mimetype, _ = mimetypes.guess_type(str(file_path))
                        # checks if img path has a mimetype, and it starts with image/.*
                        if mimetype and mimetype.startswith("image/"):
                            # match the resolution to the resolutions in the resolutions dict
                            matching_key = next((resolution for resolution in self.constants.resolutions.keys() if
                                                 resolution[0] <= width <= resolution[2] and resolution[1] <= height <=
                                                 resolution[3]), None)

                            # If any of resolutions match, save the img to the corresponding folder, if it doesn't
                            # save the image to an "other" folder
                            if matching_key:
                                matching_value = self.constants.resolutions[matching_key]

                                msg = "The corresponding resolution designation for the matching resolution {} is {}."\
                                    .format(matching_key, matching_value)
                                logger.debug(msg)

                                self.create_output_folder_and_move_files(
                                    file_path, output_dir, matching_value, mimetype)
                            else:
                                logger.debug("The resolution is not in the dictionary.")

                                self.create_output_folder_and_move_files(file_path, output_dir, "other", mimetype)

                except IOError as exc:
                    logger.error("Error occurred while processing %s: %s", file_path, exc)
                pbar.update(1)

        logger.debug("[7] FINISHED FILE SORTING STEP", verbose)

        # if remove flag is passed delete the original files
        self.delete_original_files(input_dir, remove, verbose)
