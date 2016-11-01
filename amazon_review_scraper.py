from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("https://www.amazon.com/Introduction-Computing-Programming-Python-4th/product-reviews/0134025547/ref=cm_cr_dp_see_all_summary?ie=UTF8&reviewerType=all_reviews&showViewpoints=1&sortBy=helpful")
soup=BeautifulSoup(html)
div=soup.find('div',{"id":"cm_cr-review_list"})
for tag in div:
    reviews=soup.find("span",{"class":"a-size-base review-text"}) #.text
    stars=soup.find("i",{"class":"a-icon a-icon-star a-star-5 review-rating"}) #.text
    print(reviews.getText())
    print(stars.getText(),"\n")
