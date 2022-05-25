#!/usr/bin/env python
# coding: utf-8

# # 10. Practical session: Tei and Beautiful Soup
# 
# TEI alleen met BS want ElementTree kan niet goed omgaan met de spatie (&nbsp)
# 
# Opletten: teis kunnen erg verschillen van opmaak 
# (voorbeeld van een TEI waarin de text in een p staat of in een l). 
# Het is dus altijd goed om een check te doen welke elementen je nodig hebt om de juiste gegevens
# te verzamelen.
# TEis van eenzelfde soort (bijv een dichter) zijn doorgaans gelijk, maar dubbelcheck kan nooit kwaad 
# 
# 
# Opdracht: import bS en laad de file in
# 
# ```
# from bs4 import BeautifulSoup    
# 
# with open("xml-workshop/data/tei.xml", encoding='utf8') as f:
#     root = BeautifulSoup(f, 'xml')
# ```
# 
# 
# Opdracht: bekijk de structuur
# 
# ```
# root
# ```
# 
# Opdracht: Dit tei bestand is va een boek. In welke elementen zit de tekst van deze boeken?
# En zittn ze als waarde of als attribuut
# 
# Antwoord: content zit in title, head, l en p. 
# 
# Er zijn erg veel elementen, dus een optie zou zijn om alle content van de gehele xml uit te printen. 
# Dit kan je doen met door 
# 
# ```
# root.text
# ```
# 
# Een nadeel van deze methodes is dat je ook allerhande metadata meekrijgt die je waarschijnlijk niet bij je boek content wil hebbenm 
# 
# Opdracht: zijn er manieren om de tekst op een logische  manier in te delen ?
# Antwoord: je zou het bijv per chapter kunnen doen. 
# 
# ## Tekst indelen in hoofdstukken
# 
# Je kan door de root itereren en alle elementen met div verzamelen die als type chapter hebben. 
# Vervolgens kan je van deze divs alle content printen met .text.
# 
# Opdracht: maak een for loop door de divs en print van alle divs met type chapter de content uit
# 
# Antwoord: 
# 
# ```
# for div in root.find_all('div'):
#     if div.get('type') == 'chapter':
#         print(div.text)
# ```
# 
# Hij print nu nog steeds alles als 1 lap onder elkaar zonder onderscheiding. Je kan onderscheid 
# maken door een counter te maken en dan voor elke chapter 'chapter [nr]' te zetten. Na elke div 
# verhoog je de counter met 1
# 
# ```
# counter = 1
# 
# for div in root.find_all('div'):
#     if div.get('type') == 'chapter':
#         print("chapter " + str(counter))
#         print(div.text)
#         counter += 1
# ```
# 
# Om het overzichtelijke te maken, kun je de hoofdstukken los opslaan als txt bestand,
# of een csv maken met alle hoofstukken in een eigen rij.
# 
# Opdracht: sla de hoofdstukken op als text 
# 
# Antwoord:
# ```counter = 1
# 
# for div in root.find_all('div'):
#     if div.get('type') == 'chapter':
#         chapter = "chapter_" + str(counter)
#         with open(f"{chapter}.txt", "w", encoding="utf-8") as text_file:
#             text_file.write(div.text)
#             counter += 1
# ```
# 
# Opdracht: Je kan het ook opslaan als een csv. Welke stappen waren daarvoor het handigst?
# 
# Antwoord: opslaan als lijst, dan die omzetten naar df. Dan saven
# 
# Opdracht: Stop chapter en content in lijst
# Antwoord
# ```
# chapter_list = []
# counter = 1
# 
# for div in root.find_all('div'):
#     if div.get('type') == 'chapter':
#         chapter = "chapter_" + str(counter)
#         content = div.text
#         chapter_list.append([chapter, content])
#         counter += 1
# ```
# 
# Opdracht: maak een df
# 
# Antwoord:
# 
# ```
# import pandas as pd
# book = pd.DataFrame(chapter_list , columns = (['chapter', 'content']))
# ```
# 
# DF tonen
# 
# ```
# book
# ```
# 
# Poems extraheren
# 
# Opdracht: kijk welke elementn je nodig hebt om poems eruit te halen
# 
# Antwoord: lg met type poems
# 
# Opdracht: print alle poems uit
# 
# Antwoord: 
# ```
# for div in root.find_all('lg'):
#     if div.get('type') == 'poem':
#         print(div.text)
# ```
# 
# Sla alle poems op als los tekstbestand met nummering
# 
# ```
# counter = 1
# 
# for div in root.find_all('lg'):
#     if div.get('type') == 'poem':
#         poem = "poem_" + str(counter)
#         with open(f"{poem}.txt", "w", encoding="utf-8") as text_file:
#             text_file.write(div.text)
#             counter += 1
# ```
# 
# Opdracht: ska op als csv
# 
# ```
# poem_list = []
# counter = 1
# 
# for div in root.find_all('lg'):
#     if div.get('type') == 'poem':
#         poem = "poem_" + str(counter)
#         content = div.text
#         poem_list.append([poem, content])
#         counter += 1
# 
# import pandas as pd
# poems = pd.DataFrame(poem_list , columns = (['poem', 'content']))
# 
# poems.to_csv('poems.csv')
# ```
