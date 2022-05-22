---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 4. Practical session: Working with ElemenTree

In this lesson, we are going to explore how the different packages work. We use the same example file that was used in lesson 2 (click here to download the file).

This lesson is divided intro three sessions, where every session works with one of the Python packages that was introduced in lesson ?.
With every package, we follow these steps:
- Load the XML file;
- Examine the structure of the XML file;
- Extraxt the booktitles and descriptions;
- Extract name and surname of the author;
- Extraxt the book identifier;
- Structure all information;
- Store the information in a .csv or .txt file.

Open a new Jupyter Notebook and type all code examples and code exercises in your Notebook. 

## 4a: The ElemenTree

ElemenTree is part of the standard library and therefore does not need to be installed.

Before we can use the package, we have to let Python know we want to use it. We do this by importing the package.
Type in a code cell:

```{code-cell}
import xml.etree.ElementTree as ET
```

#### Examine the structure of the file

Now, we want to open the XML file from which we want to extract information. 
Add a new code cell and type:

```{code-cell}
tree = ET.parse('data/example.xml')
root = tree.getroot()
```
```{note}
In the code above, alter the 'path_to_file/name_file' with the path to the folder and the filename. 
For example: D:\Projects\XML workshop\data\example.xml 
```

When you want to extract information from an XML file, it is important that you are familair with the structure of the file. 
There are two ways to do this. 

1. You can open the file in a programme like Notepad++ or open it in your browser
2. You can show the file in your Jupyter Notebook with the following code:

```{code-cell} ipython3
:tags: [hide-output]

# This cell should have its output hidden!
print(ET.tostring(root, encoding='utf8').decode('utf8'))
```

Wat vragen over de structuur bedenken

#### Extract the book titles and descriptions

Look at the XML structure. Which elements do we need do find the title and the description?

```{admonition} Solution
:class: tip, dropdown
We need the child element 'book', and his subchildren 'title' and 'description'. 
```

First, type the following code in your Jupyter Notebook to get the title from every book:

```{code-cell}
:tags: [hide-output]

# This cell should have its output hidden!
for book in root.findall('book'):
    title = book.find('title').text
    print(title)
```

```{note}
Explanation of the code.
The line:
	```
	for book in root.findall('book'):
	```
starts loop that iterates through all 'book' elements in the XML. For each elements, it executes the rest of the code.
	```	
	title = book.find('title').text
	```
This line creates a new variabele called 'title'. The content of the variable is content from the XML. For every 'book' elements, it searchs for 
a child element with the name 'title'. Then, it extraxts the content from the title element. To extract contents from elements, we use .text. 
	```
	title = book.find('title').text
	```
This line displays the output. In this case, it shows the title of every book. 
```
	
We can get the description of each book in the same way.
Try to alter the code above to retreive all the descriptions and print out the descriptions. 

```{admonition} Solution
:class: tip, dropdown
	
	for book in root.findall('book'):
		description = book.find('description').text
		print(description)
	
```

We can use one for loop to extract both the book title and description from the XML file. 
Combining multiple items is preferable because it save unnecessary lines of codes and merges the part of code which does the same thing.
This makes the code more readable and maintainable. 

Combining the two codes above leads to the following code:

```{code-cell}
:tags: [hide-output]

# This cell should have its output hidden!
for book in root.findall('book'):
	title = book.find('title').text
	description = book.find('description').text
	print(title, description)

```

#### Extract name and surname of the author
#### Extraxt the book identifier;
#### Structure all information;
#### Store the information in a .csv or .txt file.


