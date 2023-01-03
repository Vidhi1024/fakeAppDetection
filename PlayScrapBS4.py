#working!:)

import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/apps"

c = requests.get(url)
hc = c.content
# print(hc)
# i = c.text
soup = BeautifulSoup(hc, 'html.parser')
print(soup.prettify)
print(c.text)
u = soup('')
print(u)
title = soup.title
print(title)