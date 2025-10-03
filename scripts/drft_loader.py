"""
drft_loader.py

Helper script to load the DRFT dataset into a pandas DataFrame.
"""

import pandas as pd
from pathlib import Path

def load_drft_dataset(path: str = "DRFT_dataset.xlsx") -> pd.DataFrame:
    """
    Load the DRFT dataset from an Excel file and return it as a pandas DataFrame.

    Parameters
    ----------
    path : str, optional
        Path to the DRFT dataset (.xlsx). Default assumes the file
        is in the repository root as '4-DRFT_dataset.xlsx'.

    Returns
    -------
    pd.DataFrame
        DataFrame containing the DRFT dataset.
    """
    dataset_path = Path(path)
    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {dataset_path}. "
            "Make sure the file exists or provide the correct path."
        )

    df = pd.read_excel(dataset_path)
    return df


if __name__ == "__main__":
    # Example usage
    df = load_drft_dataset()
    print("DRFT dataset loaded successfully!")
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print(df.head())
