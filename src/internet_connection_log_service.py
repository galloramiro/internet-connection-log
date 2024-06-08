from src.speed_test_gateway import SpeedTestGateway, Server
from src.speed_test_parser import SpeedTestParser
from src.config import LOGGER
from src.speed_test_json_repository import SpeedTestJsonRepository


class InternetConnectionLogService:
    def __init__(self, gateway: SpeedTestGateway, parser: SpeedTestParser, repository: SpeedTestJsonRepository):
        self.gateway = gateway
        self.parser = parser
        self.repository = repository

    def log_internet_connection_for_single_server(self, server: Server) -> None:
        speed_test_output = self.gateway.get_speed_test_result(server.server_id)
        parsed_output = self.parser.parse_output(json_output=speed_test_output)
        LOGGER.debug(
            f"Speed test results: {server.server_name}",
            extra=parsed_output.to_dict(),
        )
        self.repository.save_speed_test_output(speed_test_output=parsed_output)

    def log_internet_connection_for_multiple_servers(self, servers: list[Server]) -> None:
        for server in servers:
            self.log_internet_connection_for_single_server(server=server)

    @staticmethod
    def build():
        return InternetConnectionLogService(
            gateway=SpeedTestGateway(),
            parser=SpeedTestParser(),
            repository=SpeedTestJsonRepository(),
        )
