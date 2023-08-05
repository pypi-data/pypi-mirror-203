"""
########################################################################################
# Author:       Martim Lima (martim.d.lima@protonmail.com)                             #
#                                                                                      #
# Date:         21/03/23                                                               #
#                                                                                      #
# Name:         reddit_subreddit_img_scrapper.py                                       #
#                                                                                      #
# Version:      1.0                                                                    #
#                                                                                      #
# Description:  This Python script that scrapes images from Reddit posts on a given    #
#               subreddit. It includes functions to download images from URLs, extract #
#               URLs from text, and write URLs to a text file.                         #
#                                                                                      #
#                                                                                      #
# Usage:        ./reddit_subreddit_img_scrapper.py                                     #
#                                                                                      #
# Required:                                                                            #
#                                                                                      #
# Dependencies:  os, sys shutil, argparse, logging, PIL, mimetypes, collections,       #
#                pathlib                                                               #
#                                                                                      #
# Notes:                                                                               #
#                                                                                      #
# Change History: - 14/03/2023  Martim Lima   Initial Entry                            #
#                                                                                      #
########################################################################################
########################################################################################
########################################################################################
#                                                                                      #
#  Copyright (C) 2023 Martim Lima                                                      #
#  martim.d.lima@protonmail.com                                                        #
#                                                                                      #
#  This program is free software; you can redistribute it and/or modify                #
#  it under the terms of the GNU General Public License as published by                #
#  the Free Software Foundation; either version 2 of the License, or                   #
#  (at your option) any later version.                                                 #
#                                                                                      #
#  This program is distributed in the hope that it will be useful,                     #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of                      #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                       #
#  GNU General Public License for more details.                                        #
#                                                                                      #
#  You should have received a copy of the GNU General Public License                   #
#  along with this program; if not, write to the Free Software                         #
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA           #
#                                                                                      #
########################################################################################
########################################################################################
########################################################################################
"""

from pathlib import Path
from loguru import logger  # type: ignore
import click

# import logging
from common.io_operations import IOOperations  # type: ignore
from common.logging.loguru_setup import LoggingSetup  # type: ignore
from common.logging.logging_constants import LoggingConstantsNamespace  # type: ignore
from core.helper.main_helper import MainHelper

logging_constants = LoggingConstantsNamespace()

LoggingSetup.script_logger_config_dict(
    logger,
    Path(logging_constants.log_filename).name,
    logging_constants.default_log_file_level,
    logging_constants.default_log_format,
    logging_constants.default_log_colorizing,
    logging_constants.default_log_rotation,
    logging_constants.default_log_retention,
    logging_constants.default_log_compression,
    logging_constants.default_log_delay,
    logging_constants.default_log_mode,
    logging_constants.default_log_buffering,
    logging_constants.default_log_encoding,
    logging_constants.default_log_serialize,
    logging_constants.default_log_backtrace,
    logging_constants.default_log_diagnose,
    logging_constants.default_log_enqueue,
    logging_constants.default_log_catch,
    False,  # enables/disables debug mode logs
)

io_operations = IOOperations()
main_helper = MainHelper()


@click.command()
@click.option("-n", "--number_results", type=int, help="Number of threads to scrape")
@click.option("-x", "--scrape", type=click.Choice(["user", "subreddits"]), default="hot",
              help="Scrape user or subreddit")
@click.option("-s", "--sorting_filter", type=click.Choice(["top", "hot", "new"]), default="hot", help="Filter threads")
@click.option("-u", "--reddit_user", type=str, help="The reddit user to search")
@click.option("-r", "--subreddits", type=str, help="The subreddit/s to search")
@click.option("-d", "--details", is_flag=True, default=False,
              help="If enable outputs the detailed list of threads of each subreddit provided into an individual file")
@click.option("-v", "--verbose", is_flag=True, default=False, help="Enables verbose mode")
def main(number_results, scrape, sorting_filter, reddit_user, subreddits, details, verbose):
    """
    Script main entry point
    """

    logger.debug("[1] - STARTING reddit_scrapper")

    io_operations.init_directories()

    match scrape:
        case "user":
            if not reddit_user:
                msg = "If you want to scrape a user profile you must provide a reddit user"
                raise click.exceptions.UsageError(msg)
            else:
                main_helper.scrape_user(reddit_user, sorting_filter, number_results, verbose)

        case "subreddits":
            main_helper.scrape_subreddit(subreddits, sorting_filter, number_results, details, verbose)

    logger.debug("[10] - ENDING reddit_scrapper")


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
