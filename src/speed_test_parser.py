import decimal
from decimal import Decimal
from dataclasses import dataclass, asdict
from typing import Dict


@dataclass
class SpeedTestParsedOutput:
    date: str = ''
    ping_latency: float = 0
    ping_latency_low: float = 0
    ping_latency_high: float = 0
    download_bandwidth: float = 0
    download_jitter: float = 0
    upload_bandwidth: float = 0
    upload_jitter: float = 0
    isp: str = ''
    server_id: int = 0
    server_host: str = ''
    server_name: str = ''
    result_id: str = ''
    result_url: str = ''

    def to_dict(self) -> Dict:
        return asdict(self)


class SpeedTestParser:
    @classmethod
    def parse_output(cls, json_output: Dict) -> SpeedTestParsedOutput:
        server_info = json_output["server"]
        result_info = json_output["result"]

        parsed_output = SpeedTestParsedOutput(
            date=json_output['timestamp'],
            server_id=server_info["id"],
            server_host=server_info["host"],
            server_name=server_info["name"],
            result_id=result_info["id"],
            result_url=result_info["url"],
            isp=json_output['isp'],
        )

        download_info = json_output["download"]
        parsed_output.download_bandwidth = cls._from_bytes_to_megabytes(download_info['bandwidth'])
        parsed_output.download_jitter = download_info['latency']['jitter']

        upload_info = json_output["upload"]
        parsed_output.upload_bandwidth = cls._from_bytes_to_megabytes(upload_info['bandwidth'])
        parsed_output.upload_jitter = upload_info['latency']['jitter']

        ping_info = json_output["ping"]
        parsed_output.ping_latency = ping_info['latency']
        parsed_output.ping_latency_low = ping_info['low']
        parsed_output.ping_latency_high = ping_info['high']

        return parsed_output

    @staticmethod
    def _from_bytes_to_megabytes(megabits: float) -> float:
        decimal_bytes = Decimal(str(megabits))
        decimal_bits = decimal_bytes * Decimal('8')
        bits_to_megabits_multiplier = Decimal(str((10**-6)))
        decimal_megabits = decimal_bits * bits_to_megabits_multiplier
        rounded_megabits = decimal_megabits.quantize(Decimal('.01'), rounding=decimal.ROUND_DOWN)
        return float(rounded_megabits)



