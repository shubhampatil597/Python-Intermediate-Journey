import logging

logging.basicConfig(

    filename="cloud.log",

    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s"

)

logs = [

    "INFO Server Started",

    "WARNING CPU Usage High",

    "ERROR Database Failed",

    "INFO Request Received",

    "ERROR Timeout"

]

for log in logs:

    if "ERROR" in log:

        logging.error(log)

    elif "WARNING" in log:

        logging.warning(log)

    else:

        logging.info(log)

print(
    "Cloud Log Analysis Complete"
)