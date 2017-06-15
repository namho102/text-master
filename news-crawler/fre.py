import string
from collections import Counter

file = open('techcrunch_.txt', 'r')
text = file.read()
out = text.translate(None, string.punctuation)
# print out

wordlist = out.split()
for pair in Counter(wordlist).most_common(500):
    print pair

# wordfreq = []
# for w in wordlist:
#     wordfreq.append(wordlist.count(w))

# print("String\n" + out +"\n")
# print("List\n" + str(wordlist) + "\n")
# print("Frequencies\n" + str(wordfreq) + "\n")
# print("Pairs\n" + str(zip(wordlist, wordfreq)))