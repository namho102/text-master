from bs4 import BeautifulSoup
import requests

URL = "http://www.bleacherreport.com/mlb/archives/newest/%d"
file = open('bleacherreport.txt', 'a')


for i in range(15, 25):
    print URL % i
    r = requests.get(URL % i)

    soup = BeautifulSoup(r.text, 'lxml')

    for link in soup.select('#archive-results h3 > a'):
        link = 'http://www.bleacherreport.com' + link.get('href')
        print link
        article = requests.get(link)
        article_soup = BeautifulSoup(article.text, 'lxml')
        para = article_soup.select('.contentStream')[0].find_all('p')

        for p in para:
            text = p.getText()
            text = text.encode('utf-8').strip()
            file.write('\n')
            file.write(text)

        file.write('\n!!!@@@$$$\n')     



