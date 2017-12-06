from bs4 import BeautifulSoup
import requests

URL = "http://uk.reuters.com/news/archive/worldNews?view=page&page=%d&pageSize=20"
file = open('reuters_world_.txt', 'a')

for i in range(55, 70):
    print URL %i
    r = requests.get(URL % i)
    # print r.text
    soup = BeautifulSoup(r.text, 'lxml')

    for link in soup.select('.module-content .story-content a'):
        link = 'http://uk.reuters.com' + link.get('href')
        print link
        article = requests.get(link)
        article_soup = BeautifulSoup(article.text, 'lxml')
        para = article_soup.select('.ArticleBody_body_2ECha')[0].find_all('p')
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



