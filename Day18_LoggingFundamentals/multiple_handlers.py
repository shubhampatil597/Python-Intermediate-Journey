import logging

logger = logging.getLogger(
    "multi_handler"
)

logger.setLevel(
    logging.INFO
)

console_handler = logging.StreamHandler()

file_handler = logging.FileHandler(
    "app.log"
)

logger.addHandler(
    console_handler
)

logger.addHandler(
    file_handler
)

logger.info(
    "Application Started"
)

logger.warning(
    "Memory Usage High"
)