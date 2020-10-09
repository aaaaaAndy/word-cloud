#!/usr/bin/env python3

from os import path
from PIL import Image
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator

regexp = '\w[\w\d\.]+'
font_path = r'assets/fonts/msyh.ttf'
ROOT_PATH = path.dirname(__file__)
word_path = path.join(ROOT_PATH, 'assets/word.txt')
mask_path = path.join(ROOT_PATH, 'assets/car.png')
output_path = path.join(ROOT_PATH, 'output.png')

mask = np.array(Image.open(mask_path))
color_func = ImageColorGenerator(mask)
txt = open(word_path, 'r').read().split('\n')

wc = WordCloud(
    mask=mask,
    margin=10,
    scale=1.5,
    width=4000,
    height=2000,
    regexp=regexp,
    repeat=True,
    collocations=True,
    prefer_horizontal=1,
    font_path=font_path,
    relative_scaling=0.3,
    background_color='white'
)

wc.generate('+'.join(txt))

wc.recolor(color_func=color_func)

wc.to_file(output_path)

print('generate over!')
