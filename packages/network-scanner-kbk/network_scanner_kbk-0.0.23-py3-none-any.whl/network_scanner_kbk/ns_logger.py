import logging
import os


class NSLogger():
    def __init__(self):
        """
        This class provides an interface to the python logging module.  This
        class also provides methods to view several NetworkScanner data
        structures.
        """
        # Create logger
        self.logger = logging.getLogger(__name__)

        # Default to DEBUG for output file
        self.logger.setLevel(logging.DEBUG)

        # Log to the root of the package so data is not mixed with source
        log_file_name = os.path.join("..", "..", "network_scanner.log")
        file_handler = logging.FileHandler(log_file_name)
        format_string = '%(asctime)s : %(levelname)s : %(name)s : %(message)s'
        formatter = logging.Formatter(format_string)
        file_handler.setFormatter(formatter)

        # Add file handler to logger
        self.logger.addHandler(file_handler)

        # Also send logger information to the console
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)  # Default to INFO for console output
        self.logger.addHandler(console)

    # Wrap 3 of the 5 logging levels: debug, info, and warning.
    # For simplicity, levels error and critical are not used in this package.
    # Errors are reported through exception handling.
    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)


if __name__ == "__main__":
    print("Testing NSLogger")
    ns_log = NSLogger()
    ns_log.info("Logging INFO level message to module log file.")
