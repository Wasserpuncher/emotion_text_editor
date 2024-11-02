def suggest_alternatives(text, emotion):
    if emotion == "negative":
        return ["Consider using softer words", "Maybe rephrase to sound more optimistic"]
    elif emotion == "positive":
        return ["Perhaps add some grounding words", "Keep a balanced tone if needed"]
    else:
        return ["Neutral tone detected; no adjustments necessary"]
