from bs4 import BeautifulSoup
import requests

URL = "https://www.theguardian.com/culture?page=%d"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
file = open('theguardian_.txt', 'a')


for i in range(1, 10):
    print URL %i
    r = requests.get(URL % i, headers = headers)
    # print r.text
    soup = BeautifulSoup(r.text, 'lxml')

    for link in soup.select('.fc-item__content a'):
        link = link.get('href')

        if ('gallery' not in link
                and 'video' not in link
                and 'live' not in link
                and 'audio' not in link
                and 'ng-interactive' not in link
                and 'picture' not in link):
            print link

            article = requests.get(link, headers = headers)
            article_soup = BeautifulSoup(article.text, 'lxml')
            para = article_soup.select('.content__article-body')[0].find_all('p')
            for p in para:
                text = p.getText()
                text = text.encode('utf-8').strip()
                file.write('\n')
                file.write(text)

            file.write('\n!!!@@@$$$\n') 



