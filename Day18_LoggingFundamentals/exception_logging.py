import logging

logging.basicConfig(
    level=logging.INFO
)

try:

    result = 10 / 0

except Exception:

    logging.exception(
        "Calculation Failed"
    )