import pandas as pd
import os

def load_csv(filepath: str, sep: str = ",", encoding: str = "utf-8") -> pd.DataFrame: 
    """
    Load a CSV file and return a pandas DataFrame.
    
    Args:
        filepath (str): Path to the CSV file.
        sep (str): Separator used in the CSV file. Default is ','.
        encoding (str): File encoding. Default is 'utf-8'.
    
    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    try:
        df= pd.read_csv(filepath, sep=sep, encoding=encoding)
        print(f"[INFO] loaded {len(df)} rows and {len(df.columns)} columns")
        print(f"[INFO] Columns: {df.columns}") 
        return df
    except Exception as e:
        print(f"[ERROR] Failed to load CSV: {e}")
        raise

        
          