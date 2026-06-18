import logging

logging.basicConfig(
    level=logging.INFO
)

failed_user = "admin"

logging.warning(

    f"Failed Login Attempt "

    f"User={failed_user}"

)