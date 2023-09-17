import subprocess
from dataclasses import dataclass
from typing import Dict
import json

from src.config import LOGGER


@dataclass
class Server:
    server_name: str
    server_id: int


class SpeedTestGateway:
    @classmethod
    def get_speed_test_result(cls, server_id: int) -> Dict:
        command = [
            "speedtest",
            "--format=json-pretty",
            "--progress=no",
            "--accept-license",
            "--accept-gdpr",
            f"--server-id={server_id}",
        ]
        try:
            console_output = subprocess.check_output(command, timeout=180)
            return cls.parse_json(console_output=console_output)
        except subprocess.CalledProcessError as exc:
            LOGGER.error("Process error", extra={"server_id": server_id, "exc": str(exc)})
        except subprocess.TimeoutExpired:
            LOGGER.error("Time out error", extra={"server_id": server_id})

    @staticmethod
    def parse_json(console_output: bytes) -> Dict:
        try:
            return json.loads(console_output)
        except ValueError:
            raise subprocess.CalledProcessError
