import numpy as np

class WordGenerator:
    def __init__(self, word_list_file):
        with open(word_list_file, encoding='utf8') as f:
            chars = f.read().strip().split()
        print(len(chars))
        self.chars = chars

    def generate(self):
        return np.random.choice(self.chars)
