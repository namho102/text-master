from bs4 import BeautifulSoup
import requests

r  = requests.get("https://techcrunch.com/2017/06/08/confirmed-verizon-will-cut-15-of-aol-yahoo-staff-after-merger-closes/")

soup = BeautifulSoup(r.text, 'lxml')

# for link in soup.find_all('a'):
#     print(link.get('href'))

print(soup.select('.article-entry')[0].text)    