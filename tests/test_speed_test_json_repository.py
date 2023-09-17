import pytest

from src.config import MAIN_DIR
from src.speed_test_json_repository import SpeedTestJsonRepository
from src.speed_test_parser import SpeedTestParsedOutput


@pytest.fixture
def test_repository():
    repository = SpeedTestJsonRepository
    repository._FILES_PATH = f"{MAIN_DIR}/tests/test_file.json"
    return repository


def _clean_test_file(test_repository):
    test_repository._save_dict_to_current_file({"logs": []})
    assert len(test_repository._get_current_file()["logs"]) == 0


def test_json_repository_save(test_repository):
    _clean_test_file(test_repository)
    output = SpeedTestParsedOutput(
        date="2023-09-05T01:42:17Z",
        ping_latency=13.024,
        ping_latency_low=12.147,
        ping_latency_high=14.853,
        download_bandwidth=19.42,
        download_jitter=93.982,
        upload_bandwidth=4.83,
        upload_jitter=88.716,
        isp="Super Argentina",
        server_id=58819,
        server_host="st-cordoba-coe1.cablevisionfibertel.com.ar",
        server_name="Telecom Personal",
        result_id="ce5c402f-8f2b-4628-ac37-2c62634cbe55",
        result_url="https://www.speedtest.net/result/c/ce5c402f-8f2b-4628-ac37-2c62634cbe55",
    )

    saved = test_repository.save_speed_test_output(speed_test_output=output)
    assert saved


def test_json_repository_update_and_not_override(test_repository):
    _clean_test_file(test_repository)
    output = SpeedTestParsedOutput(
        date="2023-09-05T01:42:17Z",
        ping_latency=13.024,
        ping_latency_low=12.147,
        ping_latency_high=14.853,
        download_bandwidth=19.42,
        download_jitter=93.982,
        upload_bandwidth=4.83,
        upload_jitter=88.716,
        isp="Super Argentina",
        server_id=58819,
        server_host="st-cordoba-coe1.cablevisionfibertel.com.ar",
        server_name="Telecom Personal",
        result_id="ce5c402f-8f2b-4628-ac37-2c62634cbe55",
        result_url="https://www.speedtest.net/result/c/ce5c402f-8f2b-4628-ac37-2c62634cbe55",
    )
    test_repository.save_speed_test_output(speed_test_output=output)

    output = SpeedTestParsedOutput(
        date="2023-09-05T01:42:17Z",
        ping_latency=13.024,
        ping_latency_low=12.147,
        ping_latency_high=14.853,
        download_bandwidth=19.42,
        download_jitter=93.982,
        upload_bandwidth=4.83,
        upload_jitter=88.716,
        isp="Super Argentina",
        server_id=58819,
        server_host="st-cordoba-coe1.cablevisionfibertel.com.ar",
        server_name="Telecom Personal",
        result_id="ce5c402f-8f2b-4628-ac37-2c62634cbe55",
        result_url="https://www.speedtest.net/result/c/ce5c402f-8f2b-4628-ac37-2c62634cbe55",
    )

    test_repository.save_speed_test_output(speed_test_output=output)

    assert len(test_repository._get_current_file()["logs"]) == 2
