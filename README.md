# Air Quality Analysis - Data Science Capstone Project

## Problem Statement

Air pollution is one of the most significant environmental threats to urban populations. While everyone is exposed, pollutant emissions, levels of exposure, and population vulnerability vary significantly across neighborhoods. Exposure to common air pollutants has been linked to respiratory and cardiovascular diseases, cancers, and premature deaths. This project aims to analyze air quality data collected from New York City to better understand pollution trends, identify potential health risks, and predict air quality levels.

## Objectives

### Knowledge Discovery

* Identify daily and seasonal patterns in pollutant concentrations (e.g., higher PM2.5 levels in winter due to heating).
* Determine which pollutants show the strongest correlation with temperature or humidity.
* Investigate whether specific pollutants, like NO₂, show recurring daily peaks (e.g., during rush hour).
* Identify the combination of factors that lead to 'very unhealthy' AQI days.
* Analyze ozone levels for cyclical patterns detectable through time-series models.

### Predictive Modeling

* Develop models for forecasting PM2.5 levels using historical weather data.

## Data Description

* Type: Time series, tabular data
* Volume: Approximately 20,000 samples
* Source: Air quality surveillance data collected from New York City
* Link: [Air Quality Dataset](https://catalog.data.gov/dataset/air-quality)

## Project Motivation

The primary motivation behind this project is to gain insights into urban air pollution and its impact on public health. Understanding the patterns and predictors of air quality will help policymakers, environmental agencies, and public health officials make informed decisions to mitigate health risks associated with poor air quality.

## Methodology

1. Data Preprocessing: Cleaning, formatting, and handling missing values.
2. Exploratory Data Analysis (EDA): Analyzing temporal and spatial variations in pollutant levels.
3. Correlation Analysis: Identifying correlations between pollutants and meteorological factors (temperature, humidity).
4. Time-Series Analysis: Detecting patterns and forecasting using models such as ARIMA or LSTM.
5. Predictive Modeling: Building regression models to predict PM2.5 levels.
6. Model Evaluation: Using metrics like RMSE, MAE, and R-squared to assess model accuracy.
7. Reporting: Summarizing findings and providing actionable insights.

## Expected Outcomes

* Daily and seasonal pollution patterns in New York City.
* Identification of critical factors influencing air quality.
* Predictive models for PM2.5 concentration.
* Comprehensive analysis report including data visualizations and predictive insights.

## Acknowledgments

This project utilizes data provided by New York City's air quality surveillance initiative, available on [Data.gov](https://catalog.data.gov/dataset/air-quality).
