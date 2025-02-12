import logging.config

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s:%(name)s:%(process)d:%(lineno)d " "%(levelname)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console_output": {
            "formatter": "default",
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "lubimovka": {
            "level": "DEBUG",
            "handlers": [
                "console_output",
            ],
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "console_output",
        ],
    },
}
logging.config.dictConfig(LOGGING_CONFIG)
