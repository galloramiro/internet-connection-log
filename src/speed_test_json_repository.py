import json
from typing import Dict

from src import SpeedTestParsedOutput
from src.config import LOGGER, FILES_DIR


class SpeedTestJsonRepository:
    _FILES_PATH = f"{FILES_DIR}/internet_logs.json"

    @classmethod
    def save_speed_test_output(cls, speed_test_output: SpeedTestParsedOutput) -> bool:
        try:
            dict_output = speed_test_output.to_dict()
            LOGGER.debug("Start saveing process", extra={"speed_test_output": dict_output})

            LOGGER.debug("Obtaining current file")
            current_file = cls._get_current_file()

            LOGGER.debug("Updating current file", extra={"current_file_lenght": len(current_file)})
            current_file["logs"].append(dict_output)

            LOGGER.debug("Saving new file", extra={"current_file_lenght": len(current_file)})
            cls._save_dict_to_current_file(current_file)
            return True
        except Exception as exc:
            LOGGER.error(f"Failed to update file {str(exc)}")
            return False

    @classmethod
    def _get_current_file(cls) -> Dict:
        with open(cls._FILES_PATH, "r") as file_to_read:
            current_file = json.load(file_to_read)
        return current_file

    @classmethod
    def _save_dict_to_current_file(cls, dict_to_save: Dict):
        with open(cls._FILES_PATH, "w") as file_to_update:
            json.dump(dict_to_save, file_to_update, indent=4)
        return True
