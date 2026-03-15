import pytest
from src.models.ai_classifier import AITextClassifier
from src.models.language_analyzer import LanguagePatternAnalyzer
from src.models.predictability_scorer import PredictabilityScorer
from src.models.variation_analyzer import VariationAnalyzer
from src.detection_engine import CredShieldDetectionEngine

def test_ai_classifier():
    clf = AITextClassifier()
    result = clf.predict("This is a test sentence.")
    assert "ai_score" in result and "human_score" in result

def test_language_analyzer():
    analyzer = LanguagePatternAnalyzer()
    scores = analyzer.sentence_structure("This is a test. Another sentence.")
    assert "num_sentences" in scores

def test_predictability_scorer():
    scorer = PredictabilityScorer()
    perplexity = scorer.perplexity("This is a test sentence.")
    assert perplexity > 0

def test_variation_analyzer():
    analyzer = VariationAnalyzer()
    diversity = analyzer.lexical_diversity(["This is a test.", "Another test."])
    assert diversity > 0

def test_detection_engine():
    engine = CredShieldDetectionEngine()
    result = engine.analyze("This is a test sentence.")
    assert "authenticity_score" in result
