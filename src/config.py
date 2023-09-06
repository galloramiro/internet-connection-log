import logging

logging.basicConfig(
    filename="/app/internet_connection.log",
    filemode="a",
    format="%(asctime)s,%(msecs)d - %(name)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)


LOGGER = logging.getLogger("internetConnectionLog")
