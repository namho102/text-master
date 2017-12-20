from bs4 import BeautifulSoup
import requests

URL = "http://money.cnn.com/news/briefing/?daysAgo=%d&type=article"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
file = open('cnn1.txt', 'a')

for i in range(50, 60):
    print URL %i
    r = requests.get(URL % i, headers = headers)
    # print r.text
    soup = BeautifulSoup(r.text, 'lxml')
    # jsBriefs > a:nth-child(1)
    for link in soup.select('a.brief'):
        link = link.get('href')

        if ('economy' in link or 'companies' in link or 'smallbusiness' in link or 'investing' in link):
            print link
            article = requests.get(link, headers=headers)
            article_soup = BeautifulSoup(article.text, 'lxml')
            para = article_soup.select('#storycontent')[0].find_all('p')
            for p in para:
                if not p.has_attr("class"):
                    text = p.getText()
                    text = text.encode('utf-8').strip()
                    file.write('\n')
                    file.write(text)

            file.write('\n!!!@@@$$$\n') 




