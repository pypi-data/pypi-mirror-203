import numpy as np

class WordGenerator:
    def __init__(self):
        with open('char_std_5990.txt', encoding='utf8') as f:
            chars = f.read().strip().split()
        print(len(chars))
        self.chars = chars

    def generate(self):
        return np.random.choice(self.chars)
