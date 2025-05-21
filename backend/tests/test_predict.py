from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_predict_valid_input():
    response = client.post("/v1/predict/predict", json={
        "pm25_lag_1": 8.5,
        "pm25_lag_2": 8.2,
        "pm25_lag_3": 9.0,
        "year": 2024,
        "month": 6,
        "sin_month": 0.5,
        "cos_month": 0.87
    })
    assert response.status_code == 200
    json_data = response.json()
    assert "predicted_pm25" in json_data
    assert isinstance(json_data["predicted_pm25"], float)


def test_predict_invalid_input():
    response = client.post("/v1/predict/predict", json={
        "pm25_lag_1": "bad",  # invalid type
        "pm25_lag_2": 8.2,
        "pm25_lag_3": 9.0,
        "year": 2024,
        "month": 6,
        "sin_month": 0.5,
        "cos_month": 0.87
    })
    assert response.status_code == 422
