import logging

logging.basicConfig(

    filename="application.log",

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s"

)

logging.info(
    "Application Started"
)

logging.warning(
    "Disk Space Low"
)

logging.error(
    "Database Failed"
)

print(
    "Logs Saved Successfully"
)