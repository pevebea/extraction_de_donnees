import csv
import requests
from bs4 import BeautifulSoup

i = 1
all_citations = []

while True:
    main_url = f"https://quotes.toscrape.com/page/{i}/" # url de la page i, i = un nombre entier
    page = requests.get(main_url)

    soup = BeautifulSoup(page.text, "html.parser")  # recuperationn de la page i
    next = soup.find_all("li", class_ = "next")     # verifie s'il ya une page suivante
    # print(next, i)
    author_and_citations = soup.find_all("div", class_="quote")

    for element in author_and_citations:    # aJOUT DES DONNEES RECUPEREES DANS UNE LISTE PYTHONN
        author = element.find("small", class_ = "author").text
        citation = element.find("span", class_ = "text").text
        all_citations.append({
            "author": author,
            "citation": citation,
        })

    # TANQUE LA PAGE SUIVANTE EST DISPO, INCREMENTER i, SINON CASSER LA BOUCLE
    if next:
        i += 1
    else:
        break

# print(len(all_citations))
# CREATION DU FIIICHIER DANS LE QUEL LES CITATIONS SERONT ENREGISTREES
with open("all_citations.csv", "w", encoding="utf-8", newline = "") as fichier:
    fichier = csv.writer(fichier)
    for citation in all_citations:
        fichier.writerow(citation.values())


