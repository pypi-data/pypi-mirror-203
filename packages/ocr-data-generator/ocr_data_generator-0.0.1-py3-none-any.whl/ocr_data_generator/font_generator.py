import glob, os
import numpy as np
randint = np.random.randint
from PIL import ImageFont

class FontGenerator:
    def __init__(self, font_dir):
        self.min_font_size=20
        self.max_font_size=50
        self.font_dir = font_dir
        self.font_path_list=glob.glob(font_dir+"/*.ttf")
        self.font_path_list+=glob.glob(font_dir+"/*.ttc")
        print('fonts', len(self.font_path_list))
        self.font_cache = {}

    def get_random_font(self):
        font_path=np.random.choice(self.font_path_list)
        font_name = os.path.basename(font_path)
        font_size = randint(self.min_font_size,self.max_font_size)
        font = self.get_font(font_name, font_size)

        return font, font_name, font_size

    def get_font(self, font_name, font_size):
        font_name = os.path.basename(font_name)
        key = f'{font_name}-{font_size}'
        if key in self.font_cache:
            return self.font_cache[key]
        else:
            font_path = os.path.join(self.font_dir, font_name)
            font = ImageFont.truetype(font_path, size=font_size, index=0, encoding="utf-8")
            self.font_cache[key] = font
        return font