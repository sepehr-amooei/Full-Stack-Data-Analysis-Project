import pandas as pd

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes duplicate rows from the DataFrame.
    """
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print(f"[INFO] Removed {before - after} duplicated rows.")
    return df

def handle_missing_values(df: pd.DataFrame, method: str = "drop", fill_value=None) -> pd.DataFrame:
    """
    Handles missing values in the DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.
        method (str): Method to handle missing values ("drop", "fill").
        fill_value (any): Value to fill if method is "fill".

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    if method == "drop":
        before = len(df)
        df = df.dropna()
        after = len(df)
        print(f"[INFO] Dropped {before - after} rows with missing values.")
    elif method == "fill":
        df = df.fillna(fill_value)
        print(f"[INFO] Filled missing values with {fill_value}")
    else:
        raise ValueError(f"Invalid method: {method}. Use 'drop' or 'fill'.")
    return df

def convert_dtypes(df: pd.DataFrame, dtype_map: dict) -> pd.DataFrame:
    """
    Converts data types of specified columns.

    Args:
        df (pd.DataFrame): Input DataFrame.
        dtype_map (dict): Dictionary mapping columns to target data types.

    Returns:
        pd.DataFrame: DataFrame with converted column types.
    """
    for col, dtype in dtype_map.items():
        try:
            df[col] = df[col].astype(dtype)
            print(f"[INFO] Converted column '{col}' to {dtype}.")
        except Exception as e:
            print(f"[WARNING] Failed to convert column '{col}' to {dtype}: {e}")
    return df

def convert_column_to_datetime(df: pd.DataFrame, col: str, format: str = '%Y-%m-%d') -> pd.DataFrame:
    """
    Converts a column to datetime using a specific format.

    Args:
        df (pd.DataFrame): Input DataFrame.
        col (str): Column name to convert.
        format (str): Date format string (default: '%Y-%m-%d').

    Returns:
        pd.DataFrame: DataFrame with converted datetime column.
    """
    try:
        df[col] = pd.to_datetime(df[col], format=format)
        print(f"[INFO] Converted column '{col}' to datetime with format '{format}'.")
    except Exception as e:
        print(f"[WARNING] Failed to convert '{col}' to datetime: {e}")
    return df

def standardize_text_column(df: pd.DataFrame, columns: list, lowercase: bool = True) -> pd.DataFrame:
    """
    Standardizes text column by converting to lowercase and stripping whitespace.
    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list): List of column names to standardize.
        lowercase: Whether to convert text to lowercase. Default is True.

    """
    for column in columns:
        if column in df.columns:
            if lowercase:
                df[column] = df[column].astype(str).str.lower().str.strip()
            else:
                df[column] = df[column].astype(str).str.strip()
            print(f"[INFO] Standardized text in column '{column}'.")
        else:
            print(f"[WARNING] Column '{column}' not found in DataFrame.")

    return df
            