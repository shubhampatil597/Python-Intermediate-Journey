import logging

from logging.handlers import RotatingFileHandler

logger = logging.getLogger(
    "deployment"
)

logger.setLevel(
    logging.INFO
)

handler = RotatingFileHandler(

    "deployment.log",

    maxBytes=1000,

    backupCount=3

)

logger.addHandler(
    handler
)

logger.info(
    "Deployment Started"
)

logger.info(
    "Application Uploaded"
)

logger.info(
    "Dependencies Installed"
)

logger.info(
    "Application Configured"
)

logger.info(
    "Deployment Completed"
)

print(
    "Deployment Successful"
)