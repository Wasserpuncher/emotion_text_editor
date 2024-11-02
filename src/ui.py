class TextEditorUI:
    def get_text(self):
        print("Enter your text below (type 'END' to finish):")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)
        return "\n".join(lines)
