from text_analyzer import analyze_emotion
from suggestions import suggest_alternatives
from ui import TextEditorUI

def main():
    editor = TextEditorUI()
    text = editor.get_text()
    emotion = analyze_emotion(text)
    suggestions = suggest_alternatives(text, emotion)

    print(f"Detected emotion: {emotion}")
    print("Suggested words to adjust tone:")
    for suggestion in suggestions:
        print(suggestion)

if __name__ == "__main__":
    main()
