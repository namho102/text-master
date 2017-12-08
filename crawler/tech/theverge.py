from bs4 import BeautifulSoup
import requests


URL = "https://www.theverge.com/archives/%d"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
file = open('theverge.txt', 'a')


for i in range(40, 55):
    print URL %i
    r = requests.get(URL % i, headers = headers)
    # print r.text
    soup = BeautifulSoup(r.text, 'lxml')


    for link in soup.select('.m-tag-page__content h3 a'):
        link = link.get('href')
        print link
        if not link.startswith('https://live.theverge.com'):
            article = requests.get(link, headers = headers)
            article_soup = BeautifulSoup(article.text, 'lxml')
            para = article_soup.select('.c-entry-content')[0].find_all('p')
            for p in para:
                text = p.getText()
                text = text.encode('utf-8').strip()
                file.write('\n')
                file.write(text)

            file.write('\n!!!@@@$$$\n') 



