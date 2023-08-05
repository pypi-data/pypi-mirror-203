from pathlib import Path
from loguru import logger  # type: ignore
import click

# import logging
from common.io_operations import IOOperations  # type: ignore
from common.logging.loguru_setup import LoguruSetup  # type: ignore
from common.logging.logging_constants import LoggingConstants  # type: ignore
from core.helper.main_helper import MainHelper

logging_constants = LoggingConstants()
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
@click.option("-o", "--output", type=str, help="The directory to output the downloads")
@click.option("-v", "--verbose", is_flag=True, default=False, help="Enables verbose mode")
def main(number_results, scrape, sorting_filter, reddit_user, subreddits, details, output, verbose):
    """
    Script main entry point
    """

    # Setups directories used in the application
    with logger.catch(reraise=True):
        logger.remove()
        output_directory = io_operations.init_directories(output)

    logger.debug("[1] - STARTING reddit_scrapper")

    # Setups logging for the application
    LoguruSetup.script_logger_config_dict(
        logger,
        output_directory,
        Path(logging_constants.log_filename).name,
        logging_constants.default_log_stfout_level,
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

    # Scrapes a user or subreddit
    match scrape:
        case "user":
            if not reddit_user:
                msg = "If you want to scrape a user profile you must provide a reddit user"
                raise click.exceptions.UsageError(msg)
            else:
                main_helper.scrape_user(reddit_user, sorting_filter, number_results, output_directory, verbose)

        case "subreddits":
            main_helper.scrape_subreddit(subreddits, sorting_filter, number_results, details, output_directory,  verbose)

    logger.debug("[10] - ENDING reddit_scrapper")


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
