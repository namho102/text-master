import string
import re
from ftfy import fix_text, fix_encoding

def clean_text(topic_name):
    with open('text/' + topic_name + '.txt', 'r') as file:
        text = file.read()

        # print(string.punctuation)


        text = fix_encoding(fix_text(text))
        # text = text.replace("–", "")
        # text = text.translate(string.punctuation)


        text = re.sub('''[-[!"#$%&*+,—–/:;()[\]{}<=>?@^_`{|}~]''', ' ', text)
        # print(text)

        out = open('text/' + topic_name + '_.txt', 'w')
        out.write(text)

topics = ['tech', 'sport', 'entertainment', 'business', 'society']
for topic in topics:
    clean_text(topic)

# clean_text('test')