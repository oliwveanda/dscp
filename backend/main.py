from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ai.models.predictor import AirQualityPredictor

app = FastAPI()

predictor = AirQualityPredictor()

class PredictionRequest(BaseModel):
    temperature: float
    humidity: float

@app.post("/predict")
async def predict_air_quality(data: PredictionRequest):
    try:
        result = predictor.predict(data.temperature, data.humidity)
        return {"PM2.5 Prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to the Air Quality Predictive Model API"}
