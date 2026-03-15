import re
from typing import List

class TextPreprocessor:
    def __init__(self):
        pass

    def clean_text(self, text: str) -> str:
        text = re.sub(r"[^\w\s]", "", text)
        text = text.lower().strip()
        return text

    def segment_sentences(self, text: str) -> List[str]:
        return re.split(r"[.!?]", text)

    def tokenize(self, text: str) -> List[str]:
        return text.split()

    def remove_noise(self, text: str) -> str:
        # Placeholder for noise removal
        return text

    def standardize(self, text: str) -> str:
        # Placeholder for standardization
        return text
