import logging

MAIN_DIR = "/app"
FILES_DIR = f"{MAIN_DIR}/files"

logging.basicConfig(
    format="%(asctime)s,%(msecs)d - %(name)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
    handlers=[logging.FileHandler(f"{FILES_DIR}/internet_connection.log"), logging.StreamHandler()],
)


LOGGER = logging.getLogger("internetConnectionLog")
