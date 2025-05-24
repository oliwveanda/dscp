import matplotlib.pyplot as plt
import pandas as pd


def plot_all_models(
    linreg_df: pd.DataFrame,
    xgb_df: pd.DataFrame,
    rf_df: pd.DataFrame
):
    """
    Plot actual vs predicted PM2.5 values side by side for 3 models.

    Args:
        linreg_df (pd.DataFrame): DataFrame with 'date', 'true', 'pred' for Linear Regression # noqa
        xgb_df (pd.DataFrame): DataFrame with 'date', 'true', 'pred' for XGBoost
        rf_df (pd.DataFrame): DataFrame with 'date', 'true', 'pred' for Random Forest
    """
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 5), sharey=True)

    models = [
        ("Linear Regression", linreg_df),
        ("XGBoost Regressor", xgb_df),
        ("Random Forest Regressor", rf_df)
    ]

    for ax, (title, df) in zip(axes, models):
        ax.plot(df["date"], df["true"], marker='o', label="Actual", linewidth=2)
        ax.plot(df["date"], df["pred"], marker='x', label="Predicted", linewidth=2)
        ax.set_title(title)
        ax.set_xlabel("Date")
        ax.grid(True)
        if ax == axes[0]:
            ax.set_ylabel("PM2.5 (µg/m³)")
        ax.legend()

    plt.tight_layout()
    plt.show()
