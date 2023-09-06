import time

from speed_test_gateway import SpeedTestGateway, Server
from speed_test_parser import SpeedTestParser
from config import LOGGER


def run_speed_test():
    telecom_personal_server = Server(server_name="Telecom Personal", server_id=58819)
    telecom_personal_speed_test_output = SpeedTestGateway.get_speed_test_result(telecom_personal_server.server_id)
    telecom_personal_parsed_output = SpeedTestParser.parse_output(json_output=telecom_personal_speed_test_output)
    LOGGER.debug(f'Resultados test de velocidad: {telecom_personal_server.server_name}',
                 extra=telecom_personal_parsed_output.to_dict())

    internet_cordoba_server = Server(server_name="INTERNET CÓRDOBA", server_id=43996)
    internet_cordoba_speed_test_output = SpeedTestGateway.get_speed_test_result(
        internet_cordoba_server.server_id
    )
    internet_cordoba_parsed_output = SpeedTestParser.parse_output(json_output=internet_cordoba_speed_test_output)
    LOGGER.debug(f'Resultados test de velocidad: {internet_cordoba_server.server_name}',
                 extra=internet_cordoba_parsed_output.to_dict())

if __name__ == "__main__":
    while True:
        run_speed_test()
        time.sleep(900)