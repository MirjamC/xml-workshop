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

Open a new Jupyter Notebook and type all code examples and code exercises in your Notebook. (see explanation in ET:import)


## voorbeeld toevoegen
Opletten: teis kunnen erg verschillen van opmaak 
##(voorbeeld van een TEI waarin de text in een p staat of in een l). 

As you can see in the example, it is wise to **always** check which elements you need to ensure you extract the correct data. 
TEI files of the same kind, for example all about one poet, usually are similar. However, double-checking this can save a lot of work (and frustration) later on.
Let's start with importing Beautifull Soup and loading the XML file.

```{admonition} Exercise
:class: attention
Import Beautifull Soup and load the XML file into a variable.
```

````{admonition} Solution
:class: tip, dropdown
```Python
from bs4 import BeautifulSoup    

with open("xml-workshop/data/tei.xml", encoding='utf8') as f:
    root = BeautifulSoup(f, 'xml')
```
````

We are now all clear to start exploring the XLM file. As always we should first explore the structure.

```{admonition} Exercise
:class: attention
Check the structure of the data.
```

````{admonition} Solution
:class: tip, dropdown
We can check the structure of the loaded file by simply running the variable it is stored in.
```Python
root
```
````

```{code-cell}
:tags: [remove-input, hide-output] 
from bs4 import BeautifulSoup    

with open("xml-workshop/data/tei.xml", encoding='utf8') as f:
    root = BeautifulSoup(f, 'xml')
root
```



This TEI file contains information of a book. It has multiple elements containing data about the book and the content of the book. We will need to read teh structure carefully to find the right elements where the content we want is stored.

```{admonition} Exercise
:class: attention
 In which elements can you find the main content, the text, of this book?
Is the content present as a value or as an attribute?
```

```{admonition} Solution
:class: tip, dropdown
The content is contained in the elements *title*, *head*, *l*, and *p*.
```

There are a lot of elements containing the data. One option is to print the whole XML. This way no content will be missed and all possible text is extracted. This can be done with:
```{code-cell}
:tags: [hide-output] 
root.text
```

A downside of this option is that a lot of metadata is printed out as well. Usually you would not want to have the metadata within the content. Filtering this out afterwards is very work-intensive.


```{admonition} Exercise
:class: attention
Can you think of a way to structure the text in a more logical manner? 
```
```{admonition} Solution
:class: tip, dropdown
One option would be to print it out per chapter.
```

## Dividing the text in chapters

It is possible to iterate through the root and collect all the *div* elements with as type *chapter*. When all the chapters are collected it is then possible to print all *.text* content contained in these *div*s. 
Using a *for loop* is a good start. This will iterate through the divs one by one. Within the loop we can perform the different actions, like extraction and transformation. 
 
```{admonition} Exercise
:class: attention
Construct a *for loop* that goes through the divs and prints out all content of the divs with *type* 'chapter' 
```

````{admonition} Solution
:class: tip, dropdown
One option would be to print it out per chapter.
```Python
## the for loop iterates through every div 
for div in root.find_all('div'):
	## all actions within the loop are performed div by div.
	## here we select only divs with type chapter
    if div.get('type') == 'chapter':
		## and we print the div
        print(div.text)
```
````
```{code-cell}
:tags: [remove-input, hide-output] 
for div in root.find_all('div'):
    if div.get('type') == 'chapter':
        print(div.text)
```


The code still prints out everything as a single piece of text without anything to distinguish the different chapters. Adding a chapter header is an easy way to be able to seperate the different chapters. 
This can be done by making a counter and printer the text 'chapter [counter]' before every chapter. After every *div* that the code iterates through the counter is raised by one, so every chapter gets a distinguishing number.

```Python
## initialise the counter at 1
counter = 1

for div in root.find_all('div'):
    if div.get('type') == 'chapter':
        print("chapter " + str(counter))
        print(div.text)
		## add 1 to the counter every iteration of the loop
        counter += 1
```

Try the code above to see how the output now contains increasing chapter count

```{code-cell}
:tags: [remove-input,hide-output]

from bs4 import BeautifulSoup    

with open("xml-workshop/data/tei.xml", encoding='utf8') as f:
    root = BeautifulSoup(f, 'xml')

counter = 1

for div in root.find_all('div'):
    if div.get('type') == 'chapter':
        print("chapter " + str(counter))
        print(div.text)
		## add 1 to the counter every iteration of the loop
        counter += 1
```

Great! we now have all the chapters in order, and numbered. However, this is not the most readable output.


## Saving the chapters to disk

Printing to the output is great for prototyping, but to make sure the extracted data can be used for further analysis and to keep the workspace a bit uncluttered it is best to save the extracted content to file. This can be done chapter for chapter or by creating one larger file containting a chapter per row.

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

Now we have a lot of text files. Each one containing one chapter of the book . For some uses this may be preferable, but for other a single, ordered file may be preferred. 
In the next exercises we will write code that will store the chapters in an ordered format in a single file.

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

Having refreshed our memory we will now put it into practice. 

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

With the first step done the list can now be transformed into a Dataframe. Don't forget to think about the order of the list content and the Dataframe columns.

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

```{admonition} Exercise
:class: attention
It is good practice to check what you transformed, so print out the dataframe.
```

```{admonition} Solution
:class: tip, dropdown
	book
```


If the Dataframe is in order we can save the Datframe directly to file.
 
```{admonition} Exercise
:class: attention
Save the Dataframe to csv.
```

````{admonition} Solution
:class: tip, dropdown
```Python
chapters.to_csv('chapters.csv')
```
Remember that this saves the csv in the root folder of your jupyter installation. If you want it saved in a specific location you need to specify the path before the filename followed by a /.
````

## Extracting Poems

For some uses only a specific pieces of an XML is needed. Extracting everything and then either removing or ignoring part of the extracted content is a lot of work that can be omitted by specifically extracting what is needed.
The example TEI file contains a book that consists of both pieces of prose and poems. Both of these are specified somewhere in the XML. Over the coming exercises we will extract only the poems. To do this we need to know which elements indicate contain the poems.

```{admonition} Exercise
:class: attention
Check the file to see which elements are needed to extract the poems from the file.
```

```{admonition} Solution
:class: tip, dropdown
To extract the poems the element **lg** with type **poems** is needed. 
```

Having found the elements with the poems, we will now need to extract them from the XML.

```{admonition} Exercise
:class: attention
Write a piece of code that extracts and prints all the poems from the file. You can look at the previous exercises for hints.
```

````{admonition} Solution
:class: tip, dropdown
```Python
for div in root.find_all('lg'):
    if div.get('type') == 'poem':
        print(div.text)
```
````

As we did in the previous exercises where we extracted the whole chapters, we will save the extracted poems as seperate, and numbered, files. 


```{admonition} Exercise
:class: attention
Expand the code of the previous exercise to include a counter for numbering the poems, and saving the poems one by one. As with the previous exercises use 'poem + counter' or something similar as a filename. 
```

````{admonition} Solution
:class: tip, dropdown
```
counter = 1

for div in root.find_all('lg'):
    if div.get('type') == 'poem':
        poem = "poem_" + str(counter)
        with open(f"{poem}.txt", "w", encoding="utf-8") as text_file:
            text_file.write(div.text)
            counter += 1
```
````

Again, we now have many seperate files. But we will also want to create a single file containing the poems in a structured manner.


```{admonition} Exercise
:class: attention
Adapt the code above to save the extracted poems to a single csv. If you feel lost, just go back a few exercises and look at what we did there. Remember, first list, then dataframe.
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

This should create a file in your Jupyter home folder containing all all the numbered poems.

The next exercise is a bit more challenging. 

```{admonition} Exercise
:class: attention
Create a Dataframe containing all the (numbered) chapters and poems:
- The chapters must be numbered consecutively
- The poems must be numbered consecutively per chapter

This means that you will need to extract chapter information from the XML, in addition to the poem information. Also, something to number the chapters is needed.
```

````{admonition} Solution
:class: tip, dropdown
You code should look similar to the code below. 
```
import pandas as pd
chapter_list = []
c_counter = 1
p_counter = 1 
	for div in root.find_all('div'):
		if div.get('type') == 'chapter':
			chapter = "chapter_" + str(c_counter)
			content = div.text
			for poems in div.find_all('lg'):
				if poems.get('type') == 'poem':
				poem = "poem_" + str(p_couter)
				p_content = poems.text
				chapter_list.append(chapter, poem, p_content])
				p_counter += 1
		c_counter += 1
		p_counter = 1

poems  = pd.DataFrame(chapter_list, columns = {['chapter', 'poem', 'content'])
```
````
```{code-cell}
:tags: [remove-input, hide-output]
import pandas as pd
chapter_list = []
c_counter = 1
p_counter = 1 
	for div in root.find_all('div'):
		if div.get('type') == 'chapter':
			chapter = "chapter_" + str(c_counter)
			content = div.text
			for poems in div.find_all('lg'):
				if poems.get('type') == 'poem':
				poem = "poem_" + str(p_couter)
				p_content = poems.text
				chapter_list.append(chapter, poem, p_content])
				p_counter += 1
		c_counter += 1
		p_counter = 1

poems  = pd.DataFrame(chapter_list, columns = {['chapter', 'poem', 'content'])
poems
```

As you can see we now have the poems numbered per chapter, and each chapters nicely numbered as well. This Datarfame will make a nice and ordered dataset for further analysis or presentation.

Having extracted different types of content and saving them to text and csv, we could, for example, use these for further analyses. Remember that saving files without specifying a pathname saves them to the root folder of Jupyter. This folder might clutter up quickly and it is wise to clean it up regularly or keep it clean by specifying a pathname to a specific folder.






