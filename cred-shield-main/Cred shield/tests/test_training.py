import pytest
from src.training.data_loader import DataLoader
from src.training.model_trainer import ModelTrainer
from src.training.evaluator import ModelEvaluator
import pandas as pd

def test_data_loader():
    loader = DataLoader()
    df = pd.DataFrame({"text": ["a", "b", "c"]})
    splits = loader.split(df)
    assert "train" in splits and "val" in splits and "test" in splits

def test_model_trainer():
    trainer = ModelTrainer()
    # Placeholder: test trainer instantiation
    assert trainer.model is not None

def test_evaluator():
    evaluator = ModelEvaluator()
    y_true = [0, 1, 1, 0]
    y_pred = [0, 1, 0, 0]
    scores = evaluator.evaluate(y_true, y_pred)
    assert "accuracy" in scores
