#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import csv # permet de 

url = "https://quotes.toscrape.com/" # lien du site a scapper
page = requests.get(url) # requete au serveur

soup = BeautifulSoup(page.text, "html.parser")

# recherche par balise/ element
# element_h1 = soup.find_all("h1")
# element =
#  soup.find("p")
# print(soup)

citations = []

author_and_citations = soup.find_all("div", class_="quote")
# print(element_citations)
for element in author_and_citations:
    # extraire le txte de chaque citation
    texte = element.find("span", class_="text").text
    author = element.find("small", class_="author").text
    citations.append({
        "texte": texte,
        "author": author,
    })

# LOGIQUE D'EXTRACTION VERS UN FICHIER CSV
# creation du fichier
with open("citations.csv", "w", encoding = "utf-8", newline = "") as csv_file:
    # Ecrire dans le fichier
    ecriture = csv.writer(csv_file)
    # enregistrement des citations
    for citation in citations:
        ecriture.writerow(citation.values())

# fermeture du fichier 
csv_file.close()