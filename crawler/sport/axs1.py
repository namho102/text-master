from splinter import Browser
import pandas as pd
# open a browser
browser = Browser('chrome')
browser.visit('https://www.axs.com/tag/Sports?page=1')

link = browser.find_by_css('#recent-articles-body ul h3 a')[0]
print(link)

link.click()