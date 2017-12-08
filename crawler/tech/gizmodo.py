from bs4 import BeautifulSoup
import requests


URL = "http://gizmodo.com/tag/science?startIndex=%d"
file = open('gizmodo.txt', 'a')

# r  = requests.get("https://techcrunch.com/page/2")

for i in xrange(6, 10):
    index = i*20
    r = requests.get(URL % index)
    print URL % index
    soup = BeautifulSoup(r.text, 'lxml')

    for link in soup.select('.post-list--pe .headline a'):
        link = link.get('href')
        print(link)

        article = requests.get(link)
        article_soup = BeautifulSoup(article.text, 'lxml')
        para = article_soup.select('.post-content')[0].find_all('p')
        for p in para:
            text = p.getText()
            text = text.encode('utf-8').strip()
            file.write('\n')
            file.write(text)

        file.write('\n!!!@@@$$$\n')   

