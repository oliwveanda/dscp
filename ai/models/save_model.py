from pathlib import Path

import joblib


def save_model(model, path: Path):
    """
    Save the trained model to disk using joblib.

    Args:
        model: Trained model object
        path (Path): Path to save the model
    """
    joblib.dump(model, path)
    print(f"Model saved to {path}")


def load_model(path: Path):
    """
    Load a saved model from disk.

    Args:
        path (Path): Path to the saved model

    Returns:
        Loaded model
    """
    return joblib.load(path)
