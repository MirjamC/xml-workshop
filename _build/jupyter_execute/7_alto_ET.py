#!/usr/bin/env python
# coding: utf-8

# # 7. Practical: Extract information from the Alto format with ElemenTree
# 
# In this lesson ,we are going to work with the Alto and Didle format. As shown in lesson ***?***, the Alto and Didle are connected to each other. 
# The Alto stores the plain text and the Didl the metadata of the newspaper. For this lesson, we assume that you have followed the practical lesson 4. 
# 
# This lesson contains the following content
# - Load the Alto file and examine the structure <span style="color:#ef6079">(*basic*)</span>
# - Extract the complete content of a newspaper page from the Alto file <span style="color:#ef6079">(*basic*)</span>
# - Load the Didl file and examine the structure <span style="color:#ef6079">(*basic*)</span>
# - Extract newspaper metadata from the Didl file. <span style="color:#ef6079">(*basic*)</span>
# - Extract all seperate articles from the total newspaper from the Didl file <span style="color:#ef6079">(*moderate*)</span>
# - Extract all seperate articles from a specific newspaper from the Didl file <span style="color:#ef6079">(*advanced*)</span>
# 
# Open a new Jupyter Notebook and type all code examples and code exercises in your Notebook. 
# 
# ## Load the Alto file and examine the structure
# 
# ```{admonition} Exercise
# :class: attention
# Import the package and load the xml file. 
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```Python
# import xml.etree.ElementTree as ET
# tree = ET.parse('/data/alto_id1.xml')
# root_alto = tree.getroot()
# ```
# ````

# In[1]:


import xml.etree.ElementTree as ET
tree = ET.parse("data/alto_id1.xml")
root_alto = tree.getroot()


# ```{note}
# We will work with two XML files in this lesson. Therefore, we will name the root of the XML files according to the type of the XML: 'root_alto' for the alto XML and 'root_didl' for the Didl XML. 
# ```
# 
# Before you can extract content from an XML file, you have to see what is inside and how it is structured. 
# 
# ```{admonition} Exercise
# :class: attention
# Show the XML file in your Notebook
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```Python
# 	print(ET.tostring(root_alto, encoding='utf8').decode('utf8'))
# ```
# ````

# In[2]:


print(ET.tostring(root_alto, encoding='utf8').decode('utf8'))


# *** print hier de output 
# 
# As you can see, this XML file has a lot more elements and attributes than our example file. 
# Our goal is to extract the text from the news paper, to seperate the text into articles, and to store them on our computer with the page number. 
# 
# So first, let's see if we can find where the textual content of the news paper is stored. 
# 
# ```{admonition} Exercise
# :class: attention
# Scroll through the XML file and see if you can find the element in which the text of the newspaper is stored. Hint: one of the news articles mentiones the
# word 'spoorwegmaatschappij'. 
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# The content of the news paper articles is stored in the element 'ns0:String', for example:
# 
# 	<String ID="P1_ST00323" HPOS="244" VPOS="2387" WIDTH="318" HEIGHT="35" CONTENT="spoorwegmaatschappij" WC="0.99" CC="88668080809486709965"/>
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
# ## Extract the complete content of a newspaper page from the Alto file
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
# for page in root_alto.findall('alto/Layout/Page/TextBlock/Textline/String'):
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
# for page in root_alto.findall('ns0:String'):
# 	print(page.get('CONTENT'))
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
# ```
# for book in root.findall('.//{http://schema.ccs-gmbh.com/ALTO}String'):
#     content = book.get('CONTENT')
#     print(content)
# ```
# 
# 2. Declare the namespace in elemenTree. This provides Python with a dictionary of the used namespaces, which it can then use.

# In[3]:


ns = {'ns0': 'http://schema.ccs-gmbh.com/ALTO'}


# Now you can use the abbreviation of the namespace in your code:
# ``` 
# for page in root_alto.findall('.//ns0:String', ns):
#     content = page.get('CONTENT')
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
# for page in root_alto.findall('.//ns0:String', ns):
#     content = page.get('CONTENT')
#     print(content)	
# ```
# ```` 
# 
# This leads to the following output:

# In[4]:


import xml.etree.ElementTree as ET

tree = ET.parse('data/alto_id1.xml')
root_alto = tree.getroot()

for page in root_alto.findall('.//ns0:String', ns):
    content = page.get('CONTENT')
    print(content)


# ### Make the output more readable
# 
# As you can see, the text is printed in seperate words, that all appear in one long list. So, this is quit unreadable. We can store the text in a *string* variable in which we concatenate all words.

# In[5]:


ns = {'ns0': 'http://schema.ccs-gmbh.com/ALTO'}

all_content = ""

for page in root_alto.findall('.//ns0:String', ns):
	content = page.get('CONTENT')
	all_content = all_content + " " + content
	
print(all_content)


# The content is now more readable, however, it is still one long blob of the complete text of the newspaper.
# As you can see in the XML file, the content is divided into sections. 
# 
# ```{admonition} Exercise
# :class: attention
# Look at the XML file. There are different elements that divide the text. Which element would likely be used to seperate articles from each other?
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# The element 'TextBlock'
# ```
# 
# Now that we know how we can divide the various session, let's put this into code.
# Instead of storing all the output into one variabele, we create a variable, and store within it the information of one session. Then we print the variabele and empty it, so it can be re-used for a new session.
# 
# In code, this looks like this:

# In[6]:


article_content = ""

for book in root_alto.findall('.//ns0:TextBlock', ns):
    for article in book.findall('.//ns0:String', ns):
        content = article.get('CONTENT')
        article_content = article_content + " " + content
    print(article_content)
    print("") ## add a linebreak between the seperate sessions
    article_content = ""


# Now we have a page of plain text that is better structured. 
# The only thing left is to retreive the page number, and then we'll have all the information to save this data to a textfile or csv. 
# 
# ```{admonition} Exercise
# :class: attention
# Look at the XML file. Where can we find the page number?
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# The page number is stored in the 'Page' element. 
# ```
# 
# ```{admonition} Exercise
# :class: attention
# Write the code to extract the page number from the XML. 
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```Python
# for book in root_alto.findall('.//ns0:Page', ns):
#     pagenr = book.get('ID')
#     print(pagenr)
# ```
# ````
# 
# The page number is:

# In[7]:


for book in root_alto.findall('.//ns0:Page', ns):
    pagenr = book.get('ID')
    print(pagenr)


# ## Load the Didl file and examine the structure ;
# 
# We now have a more readable page with the corresponding page number. However, if we store this as is, we will have no idea from which newspaper this page was extracted. This makes it of limited reuseability. In lesson 3 we described that we can find metadata corresponding to an Alto file in a Didle file. 
# The alto and didle file have the same identifier, so you can match them.
# 
# In our case, they both have the identifier 1. 
# 
# ```{admonition} Exercise
# :class: attention
# Load the corresponding Didl file in your notebook. Name the root 'root_didl'. Look at the structure of the file. 
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```Python
# tree = ET.parse('data/didl_id1.xml')
# root_didl = tree.getroot()
# print(ET.tostring(root_didl, encoding='utf8').decode('utf8'))
# ```
# ````
# 
# ```{admonition} Exercise
# :class: attention
# Look at the Didle file and see if you can find in which element the title of the newspaper is scored. Hint: the title is 'Algemeen Handelsblad'. 
# What parent of this element contains all information we need to extract the title and the publication date?
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# The title is stored in the element 'title', and the publication date in the element 'date'. They can both be found in the element 'Resource'. 
# ```
# 
# 
# ## Extract newspaper metadata from the Didl file.
# 
# We have seen that the block resource contains all the information we want. If we look closely at the file, we see that there are multiple elements with the name 'resource', but the one we want is the first. If you want all the information from all resource blocks, we can use the findall method as we did before. However, we now only want information from the first block. In that case, you can just simply use find(). This will return the first element is finds. The rest of the syntax stays the same. 
# 
# 
# ```{admonition} Exercise
# :class: attention
# Write a code that gets the only the first 'component' element, and then from this element create a for loop that loops through the dcx element. 
# Extract the title of the newspaper and the publication date. Store them in two seperate variables. 
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# ```
# ns_didl = {'dc': 'http://purl.org/dc/elements/1.1/',
#           'ns2': 'urn:mpeg:mpeg21:2002:02-DIDL-NS', 
#           'ns4' : 'info:srw/schema/1/dc-v1.1' }
# 
# item = root_didl.find('.//ns2:Resource', ns_didl)
# 
# for article in item.findall('.//ns4:dcx', ns_didl):
#     title = article.find('.//dc:title', ns_didl)
#     date = article.find('.//dc:date', ns_didl)
#     print(title.text, date.text) 
# ```
# ````
# 
# Now we can store the content of this newspaper page in a text file with as name the a combination of the title of the newspaper, the publication date, and the page number. 
# We can create the filename like this:
# 
# ```
# filename = f'{title}_{date}_{pagenr}.txt'
# ```
# 
# ```{admonition} Exercise
# :class: attention
# Save the content in a file.
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# with open(filename, "w", encoding="utf-8") as f:
#     f.write(article_content)
# ```
# 
# ## Extract all seperate articles from a specific newspaper from the Didl file
# 
# As you saw in the above sections, the Alto format has no clear seperation between the articles and is therefore especially suitable when you are interested in the complete newspaper page.
# 
# However, there are a lot of cases in which you would be interested in the seperate articles en metadata about these articles (for example, the type of article).
# 
# The collection of the national library makes use of Didl XML files to store additional information. You can use the Didle XML to extract this information and to gather the articles. 
# 
# ```{admonition} Exercise
# :class: attention
# Look at the Didl file, do you see information about the articles?
# ```
# 
# ```{admonition} Solution
# :class: tip, dropdown
# Yes, they are stored in the 'Resource' elements.  
# ```
# 
# As you can see, there are blocks with information about the articles. The articles themself are not present in the Didl, but we can retreive them through their identifier. To do this we will perform the following two steps:
# 
# - Extract article information and identifier from the Diddl
# - Download the articles and extract the plain text
# 
# We start by extracting the subject, title and identifier from the resource element. However, there is also
# other information stored in the resource elements, such as the news paper title. 
# 
# You can distinguish the articles using the newspaper metadata based on the element 'subject'.
# All articles have a subject ('artikel', 'familiebericht' etc) whilst the other metadata does not.
# 
# This distintion can be done with an 'if' statement, in which we check if there is a element with the name 'subject' present in the element block. 
# 
# We will start with extracting the type of article, title, and identifier from the Didl XML. The identifier will later be used to download the articles.

# In[8]:


ns_didl = {'dc': 'http://purl.org/dc/elements/1.1/',
			'ns2': 'urn:mpeg:mpeg21:2002:02-DIDL-NS', 
			'ns4' : 'info:srw/schema/1/dc-v1.1', 
			'ns7' : 'http://www.kb.nl/namespaces/ddd' }

for item in root_didl.findall('.//ns2:Resource', ns_didl):
	for article in item.findall('.//ns4:dcx', ns_didl):
		a_type = article.find('.//dc:subject', ns_didl)
		## The first block will not have a subject as it contains newspaper metadata instead of article metadata.
		## This can be filtered out using an 'if [subject] is None' control structure.
		if a_type is not None:
			title = article.find('.//dc:title', ns_didl)
			identifier = article.find('.//dc:identifier', ns_didl)
			print(a_type.text, title.text, identifier.text)


# ```{admonition} Exercise
# :class: attention
# Adapt the code above to store the variables into a list of articles.
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# Your code should look like the code below:
# ```
# ns_didl = {'dc': 'http://purl.org/dc/elements/1.1/',
#           'ns2': 'urn:mpeg:mpeg21:2002:02-DIDL-NS', 
#           'ns4' : 'info:srw/schema/1/dc-v1.1', 
#           'ns7' : 'http://www.kb.nl/namespaces/ddd' }
# 
# article_list = []
# 
# for item in root_didl.findall('.//ns2:Resource', ns_didl):
# 	for article in item.findall('.//ns4:dcx', ns_didl):
# 		a_type = article.find('.//dc:subject', ns_didl)
# 		if a_type is not None:
# 			title = article.find('.//dc:title', ns_didl)
# 			identifier = article.find('.//dc:identifier', ns_didl)
# 			article_list.append([a_type.text, title.text, identifier.text])
# ```
# ````
# 
# Now we have the identifier for every article in the dataset. This identifier can be used to download the XML of its article and extract the text from it. We will do this with one article.
# 
# As an example, we will use the identifier 'http://resolver.kb.nl/resolve?urn=ddd:010097934:mpeg21:a0001'. If we  click on this, we will be led to the image of the newspaper page. However, if we were to add ':ocr' to the identifier, we will be led to the XML containing the OCR of that newspaper page.
# 
# 'http://resolver.kb.nl/resolve?urn=ddd:010097934:mpeg21:a0001:ocr'
# 
# This OCR can be saved to file, either manually or by using Python.
# 
# To save the OCR using Python we will need the *urllib* package.
# 
# ```{note}
# We recommend to always save the identifier in the name of the file, in this case the ***a0001*** indicates the article number, so we will save the whole identifier. Because Windows does not allow ***:*** in filenames we  will change this to an underscore. 
# Everything before ***urn**** will be removed from the identifier.
# ```

# In[ ]:


## import urllib
from urllib.request import urlopen

filename = 'http://resolver.kb.nl/resolve?urn=ddd:010097934:mpeg21:a0001:ocr'
## Remove the first part from the filename, so you keep only ddd:010097934:mpeg21:a0001:ocr'
filename = filename.split('=')[1]
## Replace the : with _
filename = filename.replace(':', '_')

url = 'http://resolver.kb.nl/resolve?urn=ddd:010097934:mpeg21:a0001:ocr'

## write XML to file, downloading happens in this step too.
with open(filename + ".xml", "w", encoding="utf-8") as f:
    f.write(urlopen(url).read().decode('utf-8'))


# Now, we can open this xml file and look at the structure.

# In[ ]:


tree = ET.parse('ddd_010097934_mpeg21_a0001_ocr.xml')
root_article = tree.getroot()
print(ET.tostring(root_article, encoding='utf8').decode('utf8'))


# ```{admonition} Exercise
# :class: attention
# Extract the title and content, and store these in seperate variables.
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# Your code should look like the code below
# ```Python
# for titles in root_article.findall('.//title'):
#     title = titles.text 
# 
# for contents in root_article.findall('.//p'):
#     content = contents.text + "\n"
# ```
# ````
# 
# This can than be saved to a textfile
# 
# ```Python
# with open(filename + ".txt", "w", encoding="utf-8") as f:
#     f.write(title + "\n" + content)
# ```
# 
# The above workflow now consists of the folowing steps:
# - Downloading the file
# - Opening the file
# - Extracting the contents
# - Saving the contents to file
# 
# This can also be combined into one piece of code that handles all these steps.
# 
# ```Python
# from urllib.request import urlopen
# 
# identifier = 'http://resolver.kb.nl/resolve?urn=ddd:010097934:mpeg21:a0001:ocr'
# filename = identifier.split('=')[1]
# filename = filename.replace(':', '_')
# 
# tree = ET.ElementTree(file=urlopen(identifier))
# 
# root = tree.getroot()
# 
# for titles in root.findall('.//title'):
#     title = titles.text + "\n"
# 
# for contents in root.findall('.//p'):
#     content = contents.text + "\n"
# 
# with open(filename + ".txt", "w", encoding="utf-8") as f:
#     f.write(title + "\n" + content)
# ```
# 
# Until now we have manually selected a single article from a page and saved this. Of course one article is generally not enough and manually changing the identifier for every file is a lot of work.
# Luckily, just as we have used a for loop to iterate through an XML file, we can use a for loop to iterate through a list of identifiers.
# 
# The folowing code does just that. It iterates through **article_list** and grabs the identifier of an article. Then it adds *:ocr* behind the identifier, downloads the file, and extracts the text. Finally, it saves the result as a textfile.
# 
# ```Python
# from urllib.request import urlopen
# 
# for article in article_list:
#     # We want the third object of the list, but Python counts from 0.    
#     identifier = article[2] + ":ocr"
#     # Prepare the filename
#     filename = identifier.split('=')[1]
#     filename = filename.replace(':', '_')
#     
#     # Download the xml and load into Python
#     tree = ET.ElementTree(file=urlopen(identifier))
#     root = tree.getroot()
#     
#     #Extract the content
#     for titles in root.findall('.//title'):
#         title = titles.text 
# 
#     for contents in root.findall('.//p'):
#         content = contents.text + "\n"
#         
#     # Some content, like advertisements, have no titles. 
#     if title is None:
#         article = content
#     else:        
#         article = title + "\n" + content
#         
#     #Save the content in a file 
#     with open(filename + ".txt", "w", encoding="utf-8") as f:
#         f.write(article)
#  
# ```
# 
# ## Extract all seperate articles from a specific newspaper from the Didl file
# 
# In the above we treated two options:
# - Extracting the whole content of a page and saving into one file
# - Extracting all the articles of a newspaper and saving this to file per article.
# 
# It is also possible to download the articles per page.
# If you look into the XML file you will see the element 'Component' with attribute dc:identifier.
# For example:
# ```XML
# <didl:Component dc:identifier="ddd:010097934:mpeg21:p001:a0003:zoning">
# ```
# 
# In this case the ***p001*** indicates that this concerns the first page. If the code above is adapted to loop via the element 'Component', it becomes possible to filter out those elements whose attribute contains ***p001***. This can be done using: 
# 
# ```Python
# if 'p001' in [variable]
# ```
# 
# Then the rest of the code can be made similarly to the code we used to extract all identifiers of all articles of the whole newspaper. 
# 
# ```{admonition} Exercise
# :class: attention
# Write code to collect the identifiers from page 1 and store them row by row in a Dataframe together with the pagenumber, type of text, and title. Then print this Dataframe.
# 
# **!Pro-tip: The namespace declaration does not work for attributes!**
# ```
# 
# ````{admonition} Solution
# :class: tip, dropdown
# Your code should look like the code below:
# ```Python
# ns_didl = {'dc': 'http://purl.org/dc/elements/1.1/',
#           'ns2': 'urn:mpeg:mpeg21:2002:02-DIDL-NS', 
#           'ns4' : 'info:srw/schema/1/dc-v1.1', 
#           'ns7' : 'http://www.kb.nl/namespaces/ddd' }
# 
# article_list = []
# 
# # Declare the page variable here so it can easily be changed
# page = 'p001'
# 
# for item in root_didl.findall('.//ns2:Component', ns_didl):
#     identifier_page = item.get('{http://purl.org/dc/elements/1.1/}identifier')
#     if page in identifier_page:
#         for article in item.findall('.//ns4:dcx', ns_didl):
#                 a_type = article.find('.//dc:subject', ns_didl)
#                 if a_type is not None:
#                     title = article.find('.//dc:title', ns_didl)
#                     identifier = article.find('.//dc:identifier', ns_didl)
#                     article_list.append([page, a_type.text, title.text, identifier.text])
#  
# import pandas as pd
# articles = pd.DataFrame(article_list, columns = ['Page', 'Type', 'Title', 'Identifier'])
# 
# articles
# ```
# ````

# In[ ]:


ns_didl = {'dc': 'http://purl.org/dc/elements/1.1/',
			'ns2': 'urn:mpeg:mpeg21:2002:02-DIDL-NS', 
			'ns4' : 'info:srw/schema/1/dc-v1.1', 
			'ns7' : 'http://www.kb.nl/namespaces/ddd' }

article_list = []

page = 'p001'

for item in root_didl.findall('.//ns2:Component', ns_didl):
	identifier_page = item.get('{http://purl.org/dc/elements/1.1/}identifier')
	if page in identifier_page:
		for article in item.findall('.//ns4:dcx', ns_didl):
			a_type = article.find('.//dc:subject', ns_didl)
			if a_type is not None:
				title = article.find('.//dc:title', ns_didl)
				identifier = article.find('.//dc:identifier', ns_didl)
				article_list.append([page, a_type.text, title.text, identifier.text])
 
import pandas as pd
articles = pd.DataFrame(article_list, columns = ['Page', 'Type', 'Title', 'Identifier'])
articles

