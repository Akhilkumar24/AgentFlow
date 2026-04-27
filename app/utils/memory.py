import json
import os
from app.utils.logger import setup_logger

logger = setup_logger("utils.memory")

class AgentMemory:
    def __init__(self, file_path="memory.json"):
        self.file_path = file_path
        self.data = self._load()

    def _load(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save(self, key, value):
        self.data[key] = value
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f, indent=2)

    def get(self, key):
        return self.data.get(key)

    def clear(self):
        self.data = {}
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
