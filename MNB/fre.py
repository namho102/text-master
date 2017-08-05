from nltk.tokenize import word_tokenize
from collections import Counter

all_words = []
with open('words.txt') as f:
    content = f.readlines()

all_words = [x.strip() for x in content]

print(all_words[:10])
# print(len(words))

file = open('text/tech_.txt', 'r')
text = file.read().decode('utf-8')

# word_list = word_tokenize(text)
topic_word = text.lower().replace('.', " ").split()

print(len(topic_word))
print(len(set(topic_word)))

file = open('new_words.txt', 'a')

new_words = []
words_set = sorted(set(topic_word))
new_words = set(words_set) - set(all_words)
print(len(new_words))

for word in sorted(new_words):
    file.write('\n')
    file.write(word.encode('utf-8'))
# for word in words_set:
#     if word not in all_words:
#         new_words.append(word)
#         # file.write('\n')
#         # file.write(word.encode('utf-8'))

# print(len(new_words))
# for pair in Counter(word_list).most_common(10):
#     print pair

# wordfreq = []
# for w in wordlist:
#     wordfreq.append(wordlist.count(w))

# print("String\n" + out +"\n")
# print("List\n" + str(wordlist) + "\n")
# print("Frequencies\n" + str(wordfreq) + "\n")
# print("Pairs\n" + str(zip(wordlist, wordfreq)))