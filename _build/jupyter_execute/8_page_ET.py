#!/usr/bin/env python
# coding: utf-8

# # 8. Practical session: Page and Elementree
# 
# In this section we will use ElemenTree to extract data from Page format XML files and print this with the reading order. As you should by now be a bit more familiar with Python and handling XML explanations will be a bit more brief. When needed, refer back to previous sections.
# 
# We will follow these steps:
# 
# - Import the package and the Page file;
# - Examine the structure;
# - Extract reading order;
# - Extract the plain text;
# - Print the content with reading order.
# 
# Open a new Jupyter Notebook and type all code examples and code exercises in your Notebook. (see explanation in ET:import)
# 
# ### Import package and load the file
# 
# ```{admonition} Exercise
# :class: attention
# Import the ElemenTree package and load the XML file into your Notebook. 
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```Python
# import xml.etree.ElementTree as ET	
# tree = ET.parse('data/page.xml')
# root = tree.getroot()
# ```
# ```` 
# 
# ### Examine the structure of the file
# 
# In order to extract the required information from the file, we have to examine the structure.
# 
# ```{admonition} Exercise
# :class: attention
# Print the file in your Notebook or look at the file in your browser, either way you prefer. 
# ```

# In[1]:


import xml.etree.ElementTree as ET	
tree = ET.parse('data/page.xml')
root = tree.getroot()
print(ET.tostring(root, encoding='utf8').decode('utf8'))


# The Page XML contains a lot of information that is not the text. Rather they describe something about the location of the text on the scan.
# 
# We want to be able to extract the text. Therefore, we need to know in which element the content is stored, and whether this is as a value of the tags or as an attributes value. 
# 
# ```{admonition} Exercise
# :class: attention
# Remember namespaces? Are there any namespaces in the file that we have to take into account? 
# If there are, how can we declare these?
# Oefening: zijn er namespaces waar op gelet moet worden? Zo ja, hoe kunnen we die declaren (twee manieren)
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# - Yes, there are multiple namespaces to take into account. These are declared in the root of the XML:
# ```XML
# <ns0:PcGts xmlns:ns0="http://schema.primaresearch.org/PAGE/gts/pagecontent/2010-03-19" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
# ```
# - If you remember from section 7, there are two ways of using namespaces:
# 	1. Type the namespace before the element name between curly brackets: {http://schema.ccs-gmbh.com/ALTO}
# 	2. Declare the namespace in elemenTree. This provides Python with a dictionary of the used namespaces, which it can then use.
# ````
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
# Now that we know how the file is structured, we can start extracting the output
# 
# ### Extracting the content and reading order
# 
# 
# ```{admonition} Exercise
# The text content that we wish to extract is stored in the Unicode element. 
# Use Python and ElementTree to extract this content.
# 	*Dont't forget about namespaces!! *
# ```
# 
# 
# ````{admonition} Solution
# :class: tip, dropdown
# The following code should print out all the content.
# ```Python
# for newspaper in root.findall('.//ns0:Unicode', ns):
#     print(book.text)
# ```
# ````
# 
# Now we have all the text content, but it is not in the right order. We need to add the TextRegion id to get the data to print out in the right order. 
# 
# ```{admonition} Exercise
# What should we pay attention to when adding the TextRegion id?
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# The content we are interested in is the value between the tags. However, the TextRegion id is an *attribute*.
# ```
# 
# Expand the code include the TextRegion id and print out the TextRegion id and the content per newpaper. 
# 
# ````{admonition} Solution
# :class: tip, dropdown
# The following code should print out all the content.
# ```Python
# for newspaper in root.findall('.//ns0:TextRegion', ns):
#     regionid = newspaper.get('id')
#     for content in newspaper.findall('.//ns0:Unicode', ns):
#         print(regionid)
#         print(content.text)
# ```
# ````
# 
# Now we have all the data with its corresponding TextRegion id, however it is not very readable. Also, the getting the correct reading other from this printout is not easy.
# So we will put the data into a dataframe. 
# As seen before in section 4 we will first put the whole set into a list.
# 
# ```{admonition} Exercise
# Instead of printing the TextRegion id and content, store it into a list. 
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# The code below should store the  TextRegion id and content into a list.
# ```Python
# ## Create an empty list
# content_list = []
# 
# for newspaper in root.findall('.//ns0:TextRegion', ns):
#     regionid = newspaper.get('id')
#     for content in newspaper.findall('.//ns0:Unicode', ns):
# 		content = content.text
#     content_list.append([regionid, content])
# ```	
# ````
# 
# Let us just peek at the list to see if everything went as expected.
# 
# ```
# print(content_list)
# ```
# 
# Now we can easily make a dataframe using the list we have just created with as column 'region' and 'content'.
# 
# ````{admonition} Exercise
# Make a dataframe from the list we have just created.
# ```{note}}
# Pay attention to the order of the input list and columns!
# ```
# ````
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```Python
# import pandas as pd
# content_table = pd.DataFrame(content_list, columns = {"Region", "Content"})
# ```	
# ````
# 
# As before, check the result to make sure everything went as expected.
# 
# ```
# print(content_table)
# ``` 
# 
# Als laatste kunnen we de dataframe nu opslaan als csv, waarna het gebruikt kan worden voor verder onderzoek. 
# of om bijv. makkelijk de volgorde aan de readingorder aan te kunnen passen. 
# 
# Finally we can now save the dataframe to csv, after which it can be used for further research or manipulation. 
# 
# ```
# content_table.to_csv('page_content.csv')
# ```
# 
# ### Automatically order in the right way
# 
# Using the XML file  and the information about the reading order in the csv file it is possible to order the file in the correct reading order manually. 
# However this is a lot of work and when there are multiple, or very large files this is not the best use of our time. 
# Luckily Python offers us ways to automate this.
# 
# Because the information about the reading order and indexes stored in a different location that the content itself we will go through three steps to get this done. 
# 
# - From the XML we will take three elements that determine te order. These are stored into a Python dictionary [Python dictionaries] 
# - We retrieve the content and region information.
# - We connect the region information to the group and index. 
# 
# This can than be stored in a dataframe and sorted. 
# 
# ```{admonition} Exercise
# Using Python, extract the elements we want from the XML.
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```Python
# for order in root.findall('.//ns0:ReadingOrder', ns):
#     for group in root.findall('.//ns0:OrderedGroup', ns):
#         groupnr = group.get('id')
#         print(groupnr)
#         for suborder in group.findall('.//ns0:RegionRefIndexed', ns):  
#             region = suborder.get('regionRef')
#             index = suborder.get('index')
#             print(region, index)
# ```	
# ````
# 
# 
# Example: how to save the above output to a Python dictionary:
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
# 			dict_order.setdefault(region,[]).append([groupnr, index])
# ```
# 
# Let's print the dictionary to make certain it works.
# 
# ```
# print(dict_order)
# ```
# 
# We have previously made the code to obtain the content and the region from the XML file. Now we will combine this by comparing the values from the dictionary with the value of the TextRegion id.
# 
# ```Python
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
# ```{admonition} Exercise
# Adapt the code above to store all relevant information in a list.
# 
# Don't forget to declare an empty list first.
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```Python
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
# ````
# 
# 
# 
# ````{admonition} Exercise
# Store the list in a dataframe.
# ```{note}}
# Pay attention to the order of the input list and columns!
# ```
# ````
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```Python
# import pandas as pd
# newspaper_with_order = pd.DataFrame(content_list, columns = ["Group", "Index", "Region", "Content"])  
# ```	
# ````
# 
# Check if the result is as expected.
# ```Python
# print(newspaper_with_order)
# ```
# 
# Example: changing the order.
# ```Python
# newspaper_with_order = newspaper_with_order.sort_values(['Group', 'Index'],
#               ascending = [True, True])
# ```
# 
# Print the reordered dataframe.
# ```Python
# print(newspaper_with_order)
# ```
# 
# If everything worked as it was supposed to, the new dataframe should now be ordered by the Group and Index columns.
# Much easier to read, and better structured. Well done!
# 
# Of course, like before this can be used for further analysis, or saved to csv for later use.
