#as3:/usr/local/lib/python2.7/site-packages# cat sitecustomize.py
# encoding=utf8  
import math
import pyPdf
import sys 
from string import ascii_lowercase 
import codecs
reload(sys)  
sys.setdefaultencoding('utf8')
import re
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize
from nltk import pos_tag
from nltk import FreqDist

#input from user

test_num=0
test_num = input( "Input the number of Research articles to be classified:")
testpaths = []
for i in range (test_num):
    test=str(raw_input("Enter path:"))
    testpaths.append(test)
####################################Pre processing Test Data #####################################################
stopwords = set(stopwords.words('english'))
stopwords.update([',','.','?','!','}','(',')',']','[','=','|','*','0','.',':',';','@','^','%','$','+','_','-','9','8','7','6','1','2','3','4','5','*'])


num_classes=5

for i in range(test_num):
    with codecs.open(testpaths[i],'r',encoding='utf8') as file:
        text1 = file.read()
 
    text1 = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", text1)
    taggedlist = pos_tag(text1)
    for w in taggedlist:
        if w[1]=='PRP' or w[1] == 'DT' or w[1]=='CC':
            text1 = text1.replace(" "+w[0]+" ","")
    tokens = word_tokenize(text1)
    tokens = [x.encode('UTF8') for x in tokens]
    tokens = [ w for w in tokens if w not in stopwords]
    stemmer = SnowballStemmer("english",ignore_stopwords=True)
    mynewtext = [ w for w in tokens if w not in stopwords]
    mynewtext = [ stemmer.stem(w) for w in mynewtext ]
    f = open(str(i)+'.txt','a+')
    for item in mynewtext:
        f.write("%s " % item)
    print "test data processed"
#############################################################################################################

classes = ['Opinion Mining','Robotics','Data Mining','Wireless Networks' , 'Cryptography']
paths = ['MLDocs/opinionmining1.txt','MLDocs/robotics1.txt','MLDocs/dat1.txt','MLDocs/wireless1.txt','MLDocs/cryptography1.txt']

############################ Loading Training Data ###########################################################
trainingData = []
vocab =[]
text1 = []
for i in range(num_classes):
    f = open(paths[i],'r')
    t = f.read()
    text1.append(t)
    trainingData.append(t.split())

vectorizer = CountVectorizer(analyzer="word", tokenizer=None, preprocessor= None,stop_words='english',max_features=5000)
trani_data_features = vectorizer.fit_transform(text1)
vocab = vectorizer.get_feature_names()

vocab = [x.encode('UTF8') for x in vocab]

dictlist = [dict() for x in range(num_classes)]

for i in range(num_classes): 
    n=0.0
    fd = FreqDist(trainingData[i])
    for w in fd:
        n+= fd[w]
    for w in vocab:
        dictlist[i][w]= (fd[w]+1)/(n + len(vocab))
###############################################################################################################

max=0


for i in range (test_num):
    initial_prob = 0
    p = [ initial_prob,initial_prob,initial_prob,initial_prob,initial_prob]
    try:
        f=open(str(i)+'.txt')
    except IOError:
        print 'cannot open', testpaths[i] , 'Article Skipped.'
        continue
    text1 = f.read()
    mynewtext = text1.split()
    n=0.0
    fd = FreqDist(mynewtext)

    for j in range(num_classes):
        for w in fd:
            if w in vocab:
                p[j] += math.log(dictlist[j][w],10)
                if p[j]==0 :
                    break
                if p[j]==float('inf') :
                    break

    Result = -1
    max=-9999999999999999
   
    for j in range(num_classes):
        print p[j]
        if max<=p[j]:
            max=p[j]
            Result=j                    

    print testpaths[i] ,'----->' , classes[Result]
