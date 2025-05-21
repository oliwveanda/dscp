"""
This script is for experiment tracking and testing only.
Models used in production should be accessed through the API.
"""

from pathlib import Path

from ai.evaluation.plot_predictions import plot_all_models
from ai.models.predictor import (
    train_linear_model,
    train_random_forest_model,
    train_xgboost_model,
)
from ai.models.save_model import save_model
from ai.preprocessing.features import (
    add_lag_features,
    add_time_features,
    split_train_test,
)
from ai.preprocessing.prepare_pm25 import preprocess_pm25
from ai.preprocessing.timeseries_utils import resample_to_6_months


def run_linear_model(train_df, test_df):
    print("\n--- Linear Regression Model ---")
    results = train_linear_model(train_df, test_df)
    print(f"MAE:  {results['mae']:.4f}")
    print(f"RMSE: {results['rmse']:.4f}")
    print(results["test_df"])

    # Save the best model
    save_model(results["model"], Path("ai/models/linear_model.joblib"))
    return results


def run_xgb_model(train_df, test_df):
    print("\n--- XGBoost Model ---")
    results = train_xgboost_model(train_df, test_df)
    print(f"MAE:  {results['mae']:.4f}")
    print(f"RMSE: {results['rmse']:.4f}")
    print(results["test_df"])
    return results


def run_rf_model(train_df, test_df):
    print("\n--- Random Forest Model ---")
    results = train_random_forest_model(train_df, test_df)
    print(f"MAE:  {results['mae']:.4f}")
    print(f"RMSE: {results['rmse']:.4f}")
    print(results["test_df"])
    return results


def main():
    # Step 1: Preprocess
    csv_path = Path("ai/data/raw/air_quality.csv")
    df = preprocess_pm25(csv_path)
    df = resample_to_6_months(df)
    df = add_lag_features(df)
    df = add_time_features(df)
    train_df, test_df = split_train_test(df)

    # Step 2: Train models
    linreg_results = run_linear_model(train_df, test_df)
    xgb_results = run_xgb_model(train_df, test_df)
    rf_results = run_rf_model(train_df, test_df)

    # Step 3: Plot comparison
    plot_all_models(
        linreg_results["test_df"],
        xgb_results["test_df"],
        rf_results["test_df"]
    )


if __name__ == "__main__":
    main()
