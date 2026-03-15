import argparse
from src.training.data_loader import DataLoader
from src.training.model_trainer import ModelTrainer
from src.training.evaluator import ModelEvaluator

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train AI Detection Model")
    parser.add_argument("--config", type=str, required=True)
    parser.add_argument("--data", type=str, required=True)
    parser.add_argument("--output", type=str, default="./results")
    args = parser.parse_args()

    loader = DataLoader()
    df = loader.load_csv(args.data)
    splits = loader.split(df)
    trainer = ModelTrainer()
    trained = trainer.train(splits["train"], splits["val"], {"output_dir": args.output})
    evaluator = ModelEvaluator()
    # Placeholder: evaluation logic
    print("Training complete.")
