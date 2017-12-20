from bs4 import BeautifulSoup
import requests

URL = "http://www.abc.net.au/news/business/articles/?page=%d"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
file = open('abc1.txt', 'a')

for i in range(6, 10):
    print URL %i
    r = requests.get(URL % i, headers = headers)
    # print r.text
    soup = BeautifulSoup(r.text, 'lxml')

    for link in soup.select('h3 a'):
        link = 'http://www.abc.net.au' + link.get('href')

        if ('rural' not in link and 'specials' not in link and 'science' not in link):
            print link
            article = requests.get(link, headers=headers)
            article_soup = BeautifulSoup(article.text, 'lxml')
            para = article_soup.select('.article')[0].find_all('p')
            for p in para:
                if not p.has_attr("class"):
                    text = p.getText()
                    if ('More' not in text and 'stories from' not in text and 'Contact' not in text):
                        text = text.encode('utf-8').strip()
                        file.write('\n')
                        file.write(text)

            file.write('\n!!!@@@$$$\n')            





