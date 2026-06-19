import logging

from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler(

    "application.log",

    maxBytes=1000,

    backupCount=3

)

logger = logging.getLogger()

logger.setLevel(
    logging.INFO
)

logger.addHandler(
    handler
)

for i in range(100):

    logger.info(
        f"Log Message {i}"
    )

print(
    "Rotation Completed"
)