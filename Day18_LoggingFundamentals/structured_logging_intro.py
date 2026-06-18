import logging

logging.basicConfig(
    level=logging.INFO
)

user = "Shubham"

ip = "192.168.1.100"

logging.info(

    f"EVENT=LOGIN "

    f"USER={user} "

    f"IP={ip}"

)