#WIP
import requests
from bs4 import BeautifulSoup
#scrapes Ball State's website for URL's and title changes
def links(max_pages):
                url = 'http://cms.bsu.edu/sitemap'
                source_code = requests.get(url)
                pt = source_code.text
                soup = BeautifulSoup(pt, "html.parser")
                for link in soup.find_all('a'):
                        try:
                                href = link.get('href')
                                href2 = 'http://cms.bsu.edu' + link.get('href')
                                #print(href)
                                #print(href2)
                                #get_data(href)
                        except:
                                continue
                #for link in soup.find_all('head'):
                 #       head = link.get('title')
                  #      print(head)

#Need a function to gather page meta data and the urls
#How do we get it to search for different pages that aren't numbers?
def get_data(data_url):
        source_code = requests.get(data_url)
        pt = source_code.text
        soup = BeautifulSoup(pt, "html.parser")
        for link in soup.find_all("a"):
                try:
                        href = 'http://cms.bsu.edu' + link.get('href')
                        print(href)
                except:
                        continue


links(1)
