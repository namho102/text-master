from bs4 import BeautifulSoup
import requests

URL = "http://www.usmagazine.com/entertainment?page=%d"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
file = open('usmagazine.txt', 'a')


for i in range(2, 10):
    print URL %i
    r = requests.get(URL % i, headers = headers)
    # print r.text
    soup = BeautifulSoup(r.text, 'lxml')

    for link in soup.select('.content-card a'):
        link = link.get('href')
        if 'pictures' not in link:
            print link
            article = requests.get(link, headers=headers)
            article_soup = BeautifulSoup(article.text, 'lxml')
            para = article_soup.select('.article-content')[0].find_all('p')
            for p in para:
                text = p.getText()
                text = text.encode('utf-8').strip()
                file.write('\n')
                file.write(text)

            file.write('\n!!!@@@$$$\n') 



