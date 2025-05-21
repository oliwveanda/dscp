from pydantic import BaseModel, Field


class PredictionInput(BaseModel):
    pm25_lag_1: float = Field(..., description="PM2.5 one step before")
    pm25_lag_2: float = Field(..., description="PM2.5 two steps before")
    pm25_lag_3: float = Field(..., description="PM2.5 three steps before")
    year: int = Field(..., description="Year")
    month: int = Field(..., description="Month")
    sin_month: float = Field(..., description="Sine of month")
    cos_month: float = Field(..., description="Cosine of month")


class PredictionResponse(BaseModel):
    predicted_pm25: float
