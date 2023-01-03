#working but rejected!:(


from bs4 import BeautifulSoup
from urllib.request import urlopen
a="https://www.instagram.com/"
i=0
while i<50:
    handle=input("Enter the username: ")
    page=urlopen(a+handle).read()
    soup=BeautifulSoup(page,"html.parser")
    #print(soup)

    string=soup.find("meta", property="og:description")['content']
    fw=string.split('Followers')[0]
    fg=string.split()[2]
    p=string.split()[4]
    print(string)
    print("Followers=",fw)
    print("Following=",fg)
    print("Posts=",p)
    i=+1