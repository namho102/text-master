from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud

d = path.dirname(__file__)

with open('stop-word-list.txt') as f:
    content = f.readlines()

stop_words = [x.strip() for x in content]

def text_to_cloud(topic):
    # Read the whole text.
    text = open(path.join(d, '../after_removing_duplicate_lines/'  + topic + '.txt')).read()
    wc = WordCloud(max_words=3000, width=1366, height=768, stopwords=stop_words)
    wc.generate(text)
    wc.to_file(path.join(d, topic + ".png"))


text_to_cloud('tech')