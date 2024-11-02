import unittest
from src.suggestions import suggest_alternatives

class TestSuggestions(unittest.TestCase):
    def test_suggestions_for_positive(self):
        suggestions = suggest_alternatives("Good job!", "positive")
        self.assertTrue(len(suggestions) > 0)

    def test_suggestions_for_negative(self):
        suggestions = suggest_alternatives("I am unhappy", "negative")
        self.assertTrue(len(suggestions) > 0)

if __name__ == '__main__':
    unittest.main()
