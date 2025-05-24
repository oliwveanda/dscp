import math

from fastapi import APIRouter, Depends, HTTPException
import numpy as np

from ai.models.save_model import load_model
from backend.app.api.v1.dependencies.auth import verify_api_key
from backend.app.api.v1.schemas.predict import PredictionInput, PredictionResponse
from backend.app.core.config import settings
from backend.app.core.logger import logger


router = APIRouter()
model = load_model(settings.MODEL_PATH)


@router.post("/predict", response_model=PredictionResponse)
def predict_pm25(data: PredictionInput, _: str = Depends(verify_api_key)):
    logger.info("New /predict request received.")
    logger.debug(f"Request data: {data.model_dump()}")

    try:
        sin_month = math.sin(2 * math.pi * data.month / 12)
        cos_month = math.cos(2 * math.pi * data.month / 12)

        features = np.array([[
            data.pm25_lag_1, data.pm25_lag_2, data.pm25_lag_3,
            data.year, data.month, sin_month, cos_month
        ]])
        prediction = model.predict(features)[0]
        logger.info(f"Prediction successful. PM2.5 = {round(prediction, 2)}")
        return PredictionResponse(predicted_pm25=round(prediction, 2))
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal prediction error")
