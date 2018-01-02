from bs4 import BeautifulSoup
import requests

URL = "https://www.axs.com/tag/Sports?page=%d"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

file = open('axs.txt', 'a')


for i in range(1, 5):
    print URL % i
    r = requests.get(URL % i, headers = headers)

    soup = BeautifulSoup(r.text, 'lxml')
    print soup
    for link in soup.select('#recent-articles-body > ul h3 > a'):

    	#recent-articles-body > ul > li:nth-child(1) > div > div > h3 > a
        link = link.get('href')
        print link
        article = requests.get(link)
        article_soup = BeautifulSoup(article.text, 'lxml')
        print article_soup
        print(article_soup.select('#article-copy'))
        para = article_soup.select('#article-copy')[0].find_all('p')

        for p in para:
            text = p.getText()
            text = text.encode('utf-8').strip()
            file.write('\n')
            file.write(text)

        file.write('\n!!!@@@$$$\n')     



