import pytest
from src.utils.text_preprocessor import TextPreprocessor
from src.utils.config import Config
from src.utils.logger import Logger

def test_text_preprocessor():
    pre = TextPreprocessor()
    cleaned = pre.clean_text("Hello, World!")
    assert isinstance(cleaned, str)

def test_config():
    # Placeholder: test config loading
    assert True

def test_logger():
    logger = Logger()
    logger.info("Test log message")
    assert True
