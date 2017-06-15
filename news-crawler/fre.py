import string
from collections import Counter

file = open('techcrunch4.txt', 'r')
text = file.read()
out = text.translate(None, string.punctuation)
# print out

wordlist = out.split()
print Counter(wordlist).most_common(200)

# wordfreq = []
# for w in wordlist:
#     wordfreq.append(wordlist.count(w))

# print("String\n" + out +"\n")
# print("List\n" + str(wordlist) + "\n")
# print("Frequencies\n" + str(wordfreq) + "\n")
# print("Pairs\n" + str(zip(wordlist, wordfreq)))