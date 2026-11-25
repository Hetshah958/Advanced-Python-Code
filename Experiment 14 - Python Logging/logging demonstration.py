import logging
from pathlib import Path

def configure_logging():
    logger = logging.getLogger("experiment14")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()
    logger.propagate = False

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    log_file = Path(__file__).with_name("app.log")
    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger

def main():
    logger = configure_logging()
    logger.debug("This is a DEBUG message.")
    logger.info("Application started successfully.")
    logger.warning("This is a WARNING message.")
    logger.error("An example ERROR message.")
    logger.critical("A CRITICAL event was recorded.")
    print("Log messages were written to the console and app.log.")

if __name__ == "__main__":
    main()
