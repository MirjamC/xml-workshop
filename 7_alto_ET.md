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

# 7. Practical: Extract information from the Alto format with ElemenTree


In this lesson, we are going to extract the plain text and some additional information from an Alto file containing a Dutch newspaper. 
We assume that you have followed the practical lesson 4. We will reference to corresponding parts of that lesson so you can check how it worked. 

We follow these steps:
- Load the XML file;
- Examine the structure of the XML file;
- Extract the plain text;
- Divide the plain text into seperate articles;
- Extract the page number;
- Save the content in one file and in seperate textfiles; 

Open a new Jupyter Notebook and type all code examples and code exercises in your Notebook. 
(see explantion in {ref}`ET:import`)

## Import ElemenTree and import the xml file

```{admonition} Exercise
:class: attention
Import the package and load the xml file. 
```

```{admonition} Solution
:class: tip, dropdown
    import xml.etree.ElementTree as ET

	tree = ET.parse('xml-workshop/data/alto.xml')
	root = tree.getroot()
```

## Examine the structure of the file

Before you can extraxt content from a XML file, you have to see what inside and how it is structured. 

```{admonition} Exercise
:class: attention
Show the XML file in your Notebook
```

```{admonition} Solution
:class: tip, dropdown
	print(ET.tostring(root, encoding='utf8').decode('utf8'))
```

As you can see, this XML file has a lot more elements and attributes than our example file. 
Our goal is to extraxt the text from the news paper, to seperate the text into articles and to store them on our computer with the page number. 

So first, lets see if we can see where the textual content of the news paper is stored. 

```{admonition} Exercise
:class: attention
Scroll through the XML file and see if you can find the element in which the text of the newspaper is stored. Hint: one of the news articles mentioned
'olifant'. 
```

```{admonition} Solution
:class: tip, dropdown
The content of the news paper articles is stored in the element 'ns0:String'

	<String ID="P3_ST00483" HPOS="557" VPOS="3994" WIDTH="109" HEIGHT="26" CONTENT="olifant" WC="0.99" CC="6000010"/>
	
```

```{admonition} Exercise
:class: attention
If we compare the element 'String' to our example XML, we see that there is a difference in how the content is stored. What is the difference? 
```

```{admonition} Solution
:class: tip, dropdown
The content of the elements of the example XML where stored als values from the elements. 
The content of the String element is stored in an attribute called 'CONTENT'. 
```

```{admonition} Exercise
:class: attention
There are a lot of nested element in this XML file. What are the parents, grand parents and grand grandparents of the 'String' element? Are their more parents than this?
```

```{admonition} Solution
:class: tip, dropdown
The parent of the 'String' element is 'Textline'
The grandparent is 'TextBlock'
The grandgrandparent is 'Page'.
The complete line is alto/Layout/Page/TextBlock/Textline/String
```
Now we know some first important information about this Alto file, so let's see if we can extract the content. 

## Extract the plain text

We will start by extracting all the text, without worrying about the division between the articles. 

```{admonition} Exercise
:class: attention
As you have seen, the plain text of the news paper is stored in the 'CONTENT' attribute of the 'String' element. How can you extract the values from attributes?
```

```{admonition} Solution
:class: tip, dropdown
This can be done with the .get method, for example: book.get('id'). 
```

We learned in lesson 4 that you can acces the elements with a for loop, like
```
for book in root.findall('book'):
```
However, as you have seen above, the element 'String' is a grandgrandgrandgrandchild from the start element 'alto'.
One way to access the String element is by typing all ancestors, leading to a code like:
```
for book in root.findall('alto/Layout/Page/TextBlock/Textline/String'):
```

However, we preferably avoid that, since it takes a lot of time and leads easliy to mistake. 
```{admonition} Exercise
:class: attention
In lesson 4, we learned a way to escapte all the ancestors, how did you do this?
```

```{admonition} Solution
:class: tip, dropdown
By adding './/', for example  for book in root.findall(''.//author'):
```

So, we can easily loop through all String elements by using the .// escape, and we can extract the content from the CONTENT attribute with the .get method. 

```{admonition} Exercise
:class: attention
Create the for loop to extract the content. This loop looks like this:
    for text in the String elements:
		print(the value of the CONTENT attribute)
Complete the code and run it. What happens?
```

```{admonition} Solution
:class: tip, dropdown

	for book in root.findall('ns0:String'):
		print(book.get('CONTENT'))

The code doesn't produce any outcome. 		
```

### namespaces

So, what is going on? Why isn't there any output?
As described in lesson ***2***, some XML documents make use of *namespaces*. 
If we look at the first line of the Alto file, we see:

```
<?xml version='1.0' encoding='utf8'?>
<ns0:alto xmlns:ns0="http://schema.ccs-gmbh.com/ALTO">
```

The second line shows us that this XML make use of namespaces. 
'ns0' is used as a shortcut for 'http://schema.ccs-gmbh.com/ALTO'. 

We have now to options to handle the namespaces in ElemenTree:
1. Type the namespace before the elementname between curly brackets: {http://schema.ccs-gmbh.com/ALTO}

```
for book in root.findall('.//{http://schema.ccs-gmbh.com/ALTO}String'):
    content = book.get('CONTENT')
    print(content)
```

2. Declare the namespace in elemenTree. You therefore provide Python with a dictionary of the used namespaces, which it can use.

```{code-cell}
ns = {'ns0': 'http://schema.ccs-gmbh.com/ALTO'}
```

Now you can use the abbreviation of the namespace in your code:
``` 
for book in root.findall('.//ns0:String', ns):
    content = book.get('CONTENT')
    print(content)
```

```{note}
If you declare the namespace in Python with a dictionary, to not forget to put ', ns' after your elementname in the findall. 
Without this ns, Python does not recognize the namespace. 
You only have to declare the namespaces ones, Python will then recognize them in de rest of your Jupyter Notebook.
```

For the remainder of this lesson, we will use the second option. 

```{admonition} Exercise
:class: attention
Choose one of the namespace option and run the code to extract all the text from the CONTENT attribute. 
```

```{admonition} Solution
:class: tip, dropdown
	for book in root.findall('.//ns0:String', ns):
		print(book.get('CONTENT'))		
``` 

## Divide the plain text into seperate articles

As you can see, the text is printed in seperate words, that all appear in one long list. So, this is quit onreadable. We can store the text in a *string* variable, 
in which we concatenate all words. 

```
all_content = ""

for book in root.findall('.//ns0:String', ns):
    content = book.get('CONTENT')
    all_content = all_content + " " + content
```

The content is now more readable, however, it is still one long blob of the complete text of the newspaper.
We would like to divide the texts in articles. 









### This is old stuff!







```{admonition} Exercise
:class: attention
Look at the XML structure. Which elements do we need do find the title and the description?
```


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

```{admonition} Exercise
:class: attention
Alter the code above to retreive all the descriptions and print out the descriptions. 
```

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

## Extract name and surname of the author
You can use the same method as described above to extraxt all names and surname from the authors from the XML. 
However, if we look at the structure of the xml file, there is a different between the place of the elements 'title' and 'description'
and the elements 'name' and 'surname'. 

```
<catalog>
	<book id="bk101">
		<author>
			<name>Matthew</name>
			<surname>Gambardella</surname>
		</author>
		<title>XML Developer's Guide</title>
		<genre>Computer</genre>
		<price>44.95</price>
		<publish_date>2000-10-01</publish_date>
		<description>An in-depth look at creating applications with XML.</description>
   </book>
```


```{admonition} Exercise
:class: attention
Look at the XML snippet above. What is the difference between the element 'title' and the element 'name'?
```

```{admonition} Solution
:class: tip, dropdown
	
The element 'title' is a child of the element 'book'. 
The element 'name' however, is a child of the element 'author' and a *sub*child of the element 'book'. 
	
```

Because of the difference between the place of the elements, we need to alter our code a bit. Instead of one for loop, that iterates through all the 'book' elements, 
we also need a for loop that runs through the 'author' element of book. We can do this with the following code:

```{code-cell}
:tags: [hide-output]

# This cell should have its output hidden!
for book in root.findall('book'):
    for author in book.findall('author'):
        name = author.find('name').text
        print(name) 
```

```{admonition} Exercise
:class: attention
The above code extraxts only the name of an author. Alter the code, so that it extracts both the name and the surname. 
```

```{admonition} Solution
:class: tip, dropdown
	for book in root.findall('book'):
		for author in book.findall('author'):
			name = author.find('name').text
			surname = author.find('surname').text
			print(name, surname) 
	
```

## Extraxt the book identifier

As you can see in the XML, each book has its own ***identifier***. As books can have the same name, and authors can have written multiple books, it 
is good practise to always use the identifier to point to a specific item. 

In the previous exercises, we extracted the content that was presented between the tags of an element.
For example:


```
<title>XML Developers Guide</title>
```

In this example, you see that the title 'XML Developer's guide' is stored between the tags <title> and </title>. We extracted this content by adding '.text'. 

```{admonition} Exercise
:class: attention
Look at this example of the 'book' element with its identifier. What is the difference between the place of the content of the identifier and the
place of the content of the title?
	```
		<book id="bk101">
		</book>
	```
```

```{admonition} Solution
:class: tip, dropdown
The content of the identifier is stored in an *atrribute* of the 'book' element, with the name 'id'. 
	
```

To extract content from attributes, we need to use a 'get' method. 
We still use the for loop to iterate through all the books, but instead of the content of certain elements, we now extract the content of the attribute. 

```{code-cell}
:tags: [hide-output]

# This cell should have its output hidden!
for book in root.findall('book'):
    identifier = book.get('id')
    print(identifier)

```

## Structure all information

We can combine the different codes we use above into one cell. 
Therefore, we can use the following scheme:

```
Iterate through all books	
	Get content from id attribute
	Get title content	
	Get description content	
	Iterate through all authors
		Get name
		Get surname
	Print id, title, description, name and surname
```

```{admonition} Exercise
:class: attention
Create the code that extraxts all information we used so far, from every book. And print this information (see scheme above). 
```

```{admonition} Solution
:class: tip, dropdown
	for book in root.findall('book'):
		identifier = book.get('id')
		title = book.find('title').text
		description = book.find('description').text
		for author in book.findall('author'):
			name = author.find('name').text
			surname = author.find('surname').text
		print(identifier, title, description, name, surname)
```	

This leads to the following output:

```{code-cell}
:tags: ["hide-input"]

# This cell should have its input hidden!
for book in root.findall('book'):
	identifier = book.get('id')
	title = book.find('title').text
	description = book.find('description').text
	for author in book.findall('author'):
		name = author.find('name').text
		surname = author.find('surname').text
	print(identifier, title, description, name, surname)

```

As you can see, it displays all information we wanted, but the output is quite unreadable. For example, it is not clear which part of the content belongs
to the title, and which to the description. 

To make the output more readable, we can put text before our output variabelen. In Python, this can be done like this:
```
print(f"This is the string we type and {this_is_the_variable}")
```

So in our example, this leads to:

```{code-cell}
:tags: ["hide-output"]

# This cell should have its input hidden!
for book in root.findall('book'):
    identifier = book.get('id')
    title = book.find('title').text
    description = book.find('description').text
    for author in book.findall('author'):
        name = author.find('name').text
        surname = author.find('surname').text
    print(f"Identifier= {identifier } title= {title} description= {description} name= {name} {surname}")
```

As you can see, we can now detect the various parts that we extracted. However, it is still not easy to read.
To resolve this, we can add linebreaks between each variable and between the different books. We add a line break by adding '\n' after each variable, 
leading to the following code:

```{code-cell}
:tags: ["hide-output"]

# This cell should have its input hidden!
for book in root.findall('book'):
    identifier = book.get('id')
    title = book.find('title').text
    description = book.find('description').text
    for author in book.findall('author'):
        name = author.find('name').text
        surname = author.find('surname').text
    print(f"Identifier= {identifier }\n title= {title}\n description= {description} \n name= {name} {surname}\n")

```

Well, that output looks way better, doesn't it?

## Store the information in a .csv or .txt file.
We show you how to store the output in two different ways:
- as one file with the information of all books in .csv format (which, for example, can be opened in Excel)
- as one textfile per book. 

### Store in one file
The easiest way to store and save Python output in one file is through storing it in a datframe from the Python package 'Pandas' and then save this frame. 
You can add data directly from the for loops we created above in a pandas dataframe, but we prefer the method in which you first create a list and then transform
this list in the output, as Pandas DataFrame execution can become fairly slow with large amounts of data. 

To create a list, we first have to declare an empty list. This is done with the following syntax:
```
booklist = []
```

Now, we alter our for loop a bit. Instead of printing the output to the screen, as we did above, we store our output in a list. 
We therefor use the following code:
```{code-cell}
:tags: ["hide-output"]

# This cell should have its input hidden!
booklist = []

for book in root.findall('book'):
    identifier = book.get('id')
    title = book.find('title').text
    description = book.find('description').text
    for author in book.findall('author'):
        name = author.find('name').text
        surname = author.find('surname').text
    booklist.append([identifier, title, description, name+" "+surname])
```
This leads to a list, called 'booklist', in which for every book all information is stored. 

We can then easily transform this list to a pandas DataFrame. 
To do so, we need to import pandas first with the comment
```
import pandas as pd
```

Then we type:
``` 
books = pd.DataFrame(booklist, columns=("identifier", "title", "description", "name")
```

This code works as follows. You declare the variable 'books', which wil be used to store all the information.
Then you let Python know that you want to create a DataFrame. The content of this dataframe is the list 'booklist', which we just created. 
We then tell Python what we want the name of all columns to be (this is in the same order as the order of the variables in the list). 

You can show the dataframe you just created by typing:
``` 
books
```

This results in the following output:
```{code-cell}
:tags: ["hide-input"]

# This cell should have its input hidden!
import pandas as pd
books = pd.DataFrame(booklist, columns={"identifier","title", "description", "name"})
books
```

Now we can save this dataframe into a csv file by typing:
```
books.to_csv('book.csv')
``` 
### Create a textfile per book

If you want to create a textfile for every book, you can add the code directly in your for loop. 

First, you have to declare a textfile in Python and give it a name. Then, you can open the file and write content to it. After this, you close the file. 
You can try this with the following code:

```
myfile = open('test.txt', 'w')
myfile.write('This is just a test file')
myfile.close()
```

```{note}
By default, Python stores the text file in the same folder as where you run your Jupyter Notebook. You can alter this by adding a path to your textfile, for example:
``` myfile = open('C:/Users/Documents/test.txt', 'w') ```
Please remember to use a backward slash (/) between the folders
```

With a few alterations, we can use this code to save our book information per file. 
First, we give the textfile the name of the book identifier. we can do that by adding the variable into the name of the file like this:
```
 myfile = open(identifier+'.txt', 'w')
```

Then, we create the content of the file based on the content we exracted from the book. 
```
myfile.write(name+" "+surname + "\n" + title + "\n" + description)
```

If we put these line into our for loop, Python will save every book with its own name and own information. 
This code looks like this:
```
for book in root.findall('book'):
    identifier = book.get('id')
    title = book.find('title').text
    description = book.find('description').text
    for author in book.findall('author'):
        name = author.find('name').text
        surname = author.find('surname').text
    myfile = open(identifier+'.txt', 'w')
    myfile.write(name+surname + "\n" + title + "\n" + description)
    myfile.close()
```

## Extra: Filter information

You can also search for specific elements in you XML. For example, only the title information from the book 'bk109'.
To do so, you can start with the same for loop as we created in this lessons. However, before you print the output, you first check
if you have the element you want (in this case: book 109). This can be done with an 'if' statement and it looks like this:

```{code-cell}
for book in root.findall('book'):
    if book.attrib['id']=="bk109":
        title = book.find('title').text
        print(title)
```

You can also search the content from xml elements, searching the content for a match. For example, if we want to print all title that contain the word 'XML', 
we can use the following code:

```{code-cell}
for book in root.findall('book'):
    title = book.find('title').text
    if "XML" in title:
        print(title)
```

```{note}
Strings in Python are capital senstive! This means that 'XML' is not equal to 'xml' or 'Xml' in Python. 
```


```{admonition} Exercise
:class: attention
Print out the title of all books that have England in their description. 
```

```{admonition} Solution
:class: tip, dropdown
	for book in root.findall('book'):
		description = book.find('description').text
		if "England" in description:
			print(book.find('description').text)
```	
