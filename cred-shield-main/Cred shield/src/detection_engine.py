from src.models.ai_classifier import AITextClassifier
from src.models.language_analyzer import LanguagePatternAnalyzer
from src.models.predictability_scorer import PredictabilityScorer
from src.models.variation_analyzer import VariationAnalyzer
from typing import Dict, Any

class CredShieldDetectionEngine:
    def __init__(self, model_name: str = "roberta-base"):
        self.classifier = AITextClassifier(model_name=model_name)
        self.language_analyzer = LanguagePatternAnalyzer()
        self.predictability_scorer = PredictabilityScorer()
        self.variation_analyzer = VariationAnalyzer()

    def analyze(self, text: str) -> Dict[str, Any]:
        ai_scores = self.classifier.predict(text)
        language_scores = {
            "structure": self.language_analyzer.sentence_structure(text),
            "repetitive": self.language_analyzer.repetitive_phrases(text),
            "vocab_diversity": self.language_analyzer.vocabulary_diversity(text),
            "punctuation": self.language_analyzer.punctuation_patterns(text)
        }
        predictability = {
            "perplexity": self.predictability_scorer.perplexity(text),
            "response_length": self.predictability_scorer.response_length(text)
        }
        variation = {
            "lexical_diversity": self.variation_analyzer.lexical_diversity([text])
        }
        # Weighted score (placeholder logic)
        authenticity_score = (
            ai_scores["human_score"] * 0.4 +
            language_scores["vocab_diversity"] * 0.2 +
            (1.0 / (predictability["perplexity"] + 1e-6)) * 0.2 +
            variation["lexical_diversity"] * 0.2
        )
        return {
            "ai_scores": ai_scores,
            "language_scores": language_scores,
            "predictability": predictability,
            "variation": variation,
            "authenticity_score": authenticity_score
        }
