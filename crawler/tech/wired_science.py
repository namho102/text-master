from bs4 import BeautifulSoup
import requests


URL = "https://www.wired.com/category/science/page/%d"
file = open('wired_science.txt', 'a')

# r  = requests.get("https://techcrunch.com/page/2")

for i in range(10, 20):
    r = requests.get(URL % i)
    print URL % i
    soup = BeautifulSoup(r.text, 'lxml')

    for link in soup.select('.archive-listing-main-component .archive-item-component__info .archive-item-component__link'):
        link = 'https://www.wired.com' + link.get('href')
        print(link)

        article = requests.get(link)
        article_soup = BeautifulSoup(article.text, 'lxml')
        para = article_soup.select('article')[0].find_all('p')
        for p in para:
            text = p.getText()
            text = text.encode('utf-8').strip()
            file.write('\n')
            file.write(text)

        file.write('\n!!!@@@$$$\n') 

