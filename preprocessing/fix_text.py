import re
from ftfy import fix_text, fix_encoding


def clean_text(topic_name):
    with open('after_removing_duplicate_lines/' + topic_name + '.txt', 'r') as file:
        text = file.read()

        text = fix_encoding(fix_text(text))

        text = re.sub('''[-[!"#$%&*+,—–/:;()[\]{}<=>?@^_`{|}~]''', ' ', text)

        out = open('fixed/' + topic_name + '_.txt', 'w')
        out.write(text)


topics = ['business', 'culture', 'society', 'sport', 'tech']
for topic in topics:
    clean_text(topic)
