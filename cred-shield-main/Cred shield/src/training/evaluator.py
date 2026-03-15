from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
from typing import Any, Dict
import numpy as np

class ModelEvaluator:
    def __init__(self):
        pass

    def evaluate(self, y_true: Any, y_pred: Any) -> Dict[str, float]:
        return {
            "accuracy": accuracy_score(y_true, y_pred),
            "precision": precision_score(y_true, y_pred, average="binary"),
            "recall": recall_score(y_true, y_pred, average="binary"),
            "f1": f1_score(y_true, y_pred, average="binary"),
            "roc_auc": roc_auc_score(y_true, y_pred),
        }

    def confusion(self, y_true: Any, y_pred: Any) -> np.ndarray:
        return confusion_matrix(y_true, y_pred)
