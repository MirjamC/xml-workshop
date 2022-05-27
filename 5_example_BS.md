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

# 5. Practical session: Working with Beautiful Soup

This lesson is divided into three sessions, where every session demonstrates one of the Python packages that was introduced in lesson **3**.
With every package, we follow these steps:
- Load the XML file;
- Examine the structure of the XML file;
- Extract the booktitles and descriptions;
- Extract name and surname of the author;
- Extract the book identifier;
- Structure all information;
- Extra: Filter information

Open a new Jupyter Notebook and type all the code examples and code exercises in your Notebook. 

## Install Beautiful Soup

Beautifull Soup is not a standard Python package, so it needs to be installed first.
This can be done directly in the Jupyter Notebook using:

```
!pip install beautifulsoup4
```

or through the command line (see lesson one)

```
pip install beautifulsoup4
```

## Import Beautiful Soup and load the xml file

Before we can use the package, we have to let Python know we want to use it. We do this by importing the package.
Type the following in a code cell:

```{code-cell}
from bs4 import BeautifulSoup  
```

Now we can use the package to extract data from the XML. 

## Examine the structure of the file


We will first need to load the XML file from which we want to extract information and pass it to BeautifulSoup.
Add a new code cell and type:

```{code-cell}
with open("data/example.xml") as f:
    root = BeautifulSoup(f, 'xml')
```
```{note}
In the code above, alter the 'data/example' with the path to the folder and the filename of where you stored the file. 
```

When you want to extract information from an XML file, it is important that you are familair with the structure of the file. 
There are two ways to do this. 

1. You can open the file in a program like Notepad++ or open it in your browser
2. You can show the file in your Jupyter Notebook with the following code:

```{code-cell} ipython3
:tags: [hide-output]

print(root)
```

## Wat vragen over de structuur bedenken

## Extract the book titles and descriptions

```{admonition} Exercise
:class: attention
Look at the XML structure. Which elements do we need to extract the title and the description?
```


```{admonition} Solution
:class: tip, dropdown
We need the child element 'book', and its subchildren 'title' and 'description'. 
```

Having explored the structure of the XML a bit, we can now get to work with extracting the data.
First, type the following code in your Jupyter Notebook to get the *title* from every book:

```{code-cell}
:tags: [hide-output]

for book in root.find_all('book'):
    title = book.find('title').text
    print(title)
```

````{note}
Explanation of the code.
The line:
	```
	for book in root.find_all('book'):
	```
starts a loop that iterates through all 'book' elements in the XML. For each elements, it executes the rest of the code.
	```	
	title = book.find('title').text
	```
This line creates a new variabele called 'title'. The content of the variable is content from the XML. For every 'book' element, it searches for 
a child element with the name 'title'. Then, it extracts the content from the 'title' element. To extract content from elements, we use .text. 
	```
	print(title)
	```
This line displays the output. In this case, it shows the title of every book. 
````
	
We can get the description of each book in the same way.

```{admonition} Exercise
:class: attention
Alter the code above to retreive all the *descriptions* and print out the descriptions. 
```

````{admonition} Solution
:class: tip, dropdown
```Python
for book in root.find_all('book'):
	description = book.find('description').text
	print(description)
```	
````

```{code-cell}
:tags: ["remove-input"]
for book in root.find_all('book'):
	description = book.find('description').text
	print(description)
```

We can use one *for loop* to extract both the book title *and* the description from the XML file. 
Combining multiple items is preferable because it saves unnecessary lines of codes and merges the part of the code which does the same thing.
This makes the code more readable and better maintainable. 

Combining the two codes above leads to the following code:

```{code-cell}
:tags: [hide-output]

for book in root.find_all('book'):
	title = book.find('title').text
	description = book.find('description').text
	print(title, description)

```


## Extract name and surname of the author
You can use the same method as described above to extract all the names and surnames from the authors from the example XML. 
However, if we look at the structure of the XML file, there is a difference between the placement of the elements 'title' and 'description', and the elements 'name' and 'surname' in the XML structure. 

```XML
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

Because of the difference in the place between elements, we need to alter our code a bit. Instead of a single *for loop* that iterates through all the 'book' elements, 
we also need a second *for loop* that runs through the 'author' element of 'book'. We can do this with the following code:

```{code-cell}
:tags: [hide-output]

for book in root.find_all('book'):
    for author in book.find_all('author'):
        name = author.find('name').text
        print(name) 
```

```{admonition} Exercise
:class: attention
The above code extracts only the name of an author. Alter the code, so that it extracts both the name and the surname. 
```

````{admonition} Solution
:class: tip, dropdown
```Python
for book in root.find_all('book'):
	for author in book.find_all('author'):
		name = author.find('name').text
		surname = author.find('surname').text
		print(name, surname) 
```
````

```{code-cell}
:tags: [remove-input, hide-output]
for book in root.find_all('book'):
	for author in book.find_all('author'):
		name = author.find('name').text
		surname = author.find('surname').text
		print(name, surname) 
```
Another option is to just look for the element 'Author' and then extract the content from the subelements 'name' and 'surname'. 
This is useful if you have an XML with a lot of children where you want to extract only specific content. 
However, keep in mind that the connection between the book and the authors is lost with this code. 
The code looks like this: 

```{code-cell}
:tags: [hide-output]

for book in root.find_all('author'):
    name = book.find('name').text
    surname = book.find('surname').text
    print(name, surname)  
```

## Extract the book identifier

As you can see in the XML, each book has its own ***identifier***. As books can have the same name, and authors can have written multiple books, it is good practise to always use the identifier to point to a specific item. 

In the previous exercises, we extracted the content that was presented between the tags of an element.
For example:


```XML
<title>XML Developers Guide</title>
```

In this example, you see that the title 'XML Developer's guide' is stored between the tags **title** and **/title**. We extracted this content by adding '.text'. 

````{admonition} Exercise
:class: attention
Look at this example of the 'book' element with its identifier. Compare it to the title element above. What is the difference between the place of the content of the identifier and the place of the content of the title?

```XML
	<book id="bk101">
	</book>
```
````

```{admonition} Solution
:class: tip, dropdown
The content of the identifier is stored in an *attribute* of the 'book' element, with the name 'id'. 
	
```

To extract content from attributes, we need to use the '.get' method. 
We still use the *for loop* to iterate through all the books, but instead of the content of certain elements, we now extract the content of the attribute. 

```{code-cell}
:tags: [hide-output]

for book in root.find_all('book'):
    identifier = book.get('id')
    print(identifier)

```

## Structure all information

We can combine the different codes we have used above into one cell. 
To do this we can use the following scheme:

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
Create the code that extracts all information we have used so far, from every book. And print this information (see scheme above). 
```

````{admonition} Solution
:class: tip, dropdown
```Python
for book in root.find_all('book'):
	identifier = book.get('id')
	title = book.find('title').text
	description = book.find('description').text
	for author in book.find_all('author'):
		name = author.find('name').text
		surname = author.find('surname').text
	print(identifier, title, description, name, surname)
```
````

This leads to the following output:
```{code-cell} 
:tags: ["remove-input","output_scroll"]
for book in root.find_all('book'):
	identifier = book.get('id')
	title = book.find('title').text
	description = book.find('description').text
	for author in book.find_all('author'):
		name = author.find('name').text
		surname = author.find('surname').text
	print(identifier, title, description, name, surname)
```

As you can see, it displays all information we wanted, but the output is quite unreadable. For example, it is not clear which part of the content belongs to the title, and which to the description. 

To make the output more readable, we can put text before our output variables. In Python, this can be done like this:
```Python
print(f"This is the string we type and {this_is_the_variable}")
```

So in our example, we could add the following:

```{code-cell}
:tags: ["hide-output"]

for book in root.find_all('book'):
    identifier = book.get('id')
    title = book.find('title').text
    description = book.find('description').text
    for author in book.find_all('author'):
        name = author.find('name').text
        surname = author.find('surname').text
	## add text to identify the extracted parts
    print(f"Identifier= {identifier} title= {title} description= {description} name= {name} {surname}")
```

As you can see, we can now detect the various parts that we extracted. However, it is still not easy to read.
To resolve this, we can add linebreaks between each variable and between the different books. We add a line break by adding '\n' after each variable, 
leading to the following code:

```{code-cell}
:tags: ["hide-output"]

for book in root.find_all('book'):
    identifier = book.get('id')
    title = book.find('title').text
    description = book.find('description').text
    for author in book.find_all('author'):
        name = author.find('name').text
        surname = author.find('surname').text
	## add linebreaks
    print(f"Identifier= {identifier }\n title= {title}\n description= {description} \n name= {name} {surname}\n")

```

Well, that output looks way better, does it not? Now having this information as printout on screen is useful, but preferably we should be able to use it in further analysis. This means that we need to be able to store it somewhere.

## Store the information in a .csv or .txt file.

Here we show you how to store the output in two different ways:
- as one file with the information of all books in .csv format (which, for example, can be opened in Excel)
- as one textfile per book. 

### Store in one file
The easiest way to store and save Python output in one file is through storing it in a Dataframe from the Python package 'Pandas' and then saving this Dataframe. 
You can add data directly from the *for loops* we created above in a Pandas Dataframe, but we prefer the method in which you first create a list and then transform this list in the output, as Pandas Dataframe execution can become fairly slow with large amounts of data. 

To create a list, we first have to declare an empty list. This is done with the following syntax:
```
booklist = []
```

Now, we alter our *for loop* a bit. Instead of printing the output to the screen, as we did above, we store our output in a list. 
We can use the following code:
```{code-cell}
:tags: ["hide-output"]

booklist = []

for book in root.find_all('book'):
    identifier = book.get('id')
    title = book.find('title').text
    description = book.find('description').text
    for author in book.find_all('author'):
        name = author.find('name').text
        surname = author.find('surname').text
    booklist.append([identifier, title, description, name+" "+surname])
```
This leads to a list, called 'booklist', in which for every book all extracted information is stored. 

We can check the content of the booklist by printing it with:

```{code-cell} 
:tags: ["hide-output"]
print(booklist)
```
Having verified the list contains what we wanted to extract, we can then easily transform this list to a Pandas Dataframe. To do so, we need to first import pandas using the code:
```
import pandas as pd
```

Then we type:
``` 
books = pd.DataFrame(booklist, columns=("identifier", "title", "description", "name")
```

This code works as follows. You declare the variable 'books', which will be used to store all the information. Then you let Python know that you want to create a Dataframe. The content of this Dataframe is the list 'booklist', which we just created. We then tell Python how we want to name the columns (this should be in the same order as the order of the variables in the list). 

You can show the dataframe you just created by typing:
``` 
books
```

This results in the following output:
```{code-cell}
:tags: ["remove-input"]

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

If you want to create a textfile for every book, you can add the code directly in your *for loop*. 

First, you have to declare a textfile in Python and give it a name. Then, you open the file and write content to it. After this, you close the file. Closing the file is important, else the loop will keep adding data to the file.
You can try this with the following code:

```
myfile = open('test.txt', 'w')
myfile.write('This is just a test file')
myfile.close()
```

````{note}
By default, Python stores the text file in the same folder as where you run your Jupyter Notebook. You can alter this by adding a path to your textfile, for example:
``` myfile = open('C:/Users/Documents/test.txt', 'w') 
```
Please remember to use a backward slash (/) between the folders
````

With a few alterations, we can use this code to save our book information to a seperate file per book. 
First, we give the text file the name of the book identifier. We can do that by adding the variable into the name of the file like this:
```
 myfile = open(identifier + '.txt', 'w')
```

Then, we create the content of the file based on the content we extracted from the book. 
```
myfile.write(name + " " + surname + "\n" + title + "\n" + description)
```

If we put these lines into our *for loop*, Python will save every book with its own name and information. 
The code looks like this:
```
for book in root.find_all('book'):
    identifier = book.get('id')
    title = book.find('title').text
    description = book.find('description').text
    for author in book.find_all('author'):
        name = author.find('name').text
        surname = author.find('surname').text
    myfile = open(identifier + '.txt', 'w')
    myfile.write(name + " " + surname + "\n" + title + "\n" + description)
    myfile.close()
```

## Extra: Filter information

You can also search for specific elements in your XML. For example, just the title information from the book 'bk109'. To do so, you can start with the same *for loop* as we created in this lesson. However, before you print the output, you first check if you have the element you want (in this case: book 109). This can be done with an 'if' statement and it looks like this:

```{code-cell}
for book in root.find_all('book'):
    identifier = book.get('id')
    if identifier == "bk109":
        title = book.find('title').text
        print(title)
```

You can also search the content from XML elements, searching the content for a match. For example, if we want to print all titles that contain the word 'XML', 
we can use the following code:

```{code-cell}
for book in root.find_all('book'):
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

````{admonition} Solution
:class: tip, dropdown
```Python
for book in root.find_all('book'):
	description = book.find('description').text
	if "England" in description:
		print(book.find('description').text)
```
````	

```{code-cell}
:tags: ["remove-input"]
for book in root.find_all('book'):
	description = book.find('description').text
	if "England" in description:
		print(book.find('description').text)
```	
		
We now have a good basis to try exploring some reallife examples of XML files used in Digital Humanities research. We will introduce some of these formats in the following section.


