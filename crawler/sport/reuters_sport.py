from bs4 import BeautifulSoup
import requests

URL = "http://www.reuters.com/news/archive/sportsNews?view=page&page=%d&pageSize=20"
file = open('reuters_sport1.txt', 'a')


for i in range(15, 30):
    print URL %i
    r = requests.get(URL % i)
    # print r.text
    soup = BeautifulSoup(r.text, 'lxml')

    for link in soup.select('.module-content .story-content a'):
        link = 'http://www.reuters.com' + link.get('href')
        print link
        article = requests.get(link)
        article_soup = BeautifulSoup(article.text, 'lxml')
        para = article_soup.select('.StandardArticleBody_body_1gnLA')[0].find_all('p')
        # print(len(para))
        for i in range(0, len(para) - 1):
            text = para[i].getText()
            text = text.encode('utf-8').strip()
            file.write('\n')
            file.write(text)
        # for p in para:
        #     text = p.getText()
        #     text = text.encode('utf-8').strip()
        #     file.write('\n')
        #     file.write(text)

        file.write('\n!!!@@@$$$\n') 

