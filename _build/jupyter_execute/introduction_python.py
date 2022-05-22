#!/usr/bin/env python
# coding: utf-8

# # Lesson 1: Introduction to Python and Jupyter Notebooks
# 
# To add: how to open a Jupyter Notebook with a screenshot of how it looks. 
# 
# A Notebook is not a static webpage, but an interactive enviroment. Within the blocks (cells) of a Notebook code can be written ánd executed.
# 
# This Notebook will give a short introduction on how to work with Notebook in combination with Python.
# 
# ## How does a Notebook work?
# 
# ### Different cells
# 
# Notebooks are comprimised of different types of cells. The cell containing this text is a *textcel*. Text cells are generally used for descriptions and explantions. 
# 
# The layout is managed through *markdown* (see [markdown syntax](https://www.markdownguide.org/basic-syntax/) for more information).
# 
# The second main type of cell is the code cell. Such as teh example below:

# In[1]:


2*8


# Code cells are used to write and execute code. In our case Python. When a code cell is run, Python will execute the code in the cell.
# 
# There are multiple ways to run a cell:
# * By clicking the 'Run' button bovenaan te klikken;
# * By pressing 'shift + enter when the cell is selected (green frame)'
# 
# The moment a cell generates *output* the output is displayed beneath the cell, keeping code and output together.
# 
# **Assignment:** run the code cell above and look at the output.
# 
# ### Comments
# 
# Comments can be added to a code cell. Comments can be used to describe what a piece of code does, or can be used to tell where values can be changed.

# In[2]:


# This is an example of a comment in a code cell.


# The moment a # is typed in a code cell, everything after it will be regarded as a comment. Lines that have been marked as a comment will **not** be executed by Python when the cell is run.
# 
# **Assignment:** run the cell below. Does Python return output?

# In[3]:


#print("The solution to 35+12 is:")
#print(35+12)


# When the **#** is removed and the cell is run again, Python wil recognize the code and execute it.
# 
# **Assignment:** Ensure that Python executes the code and run the cell again.
# 
# ## Python
# 
# Below will follow a short introduction of Python. 
# Python was developed in 1991 by Guido van Rossum. The purpose of Python was to create a programming language that is both simple to understand and readable.  Python is open source, and can be used for free.
# 
# ### Input en variables
# 
# When using Python there are multiple types of input data, such as lists, numbers, text, and even whole tables.
# We put this input into *variables*. Essentially a container for the data. The name of a variable is up to your own discretion, although there are some [rules and guidlines](https://www.w3schools.com/python/gloss_python_variable_names.asp). 
# 
# Python remembers which input was loaded into which variable. This means that the variables can be used in the code instead of the data itself.
# 
# It is important to input data correctly, for numbers *no* quotation marks are used, for text quotation marks *must be* used!
# 
# The command *type()* can be used to determine what type of input a variable contains. 
# 
# *int* indicates a variable contains an integer, or whole number
# *str* indicates a variable contains a string, a piece of text. 
# 
# **Assignment** Run the cell below

# In[4]:


number = 9
text = "this is a text"


# In[5]:


type(number)


# In[6]:


type(text)


# **Important!** If you input a number *with* quotation marks Python will see it as text!
# 
# **Assignment:** Run the cell below

# In[7]:


number_but_wrong = "9"


# In[8]:


type(number_but_wrong)


# As mentioned above it is possible to use previously assigned variables in your code. 
# 
# **Assignment:** Run the cell below

# In[9]:


number_1 = 3
number_2 = 6

number_1 + number_2 


# **Assignment:** Using Python, calculate the sum of "35 + 69" in teh cell below. Start with making two variables to assign the numbers *35* and *69* to. Calculate the sum using these variables.

# In[10]:


# Make a variable for the number 35


# Make a variable for the number 69


# Calculate the sum using the variables


# The plus sign can be used to calculate sums, as you did in the above assignment. However, the plus sign can also be used to stick two different texts together. 
# 
# **Assignment:** run the cell below

# In[11]:


line_1 = "This is a "
line_2 = "stuck together text"

line_1 + line_2


# **Assignment:** Ensure that the four lines below are printed as one sentence in the output.

# In[12]:


line_1 = "Because of this Notebook "
line_2 = "I now know "
line_3 = "that programming with Python "
line_4 = "is very fun!"

# Stick the lines together


# ### Functions
# 
# When you program in Python you will make use of functions. Apart from ready made functions from packages (see below) Python contains a lot of ready to use built-in functions. Saving us a lot of manual coding!
# 
# Functions need to be passed one or more parameters as input. The syntax of a function is as follows: *functionname(parameters)*. When there are multiple parameters these are seperated with a comma.
# 
# You can find some examples below.
# 
# **Assignment:** Run the cells below

# In[13]:


# Calculate the highest number using the max() function.
max(5, 8, 35, 4, 75, 2)


# In[14]:


# Round a number using the round() function
# The first parameter is the number to round
# De second number is the required number of decimals. 
round(36.53343, 2)


# **Assignment:** Calculate the *lowest* number using the function min(). This functions works similarly to the previously used max() function.
# Use the following numbers: 6, 24, 8, 2, 14.

# In[15]:


# Use this cell to calculate the lowest number using the min() function.


# ### Packages
# 
# The last important thing to know is that Python works with packages. A package is a collection of modules with predefined functions. These functions can than be used in your own code. Using packages can save a lot of programming work and enhances the functionality of base Python. Most Python programmers regularly use packages.
# 
# Before using a Python package it needs to be *installed*. This preferably done using the command line but can also be done within your Jupyter Notebook.
# 
# Afterwards the package needs to be *imported* into the Notebook. After importing the package is ready for use.
# 
# Below you can find an example of installing, importing and using a package that measures the distances between two texts.
# 
# **Assignment:** Run the cells below

# In[16]:


# Install the package
get_ipython().system('pip install textdistance')


# In[17]:


# Import the package
import textdistance


# A package can be used in the same way as a function.
# In the case of the package used below, there are multiple methods for the calculation of the difference between texts. Among others there are the options 'hamming' and 'levenshtein'. The option that you want to use is added afte the name of the package. 
# 
# Syntax: *packagename.option(parameters)*
# 
# **Assignment:** Run the cell below

# In[18]:


## Make two variables wit ha line of text.
text1 = "Lesser leather never weathered wetter weather better"
text2 = "Lesser leather never weathered wethter weater better"

## Calculate the difference using the hamming option
textdistance.hamming(text1, text2)


# **Assignment:** Calculate the difference between texts using the levenshtein option.

# In[19]:


## Calculate the difference using the levenshtein option


# **Assignemnt:** For this assignment you will combine the previous steps to use the package 'passwordmeter'. You will use this package to measure the strength of three passwords, and determine how they can be improved.
# 
# You will test the following passwords: 
# 1: Welcome1234!
# 2: idJH$ndjj165@&4SGDJEh
# 3: PythonIsAweSome!?!
# 
# To complete this assignemnt you will need to complete the following steps:
# * Install the package 'passwordmeter'
# * Import the package 
# * Calculate the password strenght using the in-built function 'test' using the following syntax: *packagename.function(password)*

# In[20]:


# Install the package


# In[21]:


# Import the package


# In[22]:


# Check the strength of password 1 


# In[23]:


# Check the strength of password 2 


# In[24]:


# Check the strength of password 3


# ## The End
