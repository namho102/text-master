from bs4 import BeautifulSoup
import requests

r  = requests.get("https://techcrunch.com/2017/06/08/confirmed-verizon-will-cut-15-of-aol-yahoo-staff-after-merger-closes/")

soup = BeautifulSoup(r.text, 'lxml')

# for link in soup.find_all('a'):
#     print(link.get('href'))

text = soup.select('.article-entry')[0].text
text = text.encode('utf-8').strip()

file = open('techcrunch1.txt', 'a')

file.write(text)