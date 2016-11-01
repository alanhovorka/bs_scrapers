from urllib.request import urlopen
from bs4 import BeautifulSoup

isbn=9780134025544
url="http://www.barnesandnoble.com/w/introduction-to-computing-and-programming-in-python-mark-j-guzdial/1121343615?ean"
url_for_isbn=url+str(isbn)
page=urlopen(url_for_isbn)
bs=BeautifulSoup(page)
name=bs.find("h1",{"itemprop":"name"})
price=bs.find("span",{"class":"price"})
print(name.get_text(),price.get_text())
