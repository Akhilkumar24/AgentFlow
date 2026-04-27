import json
import os
from typing import Any, Dict
from app.config import config
from app.utils.logger import setup_logger

logger = setup_logger("memory")

class JSONMemory:
    def __init__(self, file_path: str = config.MEMORY_FILE):
        self.file_path = file_path
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump({}, f)

    def save(self, key: str, value: Any):
        data = self._load_all()
        data[key] = value
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)
        logger.info(f"Saved data for key: {key}")

    def load(self, key: str) -> Any:
        data = self._load_all()
        return data.get(key)

    def update(self, key: str, value: Any):
        data = self._load_all()
        if key in data and isinstance(data[key], dict) and isinstance(value, dict):
            data[key].update(value)
        elif key in data and isinstance(data[key], list) and isinstance(value, list):
             data[key].extend(value)
        else:
            data[key] = value
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)
        logger.info(f"Updated data for key: {key}")

    def _load_all(self) -> Dict[str, Any]:
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            logger.error("Failed to decode JSON memory, returning empty dict.")
            return {}

memory_store = JSONMemory()
