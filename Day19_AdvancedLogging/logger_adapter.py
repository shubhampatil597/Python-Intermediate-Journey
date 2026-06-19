import logging

logger = logging.getLogger(
    "authentication"
)

adapter = logging.LoggerAdapter(

    logger,

    {

        "user": "admin"

    }

)

adapter.info(
    "Login Successful"
)