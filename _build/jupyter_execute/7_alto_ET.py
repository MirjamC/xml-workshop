#!/usr/bin/env python
# coding: utf-8

# # 7. Practical: Extract information from the Alto/Didle format with ElemenTree
# 
# 
# In this lesson, we are going to extract the plain text and some additional information from an Alto file containing a Dutch newspaper. 
# We assume that you have followed the practical lesson 4. We will reference corresponding parts of that lesson so you can check how it worked. 
# 
# We follow these steps:
# - Load the XML file;
# - Examine the structure of the XML file;
# - Extract the plain text;
# - Divide the plain text into seperate articles;
# - Extract the page number;
# - Save the content in one file and in seperate textfiles.
# 
# Open a new Jupyter Notebook and type all code examples and code exercises in your Notebook. 
# (see explanation in {ref}`ET:import`)
# 
# ## Import ElemenTree and import the xml file
# 
# ```{admonition} Exercise
# :class: attention
# Import the package and load the xml file. 
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```Python
#     import xml.etree.ElementTree as ET
# 
# 	tree = ET.parse('xml-workshop/data/alto.xml')
# 	root = tree.getroot()
# ```
# ````
# 
# ## Examine the structure of the file
# 
# Before you can extract content from a XML file, you have to see what is inside and how it is structured. 
# 
# ```{admonition} Exercise
# :class: attention
# Show the XML file in your Notebook
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```Python
# 	print(ET.tostring(root, encoding='utf8').decode('utf8'))
# ```
# ````
# 
# As you can see, this XML file has a lot more elements and attributes than our example file. 
# Our goal is to extract the text from the news paper, to seperate the text into articles, and to store them on our computer with the page number. 
# 
# So first, let's see if we can find where the textual content of the news paper is stored. 
# 
# ```{admonition} Exercise
# :class: attention
# Scroll through the XML file and see if you can find the element in which the text of the newspaper is stored. Hint: one of the news articles mentioned
# 'olifant'. 
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# The content of the news paper articles is stored in the element 'ns0:String'
# 
# 	<String ID="P3_ST00483" HPOS="557" VPOS="3994" WIDTH="109" HEIGHT="26" CONTENT="olifant" WC="0.99" CC="6000010"/>
# ```
# 
# ```{admonition} Exercise
# :class: attention
# If we compare the element 'String' to our example XML, we see that there is a difference in how the content is stored. What is the difference? 
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# The content of the elements of the example XML were stored als values from the elements. 
# The content of the String element is stored in an attribute called 'CONTENT'. 
# ```
# 
# ```{admonition} Exercise
# :class: attention
# There are a lot of nested element in this XML file. What are the parents, grandparents and grandgrandparents of the 'String' element? Are there even more parents?
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# - The parent of the 'String' element is 'Textline'
# - The grandparent is 'TextBlock'
# - The grandgrandparent is 'Page'.
# - The complete line is alto/Layout/Page/TextBlock/Textline/String
# ```
# Now we know some important information about this Alto file, so let's see if we can extract the content. 
# 
# ## Extract the plain text
# 
# We will start by extracting all the text, without worrying about the division between the articles. 
# 
# ```{admonition} Exercise
# :class: attention
# As you have seen, the plain text of the news paper is stored in the 'CONTENT' attribute of the 'String' element. How can you extract the values from attributes?
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# This can be done with the .get method, for example: book.get('id'). 
# ```
# 
# In lesson 4 we learned that is is possible to acces the elements with a for loop, like
# ```Python
# for book in root.findall('book'):
# ```
# However, as you have seen above, the element 'String' is a grandgrandgrandgrandchild from the start element 'alto'.
# One way to access the String element is by typing all ancestors, leading to a code like:
# ```Python
# for book in root.findall('alto/Layout/Page/TextBlock/Textline/String'):
# ```
# 
# However, we preferably avoid that, since it takes a lot of time and can easily lead to mistakes. 
# ```{admonition} Exercise
# :class: attention
# In lesson 4, we learned a way to escape all the ancestors, how did we do this?
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# By adding './/', for example 
# ```Python
# for book in root.findall(''.//author'):
# ```
# ````
# 
# So, we can easily loop through all String elements by using the .// escape, and we can extract the content from the CONTENT attribute with the .get method. 
# 
# ````{admonition} Exercise
# :class: attention
# ```Python
# Create the for loop to extract the content. This loop looks like this:
#     for text in the String elements:
# 		print(the value of the CONTENT attribute)
# ```
# Complete the code and run it. What happens?
# ````
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```Python
# 	for book in root.findall('ns0:String'):
# 		print(book.get('CONTENT'))
# ```
# The code doesn't produce any output. 		
# ````
# 
# ### Namespaces
# 
# So, what is going on? Why is not there any output?
# As described in lesson ***2***, some XML documents make use of *namespaces*. 
# If we look at the first line of the Alto file, we see:
# 
# ```XML
# <?xml version='1.0' encoding='utf8'?>
# <ns0:alto xmlns:ns0="http://schema.ccs-gmbh.com/ALTO">
# ```
# 
# The second line shows us that this XML make use of namespaces. 
# 'ns0' is used as a shortcut for 'http://schema.ccs-gmbh.com/ALTO'. 
# 
# We have now two options to handle the namespaces in ElemenTree:
# 1. Type the namespace before the element name between curly brackets: {http://schema.ccs-gmbh.com/ALTO}
# 
# ```Python
# for book in root.findall('.//{http://schema.ccs-gmbh.com/ALTO}String'):
#     content = book.get('CONTENT')
#     print(content)
# ```
# 
# 2. Declare the namespace in elemenTree. This provides Python with a dictionary of the used namespaces, which it can then use.

# In[1]:


ns = {'ns0': 'http://schema.ccs-gmbh.com/ALTO'}


# Now you can use the abbreviation of the namespace in your code:
# ``` Python
# for book in root.findall('.//ns0:String', ns):
#     content = book.get('CONTENT')
#     print(content)
# ```
# 
# ```{note}
# If you declare the namespace in Python with a dictionary, do not forget to put ', ns' after your element name in the *.findall*. 
# Without this 'ns', Python does not recognize the namespace. 
# You only have to declare the namespaces once, Python will then recognize them in de rest of your Jupyter Notebook.
# ```
# 
# For the remainder of this lesson, we will use the second option. 
# 
# ```{admonition} Exercise
# :class: attention
# Choose one of the namespace options and run the code to extract all the text from the CONTENT attribute. 
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```Python
# 	for book in root.findall('.//ns0:String', ns):
# 		print(book.get('CONTENT'))		
# ```
# ```` 
# 
# ## Divide the plain text into seperate articles
# 
# As you can see, the text is printed in seperate words, that all appear in one long list. So, this is quit unreadable. We can store the text in a *string* variable in which we concatenate all words. 
# 
# ```Python
# all_content = ""
# 
# for book in root.findall('.//ns0:String', ns):
#     content = book.get('CONTENT')
#     all_content = all_content + " " + content
# ```
# 
# The content is now more readable, however, it is still one long blob of the complete text of the newspaper.
# We would like to divide the texts in articles. 
# 
# ```Python
# article_content = ""
# 
# for book in root.findall('.//ns0:TextBlock', ns):
#     for article in book.findall('.//ns0:String', ns):
#         content = article.get('CONTENT')
#         article_content = article_content + " " + content
#     print(article_content)
#     print("")
#     article_content = ""
# 
# Division between title and not title
# article_content = ""
# txt_type = ""
# 
# for book in root.findall('.//ns0:TextBlock', ns):
#     txt = book.get("STYLEREFS")
#     if "LEFT" in txt:
#         txt_type = 'Title'
#     else:
#         txt_type = 'Article'
#     for article in book.findall('.//ns0:String', ns):
#         content = article.get('CONTENT')
#         article_content = article_content + " " + content
#     print(txt_type)
#     print(article_content)
#     print("")
#     article_content = ""
# ```
# 
# - Extract the page number;
# ```Python
# for book in root.findall('.//ns0:Page', ns):
#     pagenr = book.get('ID')
#     print(pagenr)
# ```
# 
# - Save the content in one file and in seperate textfiles; 
# 
# - Met didle metadata over krant en pagina opslaan
# - Met didle losse artikelen eruit en daarvan de xmls opslaan. Uit deze xmls de tekst halen. (xml of plain text?)
# 
# 
# 
# 
# Bonus les: alto aan didle koppelen op basis van positie.
