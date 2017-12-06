from bs4 import BeautifulSoup
import requests

URL = "https://www.theguardian.com/sport?page=%d"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
file = open('theguardian.txt', 'a')


for i in range(50, 60):
    print URL %i
    r = requests.get(URL % i, headers = headers)
    # print r.text
    soup = BeautifulSoup(r.text, 'lxml')

    for link in soup.select('.fc-item__content a'):
        link = link.get('href')

        if not (link.startswith('https://www.theguardian.com/sport/live')
                or link.startswith('https://www.theguardian.com/sport/gallery')
                or link.startswith('https://www.theguardian.com/football/gallery')
                or link.startswith('https://www.theguardian.com/sport/blog/live')
                or link.startswith('https://www.theguardian.com/football/live')
                or link.startswith('https://www.theguardian.com/sport/video')
                or link.startswith('https://www.theguardian.com/politics')
                or link.startswith('https://www.theguardian.com/uk-news')
                or link.startswith('https://www.theguardian.com/football/video')
                or link.startswith('https://www.theguardian.com/football/audio')
                or link.startswith('https://www.theguardian.com/football/blog/audio')
                or link.startswith('https://www.theguardian.com/artanddesign')
                or link.startswith('https://www.theguardian.com/football/ng-interactive')):
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



