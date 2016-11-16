from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests # pip install or: https://github.com/kennethreitz/requests
import csv

#This scraper pulls down election results from the 2012 gubernational elections in Indiana

html = urlopen("http://www.in.gov/apps/sos/election/general/general2012?page=district&countyID=-1&officeID=37&districtID=938&candidate=")
soup = BeautifulSoup(html, "html.parser")

gov_results = []
table2 = soup.find_all('table')[1]
for tr in table2.find_all('tr')[5:]:
    gov_results.append(tr.text.split())
#print(gov_results)
header=["County","Gregg","Boneham","Pence","Harris","Precincts","Turnout"]
with open('election_results.csv', 'w', newline='') as outfile:
    file = csv.writer(outfile, delimiter=',')
    file.writerow(header)
    file.writerows(gov_results)



