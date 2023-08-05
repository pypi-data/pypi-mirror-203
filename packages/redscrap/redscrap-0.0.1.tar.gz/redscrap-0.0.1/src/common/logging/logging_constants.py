from datetime import time
from common.StringBuilder import StringBuilder      # type: ignore

string_builder = StringBuilder()


class LoggingConstantsNamespace:
    """
    A class representing a namespace for various constants used throughout the
    application.

    Attributes:
    - PROVIDERS (dict): a dictionary mapping shortening service names to their
      respective API endpoints.
    - TRACE_LEVEL (str): a constant string representing the TRACE logging
      level.
    - TRACE_SEVERITY_LEVEL (int): an integer representing the severity
      level for TRACE logging.
    - DEBUG_LEVEL (str): a constant string representing the DEBUG
      logging level.
    - DEBUG_SEVERITY_LEVEL (int): an integer representing the severity
      level for DEBUG logging.
    - INFO_LEVEL (str): a constant string representing the INFO
      logging level.
    - INFO_SEVERITY_LEVEL (int): an integer representing the severity
      level for INFO logging.
    - SUCCESS_LEVEL (str): a constant string representing the SUCCESS
      logging level.
    - SUCCESS_SEVERITY_LEVEL (int): an integer representing the severity
      level for SUCCESS logging.
    - WARNING_LEVEL (str): a constant string representing the WARNING
      logging level.
    - WARNING_SEVERITY_LEVEL (int): an integer representing the severity
      level for WARNING logging.
    - ERROR_LEVEL (str): a constant string representing the ERROR
      logging level.
    - ERROR_SEVERITY_LEVEL (int): an integer representing the severity
      level for ERROR logging.
    - CRITICAL_LEVEL (str): a constant string representing the CRITICAL
      logging level.
    - CRITICAL_SEVERITY_LEVEL (int): an integer representing the severity
    level for CRITICAL logging.
    - BUG (str): a constant string representing a bug emoji.
    - ROBOT (str): a constant string representing a robot emoji.
    - ROCKET (str): a constant string representing a rocket emoji.
    - RED_ALARM (str): a constant string representing a red alarm emoji.
    - RED_CIRCLE (str): a constant string representing a red circle emoji.
    - GREEN_CIRCLE (str): a constant string representing a green circle emoji.
    - WARNING (str): a constant string representing a warning emoji.
    - LIGHTNING_BOLT (str): a constant string representing a lightning bolt
      emoji.
    - SKULL (str): a constant string representing a skull emoji.
    - CHECK_MARK (str): a constant string representing a check mark emoji.
    - CROSS (str): a constant string representing a cross emoji.
    - INFO (str): a constant string representing an info icon.
    - DEFAULT_LOG_FORMAT (str): a default logging format string.
    - DEFAULT_LOG_FORMAT2 (str): a secondary default logging format string.
    - DEFAULT_LOG_FILE_LEVEL (str): a default logging level for file output.
    - DEFAULT_LOG_STDOUT_LEVEL (str): a default logging level for stdout
      output.
    - DEFAULT_LOG_COLORIZING (bool): a boolean indicating whether to colorize
      log output.
    - DEFAULT_LOG_ROTATION (float): a default log file rotation size in bytes.
    - DEFAULT_LOG_RETENTION (str): a default log file retention period.
    - DEFAULT_LOG_COMPRESSION (str): a default log file compression format.
    - DEFAULT_LOG_DELAY (bool): a boolean indicating whether to delay logging
      until the process is fully initialized.
    - DEFAULT_LOG_MODE (str): a default file logging mode.
    - DEFAULT_LOG_BUFFERING (int): a default file logging buffering level.
    - DEFAULT_LOG_ENCODING (str): a default file logging encoding.
    - DEFAULT_LOG_SERIALIZE (bool): a boolean indicating whether to serialize
      log messages.
    - DEFAULT_LOG_BACKTRACE (bool): a boolean indicating whether to include
      backtraces in log messages.
    - DEFAULT_LOG_DIAGNOSE (bool): a boolean indicating whether to diagnose
      issues with logging.
    - DEFAULT_LOG_ENQUEUE (bool): a boolean indicating whether to diagnose
      issues with logging.
    - DEFAULT_LOG_CATCH (bool): a boolean indicating whether to diagnose
      issues with logging.
    """

    #
    # Logging Constants ################################################################
    #

    @property
    def log_filename(self):
        return "redscrap.log"

    @property
    def trace_level(self):
        return "TRACE"

    @property
    def trace_severity_level(self):
        return 5

    @property
    def debug_level(self):
        return "DEBUG"

    @property
    def debug_severity_level(self):
        return 10

    @property
    def info_level(self):
        return "INFO"

    @property
    def info_severity_level(self):
        return 20

    @property
    def success_level(self):
        return "SUCCESS"

    @property
    def success_severity_level(self):
        return 25

    @property
    def warning_level(self):
        return "WARNING"

    @property
    def warning_severity_level(self):
        return 30

    @property
    def error_level(self):
        return "ERROR"

    @property
    def error_severity_level(self):
        return 40

    @property
    def critical_level(self):
        return "CRITICAL"

    @property
    def critical_severity_level(self):
        return 50

    @property
    def bug_symbol(self):
        return "🐞"

    @property
    def robot_symbol(self):
        return "🤖"

    @property
    def rocket_symbol(self):
        return "🚀"

    @property
    def red_alarm_symbol(self):
        return "🚨"

    @property
    def red_circle_symbol(self):
        return "🔴"

    @property
    def green_circle_symbol(self):
        return "🟢"

    @property
    def warning_symbol(self):
        return "⚠️"

    @property
    def lightning_bolt_symbol(self):
        return "⚡"

    @property
    def skull_symbol(self):
        return "☠️"

    @property
    def check_mark_symbol(self):
        return "✔️"

    @property
    def cross_symbol(self):
        return "❌"

    @property
    def info_symbol(self):
        return "🛈 "

    @property
    def default_log_format(self):
        log_format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
            "<level>{level.icon}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
            " - <level>{message}</level>"
        )
        return log_format

    @property
    def default_log_format2(self):
        return (
            "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {level.icon}"
            "| {name}:{function}:{line} | {message}"
        )

    @property
    def padding_log_format(self):
        log_format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
            "<level>{level.icon}</level> <level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}{extra[padding]}</cyan> - "
            "<level>{message}\n{exception}</level>"
        )
        return log_format

    @property
    def default_logger_format(self):
        """
        Default logger format
        """
        return "%(asctime)s - %(levelname)-4s - %(name)-s - %(message)s"

    @property
    def default_logger_date_format(self):
        """
        Default logger date format
        """
        return "%d-%b-%Y %H:%M:%S"

    @property
    def debug_mode_flag(self):
        return True

    @property
    def default_log_rotation_time(self):
        datetime = time(0, 0, 0)
        return datetime

    @property
    def default_log_file_level(self):
        return "DEBUG"

    @property
    def default_log_stdout_level(self):
        return "ERROR"

    @property
    def default_log_colorizing(self):
        return True

    @property
    def default_log_rotation(self):
        return 5e8

    @property
    def default_log_retention(self):
        return "10 days"

    @property
    def default_log_compression(self):
        return "zip"

    @property
    def default_log_delay(self):
        return False

    @property
    def default_log_mode(self):
        return "a"

    @property
    def default_log_buffering(self):
        return 1

    @property
    def default_log_encoding(self):
        return "utf8"

    @property
    def default_log_serialize(self):
        return True

    @property
    def default_log_backtrace(self):
        return False

    @property
    def default_log_diagnose(self):
        return False

    @property
    def default_log_enqueue(self):
        return False

    @property
    def default_log_catch(self):
        return False
