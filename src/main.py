import time

from src import Server
from src.internet_connection_log_service import InternetConnectionLogService
from src.config import LOGGER


if __name__ == "__main__":
    LOGGER.debug("Starting internet connection log service")

    telecom_personal_server = Server(server_name="Telecom Personal", server_id=58819)
    internet_cordoba_server = Server(server_name="INTERNET CÓRDOBA", server_id=43996)

    LOGGER.debug("Servers loaded", extra={"servers": [telecom_personal_server, internet_cordoba_server]})

    internet_connection_log_service = InternetConnectionLogService.build()
    seconds_between_runs = 900
    while True:
        internet_connection_log_service.log_internet_connection_for_multiple_servers(
            servers=[telecom_personal_server, internet_cordoba_server]
        )

        LOGGER.debug(
            f"Seconds between runs {seconds_between_runs}", extra={"seconds_between_runs": seconds_between_runs}
        )
        time.sleep(seconds_between_runs)
