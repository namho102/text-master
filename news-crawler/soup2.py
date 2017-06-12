from bs4 import BeautifulSoup
import requests


URL = "https://techcrunch.com/page/%d"

# r  = requests.get("https://techcrunch.com/page/2")



for i in range(1, 3):
    r = requests.get(URL % i)
    soup = BeautifulSoup(r.text, 'lxml')
    for link in soup.select('.post-title a'):
        print(link.get('href'))
