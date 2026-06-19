import logging

class ErrorFilter(

    logging.Filter

):

    def filter(

        self,

        record

    ):

        return (

            record.levelno

            >= logging.ERROR

        )

logger = logging.getLogger()

logger.addFilter(

    ErrorFilter()

)

logger.warning(
    "Ignored Warning"
)

logger.error(
    "Database Failed"
)

logger.critical(
    "Server Down"
)