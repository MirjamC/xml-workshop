#!/usr/bin/env python
# coding: utf-8

# # Lesson ?: Practical session: Working with XMLX, ElemenTree and Beautiful Soup
# 
# In this lesson, we are going to explore how the different packages work. We use the same example file that was used in lesson 2 (click here to download the file).
# 
# 
# This lesson is divided intro three sessions, where every session works with one of the Python packages that was introduced in lesson ?.
# With every package, we follow these steps:
# - Open the XML file
# - Display the structure of the XML file
# - Extraxt the booktitles
# - Extract name and surname of the author
# - Store the information in a .csv of .txt file
# 
# ## ?a: The ElemenTree
# 
# ElemenTree is part of the standard library and therefore does not need to be installed.
# 
# Before we can use the package, we have to let Python know we want to use it. We do this by importing the package.
# Type in a code cell:

# In[1]:


import xml.etree.ElementTree as ET


# Now, we want to open the XML file from which we want to extract information. 
# Add a new code cell and type:

# In[2]:


tree = ET.parse('data/example.xml')
root = tree.getroot()


# ```{note}
# In the code above, alter the 'path_to_file/name_file' with the path to the folder and the filename. 
# For example: D:\Projects\XML workshop\data\example.xml 
# ```
# 
# When you want to extract information from an XML file, it is important that you are familair with the structure of the file. 
# There are two ways to do this.

# In[3]:


print(ET.tostring(root, encoding='utf8').decode('utf8'))

