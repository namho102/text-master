from nltk.tokenize import word_tokenize
from collections import Counter
import en


all_words = []
with open('words.txt') as f:
    content = f.readlines()

all_words = [x.strip() for x in content]

# print(all_words[:10])
# print(len(words))

file = open('text/tech_.txt', 'r')
text = file.read().decode('utf-8')

# word_list = word_tokenize(text)
topic_word = text.lower().replace('.', " ").split()
# topic_word = [en.noun.singular(word) for word in topic_word]
# print(len(topic_word))
# print(len(set(topic_word)))

file = open('new_words.txt', 'a')

new_words = []
words_set = sorted(set(topic_word))


# new_words = set(words_set) - set(all_words)
# new_words = set(words_set + all_words)
new_words = words_set
# print(len(new_words))

word_count = Counter(topic_word)
word_count = dict(word_count.items())

word_fre = []

for word in sorted(new_words):
    if word_count[word] > 10 and word.isalpha():
        word_fre.append({'word': word, 'count': word_count[word]})
        file.write('\n')
        file.write(word.encode('utf-8'))

for pair in sorted(word_fre, key=lambda k: k['count']) :
    print pair
# for word in words_set:
#     if word not in all_words:
#         new_words.append(word)
#         # file.write('\n')
#         # file.write(word.encode('utf-8'))

# print(len(new_words))
# for pair in Counter(topic_word).most_common(100):
#     print pair

# wordfreq = []
# for w in wordlist:
#     wordfreq.append(wordlist.count(w))

# print("String\n" + out +"\n")
# print("List\n" + str(wordlist) + "\n")
# print("Frequencies\n" + str(wordfreq) + "\n")
# print("Pairs\n" + str(zip(wordlist, wordfreq)))