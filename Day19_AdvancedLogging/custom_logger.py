import logging

logger = logging.getLogger(
    "cloud_app"
)

logger.setLevel(
    logging.INFO
)

logger.info(
    "Application Started"
)

logger.warning(
    "Memory Usage High"
)

logger.error(
    "Database Connection Failed"
)