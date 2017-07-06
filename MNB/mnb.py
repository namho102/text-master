import math


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

    print condprob

    return (V, prior, condprob)


def extract_tokens_from_doc(V, d):
    return d.split(' ')


def apply(C, V, prior, condprob, d):
    W = extract_tokens_from_doc(V, d)
    score = {}
    for c in C:
        # score[c] = math.log(prior[c])
        score[c] = prior[c]
        for t in W:
            score[c] *= condprob[t][c]
            # score[c] += math.log(condprob[t][c])

    print score

if __name__ == "__main__":
    D = [('Chinese Beijing Chinese', 'yes'), ('Chinese Chinese Shanghai', 'yes'), ('Chinese Macao', 'yes'), ('Tokyo Japan Chinese', 'no')]
    C = ['yes', 'no']

    (V, prior, condprob) = train(C, D)
    apply(C, V, prior, condprob, 'Chinese Chinese Chinese Tokyo Japan')