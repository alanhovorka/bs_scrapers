import requests
from bs4 import BeautifulSoup
#scrapes Ball State's website for URL's and title changes
def links(max_pages):
        page = 1
        while page <= max_pages:
                url = 'http://cms.bsu.edu/sitemap'
                source_code = requests.get(url)
                pt = source_code.text
                soup = BeautifulSoup(pt, "html.parser")
                for link in soup.find_all('a'):
                        try:
                                href = link.get('href')
                                href2 = 'http://cms.bsu.edu' + link.get('href')
                                #print(href)
                                print(href2)
                                #get_data(href)
                        except:
                                continue
                for link in soup.find_all('title'):
                        head = link.get('title')
                        #print(head)
                page += 1

#Need a function to gather page meta data and the urls

def get_data(data_url):
        source_code = requests.get(data_url)
        pt = source_code.text
        soup = BeautifulSoup(pt, "html.parser")
        for link in soup.find_all("a"):
                try:
                         href = link.get('href') #build the full version of the link
                except:
                        continue

links(1)
