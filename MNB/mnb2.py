import math
import random
from nltk import tokenize

def extract_vocabulary(D):
    list_of_words = []
    for d in D:
        list_of_words += d[0].split(" ")
    return set(list_of_words)

def count_docs(D):
    return len(D)


def count_docs_in_class(D, c):
    cnt = 0
    for d in D:
        if d[1] == c:
            cnt += 1
    return cnt

def concat_docs_in_class(D, c):
    text = ''
    for d in D:
        if d[1] == c:
            text += d[0] + ' '
    return text

def count_tokens_of_term(text, t):
    word_list = text.split()
    return word_list.count(t)

def train(C, D):
    V = extract_vocabulary(D)
    # print V
    N = count_docs(D)
    # print N
    prior = {}
    condprob = {}
    for t in V:
        condprob[t] = {}
    for c in C:

        Nc = count_docs_in_class(D, c)
        # print (Nc, N)
        prior[c] = float(Nc)/N
        text_of_class = concat_docs_in_class(D, c)
        # print text_of_class
        for t in V:
            Tct = count_tokens_of_term(text_of_class, t)
            # print Tct, len(text_of_class.split()), len(V)
            condprob[t][c] = float(Tct + 1)/(len(text_of_class.split()) + len(V))

    # print condprob

    return (V, prior, condprob)


def extract_tokens_from_doc(V, d):
    word_list = []
    for t in d:
        if t in V:
            word_list.append(t)
    return word_list

def apply(C, V, prior, condprob, d):
    W = extract_tokens_from_doc(V, d)
    score = {}
    for c in C:
        # score[c] = math.log(prior[c])
        score[c] = prior[c]
        for t in W:
            score[c] *= condprob[t][c]
            # score[c] += math.log(condprob[t][c])
    return max(score, key=score.get)

def get_topic_list(topic_name):
    with open(topic_name + '.txt','rU') as f:
        raw = f.read().decode('utf-8').encode("ascii", "ignore")
        sentence_list = raw.split('.')
        # sentence_list = tokenize.sent_tokenize(raw)
        # group_sentences = []
        # for s in sentence_list:
        #     group_sentences.append((s, topic_name))
        #
        # return group_sentences
        return [(s, topic_name) for s in sentence_list]

def get_full_list(topics):
    full_list = []
    for topic in topics:
        topic_list = get_topic_list(topic)
        full_list += topic_list

    return full_list

def split_train_test(full_list, size):
    sample = random.sample(full_list, size)
    split_length = int(round(len(sample) * 0.7))
    train_data = sample[0:split_length]
    test_data = sample[split_length:]
    return (train_data, test_data)

if __name__ == "__main__":


    # D = [('Chinese Beijing Chinese', 'yes'), ('Chinese Chinese Shanghai', 'yes'), ('Chinese Macao', 'yes'), ('Tokyo Japan Chinese', 'no')]
    C = ['sport', 'tech']
    full_list = get_full_list(C)
    (D, test) = split_train_test(full_list, 1000)
    print D[:10]

    (V, prior, condprob) = train(C, D)

    # c = apply(C, V, prior, condprob, 'Chinese Chinese Chinese Tokyo Japan')

    print(apply(C, V, prior, condprob, "Yesterday Amazon and Whole Foods ruined a perfectly slow news day on a Friday in June with the announcement that Amazon intends to buy Whole Foods for almost $14 billion"))
    print(apply(C, V, prior, condprob, "Whenever a product is updated, there inevitably are people who grumble about change and wish things had stayed the same"))
    print(apply(C, V, prior, condprob, "He'll sell you solar rooftop tiles to generate electricity, a giant battery to store all that energy and an electric car to suck it up"))
    print(apply(C, V, prior, condprob, "Giroud scored 16 goals last season but started only 11 Premier League matches with manager Arsene Wenger preferring to deploy Alexis Sanchez in a central striking role"))
    print(apply(C, V, prior, condprob, "A bidding war is set to break out as Cristiano Ronaldo's Bernabeu exit beckons"))
    print(apply(C, V, prior, condprob, "Instead there could be two periods of 30 minutes with the clock stopped whenever the ball goes out of play"))
