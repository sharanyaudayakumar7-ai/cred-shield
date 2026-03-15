import argparse
from src.training.evaluator import ModelEvaluator
from src.models.ai_classifier import AITextClassifier

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate AI Detection Model")
    parser.add_argument("--model", type=str, required=True)
    parser.add_argument("--test_data", type=str, required=True)
    args = parser.parse_args()

    clf = AITextClassifier(model_name=args.model)
    # Placeholder: load test data and run evaluation
    print("Evaluation complete.")
