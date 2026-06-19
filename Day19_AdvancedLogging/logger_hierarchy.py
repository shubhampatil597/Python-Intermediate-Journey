import logging

auth_logger = logging.getLogger(
    "company.auth"
)

db_logger = logging.getLogger(
    "company.database"
)

auth_logger.warning(
    "Failed Login Attempt"
)

db_logger.error(
    "Database Connection Lost"
)