from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

with open('stop-word-list.txt') as f:
    content = f.readlines()

stop_words = [x.strip() for x in content]

# Read the whole text.
text = open(path.join(d, 'tech/gizmodo.txt')).read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
# alice_mask = np.array(Image.open(path.join(d, "alice_mask.png")))

stopwords = set(stop_words)

wc = WordCloud(max_words=3000, width=1366, height=768, stopwords=stopwords)
# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "gizmodo.png"))

