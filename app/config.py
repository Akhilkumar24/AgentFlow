import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    MEMORY_FILE = os.getenv("MEMORY_FILE", "memory.json")
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))
    MAX_WORKFLOW_LOOPS = int(os.getenv("MAX_WORKFLOW_LOOPS", 3))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    # Example placeholder if you later connect an LLM API
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

config = Config()
