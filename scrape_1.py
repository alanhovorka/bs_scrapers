from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://pythonscraping.com/pages/page1.html")
bs=BeautifulSoup(html)
#print(bs) #These all print the same thing
#print(bs.h1)
#print(bs.html.body.h1)
#print(bs.body.h1)
#print(bs.html.h1)
#get_text()stips the tags, leaving only the text
#print(bs.title.get_text())
#print(bs.div.get_text())
#print(bs.body)
