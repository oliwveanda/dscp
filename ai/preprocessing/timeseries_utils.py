import pandas as pd


def resample_to_6_months(ts_df: pd.DataFrame) -> pd.DataFrame:
    """
    Ensure the time series has a uniform 6-month interval, clearing any missing values.

    Args:
        ts_df (pd.DataFrame): Time series with ['date', 'pm25']

    Returns:
        pd.DataFrame: Regular 6-month series
    """
    # Set datetime index
    ts_df = ts_df.set_index("date").asfreq("6MS")  # Start of every 6th month

    # Interpolate missing values if any
    ts_df["pm25"] = ts_df["pm25"].interpolate(method="linear")

    return ts_df.reset_index()
