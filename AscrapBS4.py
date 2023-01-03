#worked

import requests
from bs4 import BeautifulSoup

url = "https://www.instagram.com/artly.v"

c = requests.get(url)
hc = c.content
# print(hc)
# i = c.text
soup = BeautifulSoup(hc, 'html.parser')
print(soup.prettify)
# print(c.text)
# u = soup('')
# print(u)
# title = soup.title
# print(title)