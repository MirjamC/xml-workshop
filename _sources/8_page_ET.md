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

# 8. Practical session: Page and Elementree

In this section we will use ElemenTree to extract data from Page format XML files and print this with the reading order. As you should by now be a bit more familiar with Python and handling XML explanations will be a bit more brief. When needed, refer back to previous sections.

We will follow these steps:

- Import the package and the Page file;
- Examine the structure;
- Extract reading order;
- Extract the plain text;
- Print the content with reading order.

Open a new Jupyter Notebook and type all code examples and code exercises in your Notebook. (see explanation in ET:import)

### Import package and load the file

We first need to prepare the Notebook  by importing hte package we need and loading the XML file into the enviroment.

```{admonition} Exercise
:class: attention
Import the ElemenTree package and load the XML file into your Notebook.  You can look back to lesson 4 if you need a reminder on how to do this. The XML file is named 'page.xml' and is stored in the data folder of this workshop.
```

````{admonition} Solution
:class: tip, dropdown
```
import xml.etree.ElementTree as ET	
tree = ET.parse('data/page.xml')
root = tree.getroot()
```
````

### Examine the structure of the file

In order to extract the required information from the file, we have to examine the structure.

```{admonition} Exercise
:class: attention
Print the file in your Notebook or look at the file in your browser, either way you prefer. 
```

```{code-cell}
:tags: [remove-input, hide-output]
import xml.etree.ElementTree as ET	
tree = ET.parse('data/page.xml')
root = tree.getroot()
print(ET.tostring(root, encoding='utf8').decode('utf8'))
```

The page XML contains a lot of information that is not the text. This information seems to describe something about the location of the text on the scan. While interesting, we want to be able to extract the ***text***. Therefore, we need to know in which element this content is stored, and whether this is stored as a value of the tags or as an attribute. 

```{admonition} Exercise
:class: attention
Look at the XML structure, how is the content stored?
```
```{admonition} Solution
:class: tip, dropdown
The content is stored in an element called 'Unicode'. 
```

Most page XML files contain a reading order. This reading order guides the user through the file and indicates what the right order of all text elements is. 
To determine the correct reading order, we need three clues. 

```{admonition} Exercise
:class: attention
Look carefully at the XML. What information do we need to correctly display the reading order?
```
```{admonition} Solution
:class: tip, dropdown
- The id attribute of each TextRegion element
- The OrderedGroup id for each TextRegion
- The index of each region
```
Now that we know how the file is structured, and where the content we need is stored, we can start extracting the output

### Extracting the content and reading order

Remember namespaces? Before we start to extract the data we are interested in we need to stop for a moment and re-examine the file to see if we need to take namespaces into account.

```{admonition} Exercise
:class: attention
Are there any namespaces in the file that we have to take into account? 
If there are, how can we declare these?
```

````{admonition} Solution
:class: tip, dropdown
- Yes, there are multiple namespaces to take into account. These are declared in the root of the XML:
```
1. ns0:PcGts xmlns:ns0="http://schema.primaresearch.org/PAGE/gts/pagecontent/2010-03-19" 
2. xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
```
- If you remember from section 7, there are two ways of using namespaces:
	1. Type the namespace before the element name between curly brackets: {http://schema.primaresearch.org/PAGE/gts/pagecontent/2010-03-19}
	2. Declare the namespace in ElementTree. This provides Python with a dictionary of the used namespaces, which it can then use.
````


```{admonition} Exercise
The text content that we wish to extract is stored in the Unicode element. 
Use Python and ElementTree to extract this content.

	*Dont't forget about namespaces!! *
```

````{admonition} Solution
:class: tip, dropdown
The following code should print out all the content.
```
## declare the namespace
ns = {'ns0': 'http://schema.primaresearch.org/PAGE/gts/pagecontent/2010-03-19'}
## loop through all the Unicode elements and print the text data from each element
for newspaper in root.findall('.//ns0:Unicode', ns):
    print(newspaper.text)
```
````

```{code-cell}
:tags: [remove-input, hide-output]
ns = {'ns0': 'http://schema.primaresearch.org/PAGE/gts/pagecontent/2010-03-19'}
for newspaper in root.findall('.//ns0:Unicode', ns):
    print(newspaper.text)
```

Now we have all the text content, but it is not in the right order. We need to add the 'TextRegion id' to get the data to print out in the right order. 

```{admonition} Exercise
What should we pay attention to when adding the TextRegion id?
```

```{admonition} Solution
:class: tip, dropdown
The content we are interested in is the value between the tags. However, the TextRegion id is an *attribute*.
```

Knowing this we will need to use the .get() method to find the TextRegion ids. 

```{admonition} Exercise
Expand the code to also extract the TextRegion id and print it out along with the content per newspaper. 
```

````{admonition} Solution
:class: tip, dropdown
The following code should print out all the content.
```
for newspaper in root.findall('.//ns0:TextRegion', ns):
    regionid = newspaper.get('id')
    for content in newspaper.findall('.//ns0:Unicode', ns):
        print(regionid)
        print(content.text)
```
````

```{code-cell}
:tags: [remove-input, hide-output]
ns = {'ns0': 'http://schema.primaresearch.org/PAGE/gts/pagecontent/2010-03-19'}
for newspaper in root.findall('.//ns0:TextRegion', ns):
    regionid = newspaper.get('id')
    for content in newspaper.findall('.//ns0:Unicode', ns):
        print(regionid)
        print(content.text)
```


Now we have all the data with its corresponding TextRegion id, however it is not very readable. Also, getting the correct reading other from this printout is not the easiest task.
To make our life a bit easier we will put the data into a Pandas Dataframe. 
As seen before in section 4 we will first put the whole set into a list.

```{admonition} Exercise
Instead of printing the TextRegion id and content, chagne the code to it into a list. 
```

````{admonition} Solution
:class: tip, dropdown
The code below should store the TextRegion id and content into a list.
```
## Create an empty list
content_list = []

for newspaper in root.findall('.//ns0:TextRegion', ns):
    regionid = newspaper.get('id')
    for content in newspaper.findall('.//ns0:Unicode', ns):
		content = content.text
	## append the regionid and content to the list
    content_list.append([regionid, content])
```
````


Let us just peek at the list to see if everything went as expected.
`
```{admonition} Exercise
Print out the list that was made in the previous exercise to see if it was created correctly.
```

````{admonition} Solution
:class: tip, dropdown
```
print(content_list)
```
````

```{code-cell}
:tags: [remove-input, hide-output]
content_list = []
for newspaper in root.findall('.//ns0:TextRegion', ns):
	regionid = newspaper.get('id')
	for content in newspaper.findall('.//ns0:Unicode', ns):
		content = content.text
	content_list.append([regionid, content])
print(content_list)
```

Now we have a list containing the TextRegion id and the content we can transform this into a Dataframe. can easily make a dataframe using the list we have just created with as column 'region' and 'content'.


```{admonition} Exercise
Make a dataframe from the list we have just created.
```
```{note}
Pay close attention to the order of the input list and column names! The first item added to the list should also have its name first in the columns parameter.
```

````{admonition} Solution
:class: tip, dropdown
```
import pandas as pd
content_table = pd.DataFrame(content_list, columns = [Region", "Content"])
```	
````

As before, check the result to make sure everything went as expected.
```{admonition} Exercise
Check if the Dataframe is made correctly. Remember that running (and not printing) the variable it is stored in keeps the formatting more readable in case of Dataframes.
```

````{admonition} Solution
:class: tip, dropdown
```
content_table
``` 
````

```{code-cell}
:tags: [remove-input, hide-output]
import pandas as pd
content_table = pd.DataFrame(content_list, columns = ["Region", "Content"])
content_table
```

Finally we can now save the dataframe to csv, after which it can be used for further research or manipulation. 

```
content_table.to_csv('page_content.csv')
```


### Automatically order in the right way

Using the XML file  and the information about the reading order in the csv file it is possible to order the file in the correct reading order manually. 
However this is a lot of work and when there are multiple, or very large files this is not the best use of our time. 
Luckily Python offers us ways to automate this.

Because the information about the reading order and indexes stored in a different location than the content itself we will go through three steps to get this done. 

- From the XML we will take three attributes that determine te order. These will be stored into a Python dictionary [Python dictionaries]. These attributes are: *groupnr*, *regionRef*, and *index*
- We retrieve the content and region information.
- We connect the region information to the group and index. 

This can than be stored in a dataframe and sorted. 

```{admonition} Exercise
Using Python, extract the attribuites we want from the XML.
```

````{admonition} Solution
:class: tip, dropdown
```
for order in root.findall('.//ns0:ReadingOrder', ns):
	for group in root.findall('.//ns0:OrderedGroup', ns):
		groupnr = group.get('id')
		print(groupnr)
		for suborder in group.findall('.//ns0:RegionRefIndexed', ns):  
			region = suborder.get('regionRef')
			index = suborder.get('index')
			print(region, index)
```	
````

Printing this information gives us a chance to check if our code is behaving the way we expect. 
However, we wish to further automate the process and store it into a Python dictionary.


#### Example: how to save the above output to a Python dictionary:


```{code-cell}
## First initialize an empty dictionary
dict_order = {}

for order in root.findall('.//ns0:ReadingOrder', ns):
	for group in root.findall('.//ns0:OrderedGroup', ns):
		groupnr = group.get('id')
		for suborder in group.findall('.//ns0:RegionRefIndexed', ns):  
			region = suborder.get('regionRef')
			index = suborder.get('index')
			## the dictionary is filled with the three attributes
			## it sets region as the key and the groupnr and index as a list as value
			dict_order.setdefault(region,[]).append([groupnr, index])
```

Let's print the dictionary to make certain it works.

```{code-cell}
:tags: [hide-output]
print(dict_order)
```

We have previously made the code to obtain the content and the region from the XML file. Now we will combine this by comparing the values from the dictionary with the value of the TextRegion id.


```{code-cell}
for newspaper in root.findall('.//ns0:TextRegion', ns):
	region = newspaper.get('id')
    
	## here we extract from the dictionary the group and index value for the dictionary item that matches the region extracted with the orignal code.
	groupvalues = dict_order[region]
	group = groupvalues[0][0]
	index = groupvalues[0][1]
    
	for content in newspaper.findall('.//ns0:Unicode', ns):
		content = content.text
	## then we can add them to the print statement
	print(group, region, index, content)
```

With this code we merge the reading order values that we stored in the dictionary with the content that we extract with the origial code. However, we still print the code instead of storing it in something more useful.

```{admonition} Exercise
Adapt the code above to store all relevant information in a list.

Don't forget to declare an empty list first.
```

````{admonition} Solution
:class: tip, dropdown
```
content_list = []

for newspaper in root.findall('.//ns0:TextRegion', ns):
    region = newspaper.get('id')
    groupvalues = dict_order[region]
    group = groupvalues[0][0]
    index = groupvalues[0][1]
    for content in newspaper.findall('.//ns0:Unicode', ns):
        content = content.text
    content_list.append([group, index, region, content])
```	
````

Now we have stored the merged information into a list, we can transform the list into a Pandas Dataframe to make use of some of the usefull features of Dataframes.


```{admonition} Exercise
Transform the list into a Dataframe.
```
```{note}
Pay attention to the order of the list items and the columns!
```

````{admonition} Solution
:class: tip, dropdown
```
import pandas as pd
newspaper_with_order = pd.DataFrame(content_list, columns = ["Group", "Index", "Region", "Content"])  
```	
````

We then check the result again.
```{code-cell}
import pandas as pd
content_list = []
for newspaper in root.findall('.//ns0:TextRegion', ns):
	region = newspaper.get('id')
	groupvalues = dict_order[region]
	group = groupvalues[0][0]
	index = groupvalues[0][1]
	for content in newspaper.findall('.//ns0:Unicode', ns):
		content = content.text
	content_list.append([group, index, region, content])
newspaper_with_order = pd.DataFrame(content_list, columns = ["Group", "Index", "Region", "Content"])  
newspaper_with_order
```

Now we have our data in a Dataframe we have some easy options for manipulating the data. One of these is ordering, or sorting, the Dataframe. 
A Dataframe can be sorted by any of its columns, or even multiple columns. The original shape and content is maintained, but the order of the rows is changed to whatever is specified.
The syntax for sorting a Dateframe is:

```
Dataframe.sort_values([column(s) to sort by], [sorting order])
```
In the code below the Dataframe we just made is sorted by 'Group' and 'Index' in ascending order for both. 
Notice that the sorting columns are quoted. When adding more than one column a (comma seperated) list must be passed. The sorting order default is ascending, for descending ascending is set to False.

```{code-cell}
newspaper_with_order = newspaper_with_order.sort_values(['Group', 'Index'], ascending = [True, True])
```
With the reordered Dataframe in hand we can check if the sorting went as planned.


```{admonition} Exercise
Make sure you performed all of the above steps in your notebook and print out the ordered Dataframe.
```

````{admonition} Solution
:class: tip, dropdown
```
newspaper_with_order
```	
````

```{code-cell}
:tags: [remove-input, hide-output]
newspaper_with_order
```
If everything worked as it was supposed to, the new dataframe should now be ordered by the Group and Index columns. Much easier to read, and better structured. Well done!

Of course, as before we could save this Dataframe to disk using .to_csv(), or pass it to other code for further analysis.



