import logging

logging.basicConfig(
    format="%(asctime)s,%(msecs)d - %(name)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
    handlers=[
            logging.FileHandler("/app/src/internet_connection.log"),
            logging.StreamHandler()
        ]
)


LOGGER = logging.getLogger("internetConnectionLog")
