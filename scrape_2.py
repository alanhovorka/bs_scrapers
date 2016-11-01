from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs=BeautifulSoup(html)
'''
line=bs.find("span",{"class":"red"})
print(line)

#findAll(tag_name, tag_attributes) -- finds all instances, returns a list
lines=bs.findAll("span",{"class":"red"})
print(lines)
'''
'''
#Loop that gets the names of the source without the html tags
nameList=bs.findAll("span",{"class":"green"})
for name in nameList:
    print(name.get_text())
'''
'''
#Loop for a set of names, no duplicates
nameList=bs.findAll("span",{"class":"green"})
for name in set(nameList):
    print(name.get_text())
'''
'''
#count of times a word or phrase appears
nameList=bs.findAll(text="the prince")
print(len(nameList))
'''
'''
#all of the text in a document, no tags
allText=bs.findAll(id="text")
print(allText[0].get_text())
'''
'''
#include an underscore to get around the use of class in Python
nameList=bs.findAll(class_="green")
for name in nameList:
    print(name.getText())
'''    
#alternate method for the preceeding code
nameList=bs.findAll("", {"class":"green"})
for name in nameList:
    print(name.getText())
