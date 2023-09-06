from src import SpeedTestGateway


def test_speed_test_gateway_get_speed_test_result():
    """This would be a expected output:
    {
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
            "isVpn": false,
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
            "persisted": true,
        },
    }

    """
    json_output = SpeedTestGateway.get_speed_test_result(server_id=58819)

    expected_first_level_keys = [
        "type",
        "timestamp",
        "ping",
        "download",
        "upload",
        "isp",
        "interface",
        "server",
        "result",
    ]
    first_level_keys = list(json_output.keys())
    assert first_level_keys == expected_first_level_keys

    ping_expected_keys = ["jitter", "latency", "low", "high"]
    ping_keys = list(json_output["ping"].keys())
    assert ping_keys == ping_expected_keys

    download_keys = list(json_output["download"].keys())
    download_expected_keys = ["bandwidth", "bytes", "elapsed", "latency"]
    assert download_keys == download_expected_keys

    upload_keys = list(json_output["upload"].keys())
    upload_expected_keys = ["bandwidth", "bytes", "elapsed", "latency"]
    assert upload_keys == upload_expected_keys

    server_keys = list(json_output["server"].keys())
    server_expected_keys = ["id", "host", "port", "name", "location", "country", "ip"]
    assert server_keys == server_expected_keys
