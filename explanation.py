class Explanation:

    def __init__(self) -> None:
        self.explanation_text = ''


    def add(self, text: str) -> None:
        self.explanation_text += text + '\n'

    
    def write_to_file(self, filename: str) -> None:
        with open(filename, 'w') as f:
            f.write(self.explanation_text)