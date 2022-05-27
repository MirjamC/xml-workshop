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

# 7. Practical: Extract information from the Alto/Didle format with ElemenTree

In this lesson ,we are going to work with the Alto and Didle format. As shown in lesson ***?***, the Alto and Didle are connected to each other. 
The Alto stores the plain text and the Didl the metadata of the newspaper. For this lesson, we assume that you have followed the practical lesson 4. 

This lesson contains the following content
- Load the Alto file and examine the structure <span style="color:#ef6079">(*basic*)</span>;
- Extract the complete content of a newspaper page from the Alto file <span style="color:#ef6079">(*basic*)</span>
- Load the Didl file and examine the structure <span style="color:#ef6079">(*basic*)</span>;
- Extraxt newspaper metadata from the Didl file. <span style="color:#ef6079">(*basic*)</span>
- Extract all seperate articles from the total newspaper from the Didl file <span style="color:#ef6079">(*moderate*)</span>
- Extract all seperate articles from a specific newspaper from the Didl file <span style="color:#ef6079">(*advanced*)</span>

Open a new Jupyter Notebook and type all code examples and code exercises in your Notebook. 

## Load the Alto file and examine the structure

```{admonition} Exercise
:class: attention
Import the package and load the xml file. 
```

````{admonition} Solution
:class: tip, dropdown
```{code-cell}
    import xml.etree.ElementTree as ET

	tree = ET.parse('data/alto_id1.xml')
	root_alto = tree.getroot()
```
````

```{note}
We work with two xml file in this lesson. Therefore, we name the root of the xml file accordingly to the type of the xml.
Thus 'root_alto' for the alto xml and 'root_didl' for the Didl xml. 
```

Before you can extract content from a XML file, you have to see what is inside and how it is structured. 

```{admonition} Exercise
:class: attention
Show the XML file in your Notebook
```

````{admonition} Solution
:class: tip, dropdown
```Python
print(ET.tostring(root_alto, encoding='utf8').decode('utf8'))
```
````

*** print hier de output 

Our goals is to extract the text of the news paper content from the XML file, and store this in a document with the pagenumber. 

So, let's start to see if we can find where the textual content of the news paper is stored. 

```{admonition} Exercise
:class: attention
Scroll through the XML file and see if you can find the element in which the text of the newspaper is stored. Hint: one of the news articles mentiones the
word 'spoorwegmaatschappij'. 
```

```{admonition} Solution
:class: tip, dropdown
The content of the news paper articles is stored in the element 'ns0:String', for example:

	<String ID="P1_ST00323" HPOS="244" VPOS="2387" WIDTH="318" HEIGHT="35" CONTENT="spoorwegmaatschappij" WC="0.99" CC="88668080809486709965"/>
```

```{admonition} Exercise
:class: attention
If we compare the element 'String' to our example XML, we see that there is a difference in how the content is stored. What is the difference? 
```

```{admonition} Solution
:class: tip, dropdown
The content of the elements of the example XML were stored als values from the elements. 
The content of the String element is stored in an attribute called 'CONTENT'. 
```

```{admonition} Exercise
:class: attention
There are a lot of nested element in this XML file. What are the parents, grandparents and grandgrandparents of the 'String' element? Are there even more parents?
```

```{admonition} Solution
:class: tip, dropdown
- The parent of the 'String' element is 'Textline'
- The grandparent is 'TextBlock'
- The grandgrandparent is 'Page'.
- The complete line is alto/Layout/Page/TextBlock/Textline/String
```
Now we know some important information about this Alto file, so let's see if we can extract the content. 

## Extract the complete content of a newspaper page from the Alto file

We will start by extracting all the text, without worrying about the division between the articles. 

```{admonition} Exercise
:class: attention
As you have seen, the plain text of the news paper is stored in the 'CONTENT' attribute of the 'String' element. How can you extract the values from attributes?
```

```{admonition} Solution
:class: tip, dropdown
This can be done with the .get method, for example: book.get('id'). 
```

In lesson 4 we learned that is is possible to acces the elements with a for loop, like
```Python
for book in root.findall('book'):
```
However, as you have seen above, the element 'String' is a grandgrandgrandgrandchild from the start element 'alto'.
One way to access the String element is by typing all ancestors, leading to a code like:
```Python
for page in root_alto.findall('alto/Layout/Page/TextBlock/Textline/String'):
```

However, we preferably avoid that, since it takes a lot of time and can easily lead to mistakes. 
```{admonition} Exercise
:class: attention
In lesson 4, we learned a way to escape all the ancestors, how did we do this?
```

````{admonition} Solution
:class: tip, dropdown
By adding './/', for example 
```Python
for book in root.findall(''.//author'):
```
````

So, we can easily loop through all String elements by using the .// escape, and we can extract the content from the CONTENT attribute with the .get method. 

````{admonition} Exercise
:class: attention
```Python
Create the for loop to extract the content. This loop looks like this:
    for text in the String elements:
		print(the value of the CONTENT attribute)
```
Complete the code and run it. What happens?
````

````{admonition} Solution
:class: tip, dropdown
```Python
	for page in root_alto.findall('ns0:String'):
		print(page.get('CONTENT'))
```
The code doesn't produce any output. 		
````

### Namespaces 

So, what is going on? Why is not there any output?
As described in lesson ***2***, some XML documents make use of *namespaces*. 
If we look at the first line of the Alto file, we see:

```XML
<?xml version='1.0' encoding='utf8'?>
<ns0:alto xmlns:ns0="http://schema.ccs-gmbh.com/ALTO">
```

The second line shows us that this XML make use of namespaces. 
'ns0' is used as a shortcut for 'http://schema.ccs-gmbh.com/ALTO'. 

We have now two options to handle the namespaces in ElemenTree:
1. Type the namespace before the element name between curly brackets: {http://schema.ccs-gmbh.com/ALTO}

```Python
for book in root.findall('.//{http://schema.ccs-gmbh.com/ALTO}String'):
    content = book.get('CONTENT')
    print(content)
```

2. Declare the namespace in elemenTree. This provides Python with a dictionary of the used namespaces, which it can then use.

```{code-cell}
ns = {'ns0': 'http://schema.ccs-gmbh.com/ALTO'}
```

Now you can use the abbreviation of the namespace in your code:
``` Python
for page in root_alto.findall('.//ns0:String', ns):
    content = page.get('CONTENT')
    print(content)
```

```{note}
If you declare the namespace in Python with a dictionary, do not forget to put ', ns' after your element name in the *.findall*. 
Without this 'ns', Python does not recognize the namespace. 
You only have to declare the namespaces once, Python will then recognize them in de rest of your Jupyter Notebook.
```

For the remainder of this lesson, we will use the second option. 

```{admonition} Exercise
:class: attention
Choose one of the namespace options and run the code to extract all the text from the CONTENT attribute. 
```

````{admonition} Solution
:class: tip, dropdown
```
for page in root_alto.findall('.//ns0:String', ns):
    content = page.get('CONTENT')
    print(content)	
```
```` 

This leads to the following output:

```{code-cell}
:tags: [remove-input, hide-output]
import xml.etree.ElementTree as ET

tree = ET.parse('data/alto_id1.xml')
root_alto = tree.getroot()

for page in root_alto.findall('.//ns0:String', ns):
    content = page.get('CONTENT')
    print(content)
```

### Make the output more readable

As you can see, the text is printed in seperate words, that all appear in one long list. So, this is quit unreadable. We can store the text in a *string* 
variable in which we concatenate all words. 

```{code-cell} ipython3
:tags: [hide-output]
ns = {'ns0': 'http://schema.ccs-gmbh.com/ALTO'}

all_content = ""

for page in root_alto.findall('.//ns0:String', ns):
	content = page.get('CONTENT')
	all_content = all_content + " " + content
	
print(all_content)
```

The content is now more readable, however, it is still one long blob of the complete text of the newspaper.
As you can see in the xml file, the content is divide into sections. 

```{admonition} Exercise
:class: attention
Look at the xml file. There are different elements that divide the text. Which element would likely be used to seperate articles from 
each other?
```

```{admonition} Solution
:class: tip, dropdown
The element 'TextBlock'
```

Now that we know how we can divide the various session, let's put this in the code.
Instead storing all the output into one variabele, we create a variable, store it with the information of one session.
Then we print the variabele and empty it, so it is clean for a new session.

In code, this looks like this: 


```{code-cell} ipython3
:tags: [hide-output]
article_content = ""

for book in root_alto.findall('.//ns0:TextBlock', ns):
    for article in book.findall('.//ns0:String', ns):
        content = article.get('CONTENT')
        article_content = article_content + " " + content
    print(article_content)
    print("") ## add a linebreak between the seperate sessions
    article_content = ""
```

Now we have a page of plain text that is better structured. 
The only thing left is to retreive the page number, and then we'll have all the information to store this data
intro a textfile or a csv. 

```{admonition} Exercise
:class: attention
Look at the xml file. Where can we find the page number?
```

```{admonition} Solution
:class: tip, dropdown
The page number is stored in the 'Page' element. 
```

```{admonition} Exercise
:class: attention
Write the code to extract the page number from the xml. 
```

````{admonition} Solution
:class: tip, dropdown
```Python
for book in root_alto.findall('.//ns0:Page', ns):
    pagenr = book.get('ID')
    print(pagenr)
```
````

The page number is:

```{code-cell}
:tags: [remove-input, hide-output]
for book in root_alto.findall('.//ns0:Page', ns):
    pagenr = book.get('ID')
    print(pagenr)
```

## Load the Didl file and examine the structure ;

We have now a more readable page and the corresponding page number. However, if we store this then later we will have
no idea from which newspaper this page was. In lesson 3 we described that we can find metadata corresponding to an alto file in an Didle file. 
The alto and didle file have the same identifier, so you can match them.

In this case, the both have the identifier 1. 

```{admonition} Exercise
:class: attention
Load the corresponding Didl file in your notebook. Name the root 'root_didl'. Look at the structure of the file. 
```

````{admonition} Solution
:class: tip, dropdown
```Python
	tree = ET.parse('data/didl_id1.xml')
	root_didl = tree.getroot()
	print(ET.tostring(root_didl, encoding='utf8').decode('utf8'))
```
````

```{admonition} Exercise
:class: attention
Look at the Didle file and see if you can find in which element the title of the newspaper is scored. Hint: the title is 'Algemeen Handelsblad'. 
What parent of this element contains all information we need to extract the title and the publication date?
```

````{admonition} Solution
The title is stored in the element 'title', and the publication date in the element 'date'. They can both be found in the element 
'Resource'. 
```

## Extraxt newspaper metadata from the Didl file.

We see that the block resource containts all the information we want. If we look closely at the file, we see that there are multiple
element with the name 'resource', but the one we want is the first. If you want all the information from all resource blocks, we use
the findall method as we did before. However, we now only want information from the first block. In that case, you can just simply use
find(). This will returns the first element it occurs. The rest of the syntax stays the same. 


```{admonition} Exercise
:class: attention
Write a code that gets the only the first 'component' element, and then from this element create a for loop that loops through the dcx element. 
Extract the title of the newspaper and the publication date. Store them in two seperate variables. 
```

````{admonition} Solution
```
ns_didl = {'dc': 'http://purl.org/dc/elements/1.1/',
          'ns2': 'urn:mpeg:mpeg21:2002:02-DIDL-NS', 
          'ns4' : 'info:srw/schema/1/dc-v1.1' }

for item in root_didl.find('.//ns2:Resource', ns_didl):
    for info in item.findall('ns4:dcx', ns_didl):
        title = info.find('.//dc:title', ns_didl).text
        date = info.find('.//dc:date', ns_didl).text  
```
```

-- toon hier de uitkomst zonder input
```{code-cell}
ns_didl = {'dc': 'http://purl.org/dc/elements/1.1/',
          'ns2': 'urn:mpeg:mpeg21:2002:02-DIDL-NS', 
          'ns4' : 'info:srw/schema/1/dc-v1.1' }

for item in root_didl.find('.//ns2:Resource', ns_didl):
    for info in item.findall('ns4:dcx', ns_didl):
        title = info.find('.//dc:title', ns_didl).text
        date = info.find('.//dc:date', ns_didl).text  
```

Now we can store the content of this newspaper page in a text file with as name the title of the newspaper, the publication date and the 
page number. 

We can create the filename like this:

```
filename = f([titl
```

```{admonition} Exercise
:class: attention
Save the content in a file.
```

```{admonition} Solution

answer.  

```

## Extract all seperate articles from the total newspaper from the Didl file

As you saw in the above sections, the Alto format has no clear seperation between the articles and is therefore  especially suitable when you 
are interested in the complete newspaper page.

However, there are a lot of cases in which you would be interested in the seperate articles en metadata about this articles (for example, the type of article) 

As for the collection of the national library, you can use the Didle xml to extract these types of information and to gather the articles. 

```{admonition} Exercise
:class: attention
Look at the Didl file, do you see information about the articles?
```

```{admonition} Solution
Yes, they are stored in the 'resource' elements.  
```

As you can see, there are block with information about the articles. However, the articles self are not present in the Didl, but we can 
retreive them through there identifier. We therefore are going to perform to steps:

- Extract article information and identifier from the didle
- Download the articles and extract the plain text

We start by extracting the subject, title and identifier from the resource element. However, there is also
other information stored in the resource elements, such as the news paper title. 

You can distinguish the articles by the newspaper metadata based on the element 'subject'.
All articles have a subject ('artikel', 'familiebericht' etc) whilst the other metadata don't.

We can 

```{admonition} Exercise
:class: attention
Write a for loop that extract the subject, title and identifier of each article
and print them. 
```

```{admonition} Solution
Yes, they are stored in the 'resource' elements.  
```

## Extract all seperate articles from a specific newspaper from the Didl file





