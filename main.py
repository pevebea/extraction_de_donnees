#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/" # lien du site a scapper
page = requests.get(url) # requete au serveur

soup = BeautifulSoup(page.text, "html.parser")

# recherche par balise/ element
# element_h1 = soup.find_all("h1")
# element =
#  soup.find("p")
print(soup)

# citations = []
# element_citations = soup.find_all("div", class_="quote")
# # print(element_citations)
# for element in element_citations:
#     # extraire le txte de chaque citation
#     texte = element.find("span", class_="text").text
#     print(texte)



authors_names = soup.find_all("div", class_="quote")
# print(authors_names)
for name in authors_names:
    # extraire le txte de chaque citation
    texte = name.find("small", class_="author").text
    print(texte)