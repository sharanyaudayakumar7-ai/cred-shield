from src.detection_engine import CredShieldDetectionEngine

if __name__ == "__main__":
    engine = CredShieldDetectionEngine()
    print("Cred Shield AI Detection Demo")
    while True:
        text = input("Enter text (or 'exit' to quit): ")
        if text.lower() == "exit":
            break
        result = engine.analyze(text)
        print("Detection Result:", result)
        print(f"AI Score: {result['ai_scores']['ai_score']:.3f}")
        print(f"Human Score: {result['ai_scores']['human_score']:.3f}")
        print("Language Analysis:")
        print(f"Number of Sentences: {result['language_scores']['structure']['num_sentences']}")
        print(f"Average Sentence Length: {result['language_scores']['structure']['avg_sentence_length']:.2f}")
        print(f"Vocabulary Diversity: {result['language_scores']['vocab_diversity']:.3f}")
        print(f"Punctuation: {result['language_scores']['punctuation']}")
        print("Predictability:")
        print(f"Perplexity: {result['predictability']['perplexity']:.2f}")
        print(f"Response Length: {result['predictability']['response_length']}")
        print("Variation:")