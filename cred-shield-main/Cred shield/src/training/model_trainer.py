from src.training.data_loader import DataLoader
from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments
from typing import Any
import wandb

class ModelTrainer:
    def __init__(self, model_name: str = "roberta-base"):
        self.model_name = model_name
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.data_loader = DataLoader()

    def train(self, train_dataset: Any, val_dataset: Any, config: dict):
        training_args = TrainingArguments(
            output_dir=config.get("output_dir", "./results"),
            num_train_epochs=config.get("epochs", 3),
            per_device_train_batch_size=config.get("batch_size", 8),
            evaluation_strategy="epoch",
            logging_dir="./logs",
            report_to=["wandb"]
        )
        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=val_dataset
        )
        trainer.train()
        return trainer
