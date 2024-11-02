from textblob import TextBlob
import spacy

nlp = spacy.load("en_core_web_sm")

def analyze_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.3:
        return "positive"
    elif polarity < -0.3:
        return "negative"
    else:
        return "neutral"
