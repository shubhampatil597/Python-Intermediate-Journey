import logging

from logging.handlers import TimedRotatingFileHandler

handler = TimedRotatingFileHandler(

    "timed.log",

    when="midnight",

    interval=1,

    backupCount=7

)

logger = logging.getLogger(
    "timed_logger"
)

logger.setLevel(
    logging.INFO
)

logger.addHandler(
    handler
)

logger.info(
    "Application Started"
)

print(
    "Timed Rotation Configured"
)