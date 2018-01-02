from bs4 import BeautifulSoup
import requests

URL = "http://www.newsweek.com/sports?page=%d"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

file = open('newsweek.txt', 'a')

for i in range(30, 35):
    print URL % i
    r = requests.get(URL % i, headers = headers)

    soup = BeautifulSoup(r.text, 'lxml')
    for link in soup.select('#block-nw-nw-archive div.archive-list h3 a'):
        link = 'http://www.newsweek.com/' + link.get('href')
        print link
        article = requests.get(link)
        article_soup = BeautifulSoup(article.text, 'lxml')

        para = article_soup.select('div.article-content > div.article-body p')

        for p in para:
            text = p.getText()
            if 'by subscribing now' not in text:
	            text = text.encode('utf-8').strip()
	            file.write('\n')
	            file.write(text)

        file.write('\n!!!@@@$$$\n')     



