import logging

logging.basicConfig(
    level=logging.INFO
)

cpu_usage = 92

if cpu_usage > 90:

    logging.warning(

        f"CPU Usage High: {cpu_usage}%"

    )