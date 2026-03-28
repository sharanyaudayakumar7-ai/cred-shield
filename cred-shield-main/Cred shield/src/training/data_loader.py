#import libraries 

import pandas as pd
from datasets import load_dataset
from typing import List, Dict, Any

class DataLoader:
    def __init__(self):
        pass

    def load_csv(self, path: str) -> pd.DataFrame:
        return pd.read_csv(path)

    def load_json(self, path: str) -> pd.DataFrame:
        return pd.read_json(path)

    def load_hf_dataset(self, name: str) -> Any:
        return load_dataset(name)

    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        # Placeholder for preprocessing
        return df

#training data sets 
        def split(self, df: pd.DataFrame, val_ratio: float = 0.2, test_ratio: float = 0.1) -> Dict[str, pd.DataFrame]:
        n = len(df)
        val_size = int(n * val_ratio)
        test_size = int(n * test_ratio)
        train_size = n - val_size - test_size
        train = df.iloc[:train_size]
        val = df.iloc[train_size:train_size+val_size]
        test = df.iloc[train_size+val_size:]
        return {"train": train, "val": val, "test": test}
