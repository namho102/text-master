from bs4 import BeautifulSoup
import requests

URL = "http://www.ibtimes.com/business?page=%d"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
file = open('ibtimes1.txt', 'a')

for i in range(1, 10):
    print URL %i
    r = requests.get(URL % i, headers = headers)
    # print r.text
    soup = BeautifulSoup(r.text, 'lxml')
    # jsBriefs > a:nth-child(1)
    for link in soup.select('.content h3 a'):
        link = "http://www.ibtimes.com" + link.get('href')

        # if ('economy' in link or 'companies' in link or 'smallbusiness' in link or 'investing' in link):
        print link
        article = requests.get(link, headers=headers)
        article_soup = BeautifulSoup(article.text, 'lxml')
        para = article_soup.select('.article-body')[0].find_all('p')
        for p in para:
            if not p.has_attr("class"):
                text = p.getText()
                if ('Copyright Wall' not in p):
                    text = text.encode('utf-8').strip()
                    file.write('\n')
                    file.write(text)

        file.write('\n!!!@@@$$$\n') 




