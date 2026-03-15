import nltk
import numpy as np
from collections import Counter
from typing import List, Dict, Any

class LanguagePatternAnalyzer:
    def __init__(self):
        pass

    def sentence_structure(self, text: str) -> Dict[str, Any]:
        sentences = nltk.sent_tokenize(text)
        lengths = [len(nltk.word_tokenize(s)) for s in sentences]
        return {"num_sentences": len(sentences), "avg_sentence_length": np.mean(lengths)}

    def repetitive_phrases(self, text: str) -> Dict[str, Any]:
        words = nltk.word_tokenize(text)
        freq = Counter(words)
        repetitive = {w: c for w, c in freq.items() if c > 5}
        return {"repetitive_phrases": repetitive}

    def vocabulary_diversity(self, text: str) -> float:
        words = nltk.word_tokenize(text)
        return len(set(words)) / (len(words) + 1e-6)

    def unnatural_transitions(self, text: str) -> float:
        # Placeholder for transition analysis
        return 0.0

    def punctuation_patterns(self, text: str) -> Dict[str, int]:
        punctuations = Counter([c for c in text if c in ".,!?;:"])
        return dict(punctuations)

    def formal_robotic_language(self, text: str) -> float:
        # Placeholder for formality analysis
        return 0.0

    def ngram_analysis(self, text: str, n: int = 2) -> Dict[str, int]:
        words = nltk.word_tokenize(text)
        ngrams = nltk.ngrams(words, n)
        freq = Counter(ngrams)
        return {"ngram_freq": freq}
