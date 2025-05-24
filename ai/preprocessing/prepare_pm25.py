from pathlib import Path

import pandas as pd


def load_raw_data(csv_path: Path) -> pd.DataFrame:
    """Load the raw air quality CSV file."""
    return pd.read_csv(csv_path)


def filter_pm25_data(df: pd.DataFrame) -> pd.DataFrame:
    """Filter only rows where Name contains fine particles (PM 2.5)."""
    return df[df["Name"].str.lower().str.contains("fine particles")].copy()


def pick_top_location(df: pd.DataFrame) -> str:
    """Return the location with the most PM2.5 measurements."""
    return df["Geo Place Name"].value_counts().idxmax()


def prepare_time_series(df: pd.DataFrame, location: str) -> pd.DataFrame:
    """
    Extract and prepare time series data for the given location.
    Groups by Start_Date and averages values if duplicates exist.
    """
    df = df[df["Geo Place Name"] == location].copy()
    df["Start_Date"] = pd.to_datetime(df["Start_Date"], errors="coerce")
    ts_df = df.groupby("Start_Date")["Data Value"].mean().reset_index()
    ts_df.columns = ["date", "pm25"]
    return ts_df.sort_values("date").reset_index(drop=True)


def preprocess_pm25(csv_path: Path) -> pd.DataFrame:
    """Main function to load, filter, and prepare the PM2.5 time series."""
    df = load_raw_data(csv_path)
    df = filter_pm25_data(df)
    location = pick_top_location(df)
    ts_df = prepare_time_series(df, location)
    return ts_df
