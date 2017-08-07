from nltk.tokenize import word_tokenize
from collections import Counter
import en

#
# print en.verb.infinitive("wasn't")
# print en.noun.singular("apps")
# print en.sentence.tag("Facebook is so cool")
# print en.is_verb('died')
# print en.is_verb("wasn't")
# print en.is_noun('facebook')
#
# print(en.noun.plural('happiness'))
# print(en.noun.singular('happiness'))
#
# print(en.noun.plural('app'))
# print(en.noun.singular('app'))
#
# print(en.noun.plural('apps'))
# print(en.noun.singular('apps'))
#
# print(en.verb.tense('died'))
# print(en.verb.tense('died'))

string = "Many people died in Winchester after a long interested painful happiness illness"
print(en.sentence.tag(string))

# for pair in en.sentence.tag(string):
#     print(pair[1])
#     if(pair[1].startswith('N')):
#         print(en.noun.singular(pair[0]))
# for word in string.split():
#     if en.is_noun(word):
#         print(en.noun.singular(word))
#     elif en.is_verb(en.verb.infinitive(word)):
#         print(en.verb.infinitive(word))
#     else:
#         print(word)