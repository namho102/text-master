import sys 
from string import ascii_lowercase 
import codecs
reload(sys)  
sys.setdefaultencoding('utf8')

import re
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize
from nltk import pos_tag
from nltk import FreqDist
#for a in list(ascii_lowercase): print ('\''+ a+'\',')
stopwords = set(stopwords.words('english'))
stopwords.update([',','.','?','!','}','(',')',']','[','=','|','*','0','.',':',';','@','^','%','$','+','_','-','9','8','7','6','1','2','3','4','5','*'])
#stopwords.update(list(ascii_lowercase))


num_classes=5
paths = ['MLDocs/wireless.txt','MLDocs/cryptography.txt','MLDocs/opinionmining.txt','MLDocs/wireless.txt','MLDocs/robotics.txt','MLDocs/dat.txt']

files = ['MLDocs/wireless1.txt','MLDocs/cryptography1.txt','MLDocs/wireless1.txt','MLDocs/robotics1.txt','MLDocs/dat1.txt']

#creates empty dictionary for each class
dictlist = [dict() for x in range(num_classes)]
remove_list=[] #contains all the words to be removed
for i in range(num_classes):
    with codecs.open(paths[i],'r',encoding='utf8') as file:
        text1 = file.read()
    text1 = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", text1)
    taggedlist = pos_tag(text1) #pos taggin of text to remove proper nouns, determiners, pronouns, etc.
    for w in taggedlist:
        if w[1]=='PRP' or w[1] == 'DT' or w[1]=='CC' or w[1]=='PRP$' or w[1]=='NNP'or w[1]=='NNPS' or w[1]=='RB'or w[1]=='IN'or w[1]=='MD'or w[1]=='WP'or w[1]=='WP$'or w[1]=='WRB'or w[1]=='WDT':
            text1 = text1.replace(" "+w[0]+" ","")
            if w[0] not in remove_list:
                remove_list.append(w[0]) 
    tokens = word_tokenize(text1)
    tokens = [x.encode('UTF8') for x in tokens]
    #removing stopwords from text
    tokens = [ w for w in tokens if w not in stopwords]
    #stemming the text
    stemmer = SnowballStemmer("english",ignore_stopwords=True)
    newtext = [ w for w in tokens if w not in stopwords]
    newtext = [ stemmer.stem(w) for w in newtext ]
    #files that contain the preprocessed text
    f = open(files[i],'a+')
    # if string contains numbers or characters, do not add to the text
    for item in newtext:
        if item.isalpha() and len(item) > 2 and item not in remove_list :
            f.write("%s " % item)
