from fastapi import Header, HTTPException

from backend.app.core.config import settings
from backend.app.core.logger import logger


def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != settings.API_KEY:
        logger.warning("Unauthorized access attempt with API key: %s", x_api_key)
        raise HTTPException(status_code=401, detail="Unauthorized")
    logger.info("API key verified successfully")
