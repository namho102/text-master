from bs4 import BeautifulSoup
import requests


URL = "https://www.cnet.com/topics/tech-industry/%d"
file = open('cnet.txt', 'a')

# r  = requests.get("https://techcrunch.com/page/2")

for i in xrange(1, 10):
    r = requests.get(URL % i)
    print URL % i
    soup = BeautifulSoup(r.text, 'lxml')

    for link in soup.select('#topicListing .assetBody > a'):
        link = 'https://www.cnet.com' + link.get('href')


        if 'video' not in link and 'pictures' not in link:
            print(link)
            article = requests.get(link)
            article_soup = BeautifulSoup(article.text, 'lxml')
            para = article_soup.select('article')[0].find_all('p')
            for p in para:
                text = p.getText()
                if 'Subscribe:' not in text and 'iTunes' not in text and 'RSS' not in text and 'Download' not in text:
                    text = text.encode('utf-8').strip()
                    file.write('\n')
                    file.write(text)

            file.write('\n!!!@@@$$$\n')   



