from nltk import word_tokenize, sent_tokenize

with open('text.txt', 'r') as file:
    text = file.read().decode('utf-8')

# words = word_tokenize(text)
print  [word_tokenize(t) for t in sent_tokenize(text)]