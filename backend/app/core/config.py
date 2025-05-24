import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


class Settings:
    MODEL_PATH: Path = Path("ai/models/linear_model.joblib")
    API_KEY: str = os.getenv("API_KEY", "default_key")
    LOG_DIR: Path = Path("logs")
    LOG_APP_NAME: str = "pm25-api"


settings = Settings()
