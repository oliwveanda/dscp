# Air Quality Analysis - Data Science Capstone Project

## Problem Statement

Air pollution is one of the most significant environmental threats to urban populations. While everyone is exposed, pollutant emissions, levels of exposure, and population vulnerability vary significantly across neighborhoods. Exposure to common air pollutants has been linked to respiratory and cardiovascular diseases, cancers, and premature deaths. This project aims to analyze air quality data collected from New York City to better understand pollution trends, identify potential health risks, and predict...

## Objectives

### Knowledge Discovery

- Identify daily and seasonal patterns in pollutant concentrations (e.g., higher PM2.5 levels in winter due to heating).
- Determine which pollutants show the strongest correlation with temperature or humidity.
- Investigate whether specific pollutants, like NO₂, show recurring daily peaks (e.g., during rush hour).
- Identify the combination of factors that lead to 'very unhealthy' AQI days.
- Analyze ozone levels for cyclical patterns detectable through time-series models.

### Predictive Modeling

- Develop models for forecasting PM2.5 levels using historical weather data.
- Expose trained model through a FastAPI REST endpoint.

## Data Description

- Type: Time series, tabular data
- Volume: Approximately 20,000 samples
- Source: Air quality surveillance data collected from New York City
- Link: [Air Quality Dataset](https://catalog.data.gov/dataset/air-quality)

## Methodology

1. Data Preprocessing: Cleaning, formatting, and handling missing values.
2. Feature Engineering: Creating lag features and cyclical date encodings.
3. Model Training: Training multiple models (Linear Regression, XGBoost, Random Forest) and selecting the best.
4. API Development: Serving predictions through a versioned FastAPI endpoint.
5. Dockerization: Packaging the app using Docker for cross-platform deployment.
6. Authentication: Securing the endpoint via an API key header.
7. Logging: Logging all activity to `logs/api.log`.
8. Testing: Automated endpoint validation using pytest.
9. Deployment: Live hosting on Render with Docker.

## Deployment

- 🔗 Live API: [https://dscp-kskv.onrender.com/v1/predict/predict](https://dscp-kskv.onrender.com/v1/predict/predict)
- 🔐 Requires header: `x-api-key: your-api-key`

## Usage

### Local Development

```bash
poetry install
uvicorn backend.main:app --reload
```

### Docker

```bash
docker build -t pm25-api .
docker run --env-file .env -p 8000:8000 pm25-api
```

### Example Request

```bash
curl -X POST https://dscp-kskv.onrender.com/v1/predict/predict \
  -H "Content-Type: application/json" \
  -H "x-api-key: your-api-key" \
  -d '{
        "pm25_lag_1": 8.5,
        "pm25_lag_2": 8.2,
        "pm25_lag_3": 9.0,
        "year": 2024,
        "month": 6
      }'
```

## Expected Outcomes

- Seasonal and temporal analysis of pollution patterns.
- Accurate model for forecasting PM2.5 concentrations.
- Dockerized, authenticated, and tested prediction API.

## Acknowledgments

This project utilizes data provided by New York City's air quality surveillance initiative, available on [Data.gov](https://catalog.data.gov/dataset/air-quality).