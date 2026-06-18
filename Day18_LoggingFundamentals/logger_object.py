import logging

logger = logging.getLogger(
    "cloud_app"
)

logger.setLevel(
    logging.INFO
)

logger.info(
    "Cloud Application Started"
)

logger.warning(
    "CPU Usage High"
)

logger.error(
    "Database Connection Failed"
)