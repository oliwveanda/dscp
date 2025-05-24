from typing import Tuple

import numpy as np
import pandas as pd


def add_lag_features(df: pd.DataFrame, lags: int = 3) -> pd.DataFrame:
    """
    Add lagged PM2.5 values (e.g., t-1, t-2, t-3).

    Args:
        df (pd.DataFrame): Input DataFrame with 'date' and 'pm25'
        lags (int): Number of lag features to add

    Returns:
        pd.DataFrame: With additional lag columns
    """
    for i in range(1, lags + 1):
        df[f"pm25_lag_{i}"] = df["pm25"].shift(i)
    return df.dropna().reset_index(drop=True)


def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add date-related features for seasonality modeling.

    Args:
        df (pd.DataFrame): Must contain a 'date' column

    Returns:
        pd.DataFrame: With year, month, and seasonal encodings
    """
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["sin_month"] = np.sin(2 * np.pi * df["month"] / 12)
    df["cos_month"] = np.cos(2 * np.pi * df["month"] / 12)
    return df


def split_train_test(df: pd.DataFrame, test_size: int = 4) -> Tuple[pd.DataFrame, pd.DataFrame]: # noqa
    """
    Split data into train and test based on time (not randomly).

    Args:
        df (pd.DataFrame): Input DataFrame
        test_size (int): Number of periods to use for testing

    Returns:
        Tuple: (train_df, test_df)
    """
    return df.iloc[:-test_size], df.iloc[-test_size:]
