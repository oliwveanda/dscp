from fastapi import APIRouter, Depends
import numpy as np

from ai.models.save_model import load_model
from backend.app.api.v1.dependencies.auth import verify_api_key
from backend.app.api.v1.schemas.predict import PredictionInput, PredictionResponse
from backend.app.core.config import settings


router = APIRouter()
model = load_model(settings.MODEL_PATH)


@router.post("/predict", response_model=PredictionResponse)
def predict_pm25(data: PredictionInput, _: str = Depends(verify_api_key)):
    features = np.array([[  # shape (1, 7)
        data.pm25_lag_1,
        data.pm25_lag_2,
        data.pm25_lag_3,
        data.year,
        data.month,
        data.sin_month,
        data.cos_month
    ]])
    prediction = model.predict(features)[0]
    return PredictionResponse(predicted_pm25=round(prediction, 2))
