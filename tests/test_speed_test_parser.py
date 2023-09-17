from src.speed_test_parser import SpeedTestParser


def test_speed_test_parser__from_bytes_to_megabytes():
    megabytes = SpeedTestParser._from_bytes_to_megabytes(megabits=2428001)
    assert megabytes == 19.42


def test_speed_test_parser_parse_output():
    example_output = {
        "type": "result",
        "timestamp": "2023-09-05T01:42:17Z",
        "ping": {"jitter": 1.112, "latency": 13.024, "low": 12.147, "high": 14.853},
        "download": {
            "bandwidth": 2428001,
            "bytes": 16295792,
            "elapsed": 6713,
            "latency": {"iqm": 1025.787, "low": 18.547, "high": 1517.554, "jitter": 93.982},
        },
        "upload": {
            "bandwidth": 604307,
            "bytes": 4270152,
            "elapsed": 7102,
            "latency": {"iqm": 496.438, "low": 36.434, "high": 1241.525, "jitter": 88.716},
        },
        "isp": "Super Argentina",
        "interface": {
            "internalIp": "192.168.0.7",
            "name": "wlp1s0",
            "macAddr": "4C:D5:77:5F:44:4B",
            "isVpn": False,
            "externalIp": "181.118.106.252",
        },
        "server": {
            "id": 58819,
            "host": "st-cordoba-coe1.cablevisionfibertel.com.ar",
            "port": 8080,
            "name": "Telecom Personal",
            "location": "Córdoba",
            "country": "Argentina",
            "ip": "181.9.194.70",
        },
        "result": {
            "id": "ce5c402f-8f2b-4628-ac37-2c62634cbe55",
            "url": "https://www.speedtest.net/result/c/ce5c402f-8f2b-4628-ac37-2c62634cbe55",
            "persisted": True,
        },
    }
    parsed_output = SpeedTestParser.parse_output(json_output=example_output)

    assert parsed_output
