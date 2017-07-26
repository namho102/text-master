from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()

def lematizer(topic):
    # with open(topic + '.txt', 'r') as f:
    with open('text/' + topic + '.txt', 'r') as f:
        text = f.read().decode('utf-8').encode("ascii", "ignore")

        tokens = text.split()

        text = " ".join([wordnet_lemmatizer.lemmatize(token) for token in tokens])

        # new_text = wordnet_lemmatizer.lemmatize(text)
        # print new_text

        text = text.encode('ascii', 'ignore')
        out = open('new_text/' + topic + '.txt', 'w')
        out.write(text)

topics = ['tech', 'sport', 'entertainment', 'business', 'society']
for topic in topics:
    lematizer(topic)

