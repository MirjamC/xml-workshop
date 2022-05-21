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

# Lesson 4: Practical session: Working with ElemenTree and Beautiful Soup

In this lesson, we are going to explore how the different packages work. We use the same example file that was used in lesson 2 (click here to download the file).

This lesson is divided intro three sessions, where every session works with one of the Python packages that was introduced in lesson ?.
With every package, we follow these steps:
- Load the XML file;
- Display the structure of the XML file;
- Extraxt the booktitles and descriptions;
- Extract name and surname of the author;
- Store the information in a .csv or .txt file.

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

#### Extract the book titles and descriptions

Look at the XML structure. Which elements do we need do find the title and the description?

```{admonition} Solution
:class: tip, dropdown
We need the child element 'book', and his subchildren 'title' and 'description'. 
```

First, we type in the code to get the title from every book:

```{code-cell} ipython3
:tags: [hide-output]

# This cell should have its output hidden!
for book in root.findall('book'):
    title = book.find('title').text
    print(title)
```





