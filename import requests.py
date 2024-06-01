import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://en.wikipedia.org/wiki/Art"
page=requests.get(url)
soup= BeautifulSoup(page.text,"html.parser")
print("Title :- "+str(soup.title.text))
print("\n")
all=soup.find_all("div",class_="vector-body ve-init-mw-desktopArticleTarget-targetContainer")
para=str(soup.find_all('p')[1].text)
print("Paragraph-1 :- "+para)
print("\n")
for link in soup.find_all("a"):
    print("URL in the page :- "+str(link.get("href")))
    print("\n")
total_number_img=len(soup.find_all("img"))
total_number_cap=len(soup.find_all("figcaption"))
for num in range(total_number_img):
    print("Image URL :- "+str(soup.find_all("img")[num].get("src")))
    print("\n")
    if num<total_number_cap:
        print("Caption :- "+str(soup.find_all("figcaption")[num].text))
        print("\n")
    else:
        continue 


