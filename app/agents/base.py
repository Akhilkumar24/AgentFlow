from abc import ABC, abstractmethod
from typing import Any
from app.utils.logger import setup_logger
from tenacity import retry, stop_after_attempt, wait_exponential

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name
        self.logger = setup_logger(f"agent.{name.lower()}")

    @retry(stop=stop_after_attempt(2), wait=wait_exponential(multiplier=1, min=1, max=3))
    def run(self, input_data: Any) -> Any:
        self.logger.info(f"{self.name} started processing.")
        try:
            result = self.process(input_data)
            self.logger.info(f"{self.name} finished processing.")
            return result
        except Exception as e:
            self.logger.error(f"{self.name} failed: {str(e)}")
            raise

    @abstractmethod
    def process(self, input_data: Any) -> Any:
        pass
