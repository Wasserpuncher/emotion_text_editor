import unittest
from src.text_analyzer import analyze_emotion

class TestTextAnalyzer(unittest.TestCase):
    def test_positive_text(self):
        text = "This is a great day!"
        self.assertEqual(analyze_emotion(text), "positive")
        
    def test_negative_text(self):
        text = "I am feeling very sad."
        self.assertEqual(analyze_emotion(text), "negative")
        
    def test_neutral_text(self):
        text = "It's a normal day."
        self.assertEqual(analyze_emotion(text), "neutral")

if __name__ == '__main__':
    unittest.main()
