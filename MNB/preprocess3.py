
from ftfy import fix_text, fix_encoding

def clean_text(topic_name):
    with open('text/' + topic_name + '.txt', 'r') as file:
        text = file.read()

        text = fix_encoding(fix_text(text))

        out = open('text/' + topic_name + '_.txt', 'w')
        out.write(text)

topics = ['tech', 'sport', 'entertainment', 'business', 'society']
for topic in topics:
    clean_text(topic)
