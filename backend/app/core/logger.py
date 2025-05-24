import logging

from backend.app.core.config import settings

settings.LOG_DIR.mkdir(exist_ok=True)

log_file = settings.LOG_DIR / "api.log"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(settings.LOG_APP_NAME)
