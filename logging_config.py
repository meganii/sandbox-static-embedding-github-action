import logging
import os


def configure_logging():
    """Configure root logger with a readable formatter and level from LOG_LEVEL env var."""
    log_level = os.environ.get("LOG_LEVEL", "INFO").upper()
    level = getattr(logging, log_level, logging.INFO)

    handler = logging.StreamHandler()
    fmt = "%(asctime)s %(levelname)-5s %(name)s: %(message)s"
    formatter = logging.Formatter(fmt, datefmt="%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)

    root = logging.getLogger()
    if not root.handlers:
        root.addHandler(handler)
    root.setLevel(level)


def get_logger(name: str):
    configure_logging()
    return logging.getLogger(name)
