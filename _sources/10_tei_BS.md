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

# 10. Practical session: Tei and Beautiful Soup

For this session we will extract data from TEI format. We will only extract information from TEI using Beautifull Soup as ElementTree does not handle spaces (&nbsp) well.

When working with TEI format it is very important to check the lay-out. This can vary a lot between files.

Opletten: teis kunnen erg verschillen van opmaak 
##(voorbeeld van een TEI waarin de text in een p staat of in een l). 

As you can see in the example, it is wise to **always** check which elements you need to ensure you extract the correct data. 
TEI files of the same kind, for example all about one poet, usually are similar. However, double-checking this can save a lot of work (and frustration) later on.


````{admonition} Exercise
:class: attention
Import Beautifull Soup and load the XML file.
```Python
from bs4 import BeautifulSoup    

with open("xml-workshop/data/tei.xml", encoding='utf8') as f:
    root = BeautifulSoup(f, 'xml')
```
````

````{admonition} Exercise
:class: attention
Check the structure
```Python
root
```
````

````{admonition} Exercise
:class: attention
This TEI file contains information of a book. In which elements can you find the main content, the text, of this book?
Is the content present as a value or as an attribute?

````

```{admonition} Solution
:class: tip, dropdown
The content is contained in the elements *title*, *head*, *l*, and *p*.
```
There are a lot of elements containing the data. One option is to print the whole XML.
This can be done with:
```Python
root.text
```

A downside of this option is that a lot of metadata is printed out as well. Usually you would not want to have the metadata within the content. Filtering this out afterwards is very work-intensive.

````{admonition} Exercise
:class: attention
Can you think of a way to structure the text in a more logical manner?
````
```{admonition} Solution
:class: tip, dropdown
One option would be to print it out per chapter.
```

## Dividing the text in chapters

It is possible to iterate through the root and collect all the *div* elements with as type *chapter*. Having collected these it is now possible to print all *.text* content contained in these *div*s. 



````{admonition} Exercise
:class: attention
Construct a *for looop* that goes through the divs and prints out all content of the divs with *type* 'chapter' 
````

````{admonition} Solution
:class: tip, dropdown
One option would be to print it out per chapter.
```Python
for div in root.find_all('div'):
    if div.get('type') == 'chapter':
        print(div.text)
```
````

The code still prints out everything as a single piece of text without anything to distinguish the different chapters. Adding a chapter header is an easy way to be able to seperate the different chapters. 
This can be done by making a counter and printer the text'chapter [counter]' before every chapter. After every *div* that the code iterates through the counter is raised by one, so every chapter gets a distinguishing number.

```Python
counter = 1

for div in root.find_all('div'):
    if div.get('type') == 'chapter':
        print("chapter " + str(counter))
        print(div.text)
        counter += 1
```

Printing to the output is great for prototyping, but to make sure the extracted data can be used for further analysis and to keep the workspace a bit uncluttered it is best to ave the extracted content. This can be done chapter for chapter, by creating one larger file containting a chapter per row.

```{admonition} Exercise
:class: attention
Expand the code so it saves the extracted chapters as seperate text files, using the chapter name and number as file name.
Hint: do you remember f strings?
```

````{admonition} Solution
:class: tip, dropdown
```Python
counter = 1

for div in root.find_all('div'):
    if div.get('type') == 'chapter':
        chapter = "chapter_" + str(counter)
        with open(f"{chapter}.txt", "w", encoding="utf-8") as text_file:
            text_file.write(div.text)
            counter += 1
```
````


```{admonition} Exercise
:class: attention
If you recall, it is also possible to save the data as .csv.  
What are the easiest steps to do this?
```

```{admonition} Solution
:class: tip, dropdown
1. Saving the content in a list
2. Transforming into a Pandas Dataframe
3. Save the DataFrame to .csv
```

```{admonition} Exercise
:class: attention
Change the code to store the chapter and content in a list. Note that this will create one long list with all the extracted content.
```

````{admonition} Solution
:class: tip, dropdown
```Python
chapter_list = []
counter = 1

for div in root.find_all('div'):
    if div.get('type') == 'chapter':
        chapter = "chapter_" + str(counter)
        content = div.text
        chapter_list.append([chapter, content])
        counter += 1
```
````

```{admonition} Exercise
:class: attention
Transform the list into a Dataframe.
```

````{admonition} Solution
:class: tip, dropdown
```Python
import pandas as pd
book = pd.DataFrame(chapter_list , columns = (['chapter', 'content']))
```
````

It is good practice to check what you transformed.

```
book
```

## Extracting Poems


```{admonition} Exercise
:class: attention
Check the file to see which elements are needed to extract the poems from the file.
```

```{admonition} Solution
:class: tip, dropdown
To extract the poems the element **lg** with type **poems** is needed. 
```

````{admonition} Exercise
:class: attention
Print out all the poems from the file.
```

```{admonition} Solution
:class: tip, dropdown
```Python
for div in root.find_all('lg'):
    if div.get('type') == 'poem':
        print(div.text)
```
````

As before with the chapters, we will save the extracted poems as seperate, and numbered, files. 

```
counter = 1

for div in root.find_all('lg'):
    if div.get('type') == 'poem':
        poem = "poem_" + str(counter)
        with open(f"{poem}.txt", "w", encoding="utf-8") as text_file:
            text_file.write(div.text)
            counter += 1
```


```{admonition} Exercise
:class: attention
Adapt the code above to save the extracted poems to csv. If you feel lost, just go back a few excercises and look at what we did there. Remember, first list, then dataframe.
```

````{admonition} Solution
:class: tip, dropdown
```Python
poem_list = []
counter = 1

for div in root.find_all('lg'):
    if div.get('type') == 'poem':
        poem = "poem_" + str(counter)
        content = div.text
        poem_list.append([poem, content])
        counter += 1

import pandas as pd
poems = pd.DataFrame(poem_list , columns = (['poem', 'content']))

poems.to_csv('poems.csv')
```
````

Having extracted different types of content and saving them to text and csv, we could, for example, use these for further analyses. 


