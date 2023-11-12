import logging
import logging.config

logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)


def main():
    logger.info("Hello World")  # will not print anything
    logger.warning("Watch out!")  # will print a message to the console


if __name__ == "__main__":
    main()
