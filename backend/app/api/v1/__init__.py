from fastapi import APIRouter
from backend.app.api.v1.endpoints.predict import router as predict_router
from backend.app.api.v1.endpoints.predict_geo import router as predict_geo_router

api_router = APIRouter()
api_router.include_router(predict_router, prefix="/predict", tags=["Prediction"])
api_router.include_router(predict_geo_router, prefix="/predict", tags=["Predict"])
