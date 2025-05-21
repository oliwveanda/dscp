import pandas as pd
import xgboost as xgb

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


def train_linear_model(train_df: pd.DataFrame, test_df: pd.DataFrame):
    """
    Train and evaluate a linear regression model on time series data.

    Args:
        train_df (pd.DataFrame): Training set
        test_df (pd.DataFrame): Testing set

    Returns:
        dict: Evaluation results and predictions
    """
    # Features to use for training
    feature_cols = [col for col in train_df.columns
                    if col.startswith("pm25_lag")
                    or col.startswith("sin_")
                    or col.startswith("cos_")
                    or col in ["month", "year"]]

    X_train = train_df[feature_cols]
    y_train = train_df["pm25"]

    X_test = test_df[feature_cols]
    y_test = test_df["pm25"]

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict
    preds = model.predict(X_test)

    # Evaluation
    mae = mean_absolute_error(y_test, preds)
    rmse = mean_squared_error(y_test, preds) ** 0.5

    # Output
    return {
        "model": model,
        "mae": mae,
        "rmse": rmse,
        "y_true": y_test.values,
        "y_pred": preds,
        "test_df": test_df[["date"]].assign(true=y_test.values, pred=preds)
    }


def train_xgboost_model(train_df: pd.DataFrame, test_df: pd.DataFrame):
    """
    Train and evaluate an XGBoost regressor on time series data.

    Args:
        train_df (pd.DataFrame): Training set
        test_df (pd.DataFrame): Testing set

    Returns:
        dict: Evaluation results and predictions
    """
    feature_cols = [col for col in train_df.columns
                    if col.startswith("pm25_lag")
                    or col.startswith("sin_")
                    or col.startswith("cos_")
                    or col in ["month", "year"]]

    X_train = train_df[feature_cols]
    y_train = train_df["pm25"]

    X_test = test_df[feature_cols]
    y_test = test_df["pm25"]

    model = xgb.XGBRegressor(
        n_estimators=100,
        max_depth=3,
        learning_rate=0.1,
        random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    rmse = mean_squared_error(y_test, preds) ** 0.5

    return {
        "model": model,
        "mae": mae,
        "rmse": rmse,
        "y_true": y_test.values,
        "y_pred": preds,
        "test_df": test_df[["date"]].assign(true=y_test.values, pred=preds)
    }


def train_random_forest_model(train_df: pd.DataFrame, test_df: pd.DataFrame):
    """
    Train and evaluate a Random Forest Regressor on time series data.

    Args:
        train_df (pd.DataFrame): Training set
        test_df (pd.DataFrame): Testing set

    Returns:
        dict: Evaluation results and predictions
    """
    feature_cols = [col for col in train_df.columns
                    if col.startswith("pm25_lag")
                    or col.startswith("sin_")
                    or col.startswith("cos_")
                    or col in ["month", "year"]]

    X_train = train_df[feature_cols]
    y_train = train_df["pm25"]

    X_test = test_df[feature_cols]
    y_test = test_df["pm25"]

    model = RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    rmse = mean_squared_error(y_test, preds) ** 0.5

    return {
        "model": model,
        "mae": mae,
        "rmse": rmse,
        "y_true": y_test.values,
        "y_pred": preds,
        "test_df": test_df[["date"]].assign(true=y_test.values, pred=preds)
    }
