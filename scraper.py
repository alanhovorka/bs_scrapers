import requests
from bs4 import BeautifulSoup

def links(max_pages):
        page = 1
        while page <= max_pages:
                url = 'http://cms.bsu.edu/sitemap'
                source_code = requests.get(url)
                pt = source_code.text
                soup = BeautifulSoup(pt, "html.parser")
                for link in soup.find_all('a'):
                        href = link.get('href')
                        #print(href)
                        #get_data(href)
                for link in soup.find_all('title'):
                        head = link.get('title')
                        print(head)
                page += 1

#Need a function to gather page meta data and the urls

def get_data(data_url):
        source_code = requests.get(data_url)
        pt = source_code.text
        soup = BeautifulSoup(pt, "html.parser")
        for alllinks in soup.find_all("a"):
                print(alllinks.string)
        #for alllinks in soup.find_all("a"):

links(1)
