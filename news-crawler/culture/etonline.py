from bs4 import BeautifulSoup
import requests

URL = "http://www.etonline.com/news/?page=%d"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
file = open('etonline_.txt', 'a')


for i in range(1, 10):
    print URL %i
    r = requests.get(URL % i, headers = headers)
    # print r.text
    soup = BeautifulSoup(r.text, 'lxml')

    for link in soup.select('.title a'):
        link =  "http://www.etonline.com" + link.get('href')
        print link
        article = requests.get(link, headers=headers)
        article_soup = BeautifulSoup(article.text, 'lxml')
        para = article_soup.select('#Story_Content')[0].select('.story-txt')
        for p in para:
            text = p.getText()
            if ('WATCH' not in text and 'NEWS' not in text and 'RELATED' not in text):
                text = text.encode('utf-8').strip()
                file.write('\n')
                file.write(text)




