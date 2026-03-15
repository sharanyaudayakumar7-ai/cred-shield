import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from typing import List, Dict, Any

class AITextClassifier:
    def __init__(self, model_name: str = "roberta-base", device: str = None):
        self.model_name = model_name
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name).to(self.device)

    def preprocess(self, text: str) -> Dict[str, Any]:
        return self.tokenizer(text, truncation=True, padding=True, return_tensors="pt")

    def predict(self, text: str) -> Dict[str, float]:
        inputs = self.preprocess(text)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        return {"ai_score": float(probs[0][1]), "human_score": float(probs[0][0])}

    def batch_predict(self, texts: List[str]) -> List[Dict[str, float]]:
        results = []
        for text in texts:
            results.append(self.predict(text))
        return results
