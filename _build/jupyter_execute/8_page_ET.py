#!/usr/bin/env python
# coding: utf-8

# # 8. Practical session: Page and Elementree
# 
# Steps:
# 
# - Import package and load file
# - Examine structure
# - Print the content with reading order
# 
# ### Import package and load the file
# 
# ```{admonition} Exercise
# :class: attention
# Import the ElemenTree package and load the XML file into your Notebook. 
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# 	import xml.etree.ElementTree as ET	
# 	tree = ET.parse('data/page.xml')
# 	root = tree.getroot()
# ``` 
# 
# ### Examine the structure of the file
# 
# In order to extract the wanted information from the file, we have to examine the structure.
# 
# ```{admonition} Exercise
# :class: attention
# Print the file in your Notebook or look at the file in you webpage, either way you preffer. 
# ```

# In[1]:


import xml.etree.ElementTree as ET	
tree = ET.parse('data/page.xml')
root = tree.getroot()
print(ET.tostring(root, encoding='utf8').decode('utf8'))


# We want to be able to extract the text. Therefore, we need to know in which element the content is stored, and whether this is as a value of the tags or as an attributes value. 
# 
# Oefening: zijn er namespaces waar op gelet moet worden? Zo ja, hoe kunnen we die declaren (twee manieren)
# 
# 
# ```{admonition} Exercise
# :class: attention
# Look at the XML structure, how is the content stored?
# ```
# ```{admonition} Solution
# :class: tip, dropdown
# The content is stored in an element called 'Unicode'. 
# ``` 
# 
# Most page XML files contain a reading order. This reading order guides the user through the file and indicates what the right order of all text elements is. 
# To determine the correct reading order, we need three clues. 
# 
# ```{admonition} Exercise
# :class: attention
# What information do we need to correctly display the reading order?
# ```
# ```{admonition} Solution
# :class: tip, dropdown
# - The id attribute of each TextRegion element
# - The OrderedGroup id for each TextRegion
# - The index of each region
# ``` 
# 
# Now that we know how the file is structured, we can start extracting the output
# 
# ### Extracting the content and reading order
# 
# 
# -- Opdracht: content staat in Unicode, extract the content. Let op eventuele namespaces!!!
# 
# ```
# for newspaper in root.findall('.//ns0:Unicode', ns):
#     print(book.text)
# ```
# 
# -- nu hebben we de tekst maar deze staat niet in de goede volgorde, dus we willen region
# ding toevoegen
# Opdracht: waar moet je op letten?
# Antwoord: content is value tussen de tags, id is attribute
# 
# ```
# for newspaper in root.findall('.//ns0:TextRegion', ns):
#     regionid = newspaper.get('id')
#     for content in newspaper.findall('.//ns0:Unicode', ns):
#         print(regionid)
#         print(content.text)
# ```
# 
# Nu hebben we alles onder elkaar maar het is niet echt leesbaar en het is nu 
# ook niet makkelijk om de juiste leesvolgorde te krijgen. 
# Daarom gaan we het weergeven in een dataframe. 
# Net als in les 4 doen we dat door eerst de boel in een lijst te zetten. 
# 
# Opdracht: sla de input op in een lijst
# 
# ```
# ## Create an empty list
# content_list = []
# 
# for newspaper in root.findall('.//ns0:TextRegion', ns):
#     regionid = newspaper.get('id')
#     for content in newspaper.findall('.//ns0:Unicode', ns):
# 		content = content.text
#     content_list.append([regionid, content])
# ```	
# 
# Lijst tonen: 
# ```
# print(content_list)
# ```
# 
# Nu kunnen we van de lijst makkelijk een dataframe maken met de kolommen region en content
# 
# Opdracht: stop de lijst in een dataframe
# 
# ```
# import pandas as pd
# content_table = pd.DataFrame(content_list, columns = {"Region", "Content"})
# ```
# 
# ```
# print(content_table)
# ``` 
# 
# Als laatste kunnen we de dataframe nu opslaan als csv, waarna het gebruikt kan worden voor verder onderzoek. 
# of om bijv. makkelijk de volgorde aan de readingorder aan te kunnen passen. 
# 
# ```
# content_table.to_csv('page_content.csv')
# ```
# 		
# 
# ### Automatically order in the right way
# 
# Met behulp van bovenstaande bestand en de informatie over de reading order in de csv,
# kan je handmatig de volgorde juist krijgen. 
# 
# Maar dit is natuurlijk best veel werk en vooral bij meerdere bestanden niet handig. 
# 
# Gelukkig is het ook mogelijk om dit geautomatiseerd te doen. 
# 
# Omdat de informatie over de reading order en de indexen op een andere plek opgeslagen is dan 
# de content zelf, doen we dit in drie stappen
# 
# - Uit de xml halen we de drie elementn die de volgorde bepalen en deze slaan op in een Pthon dictionary (lnk naar 
# info ove dict)
# - We halen de content en de region informatie op
# - We koppelen de regio informatie aan de group en index, zodat we dat hebben
# 
# Dit kunnen we vervolgens opslaan in en dataframe en dan makkelijk sorteren. 
# 
# Opdracht: haal de elementen op uit de xml
# 
# ```
# for order in root.findall('.//ns0:ReadingOrder', ns):
#     for group in root.findall('.//ns0:OrderedGroup', ns):
#         groupnr = group.get('id')
#         print(groupnr)
#         for suborder in group.findall('.//ns0:RegionRefIndexed', ns):  
#             region = suborder.get('regionRef')
#             index = suborder.get('index')
#             print(region, index)
# ```
# 
# 
# Voorbeeld: hoe sla je zoiets op in een dict
# 
# ```
# dict_order = {}
# 
# for order in root.findall('.//ns0:ReadingOrder', ns):
#     for group in root.findall('.//ns0:OrderedGroup', ns):
#         groupnr = group.get('id')
#         for suborder in group.findall('.//ns0:RegionRefIndexed', ns):  
#             region = suborder.get('regionRef')
#             index = suborder.get('index')
#             dict_order.setdefault(region,[]).append([groupnr, index])
# ```
# 
# ```
# print(dict_order)
# ```
# 
# 
# 
# De code van de content en region hebben we al gemaakt. Nu gaan we dit samenvoegen doro de waardes
# van de dict te vergelijken met de waarde van de regio id. 
# 
# ```
# for newspaper in root.findall('.//ns0:TextRegion', ns):
#     region = newspaper.get('id')
#     groupvalues = dict_order[region]
#     group = groupvalues[0][0]
#     index = groupvalues[0][1]
#     for content in newspaper.findall('.//ns0:Unicode', ns):
#         content = content.text
#     print(group, region, index, content)
# ```
# 
# Opdracht: Pas bovestaande code aan zodat hij alle relevante informatie in een ljst opslaat
# 
# ```
# content_list = []
# 
# for newspaper in root.findall('.//ns0:TextRegion', ns):
#     region = newspaper.get('id')
#     groupvalues = dict_order[region]
#     group = groupvalues[0][0]
#     index = groupvalues[0][1]
#     for content in newspaper.findall('.//ns0:Unicode', ns):
#         content = content.text
#     content_list.append([group, index, region, content])
# ```
# 
# 
# 
# Opdracht: sla de lijst op als df NOTE: let op de volgorde van de input lijst en de kolommen (ookb ij andere lijsten
# dit neerzetten)
# 
# ```
# import pandas as pd
# newspaper_with_order = pd.DataFrame(content_list, columns = ["Group", "Index", "Region", "Content"])  
# ```
# 
# ```
# newspaper_with_order
# ```
# 
# Voorbeeld: volgorde aanpassen
# 
# ```
# newspaper_with_order = newspaper_with_order.sort_values(['Group', 'Index'],
#               ascending = [True, True])
# ```
# 
# ```
# newspaper_with_order
# ```
# 
# 
# Tada, nu klaar.
