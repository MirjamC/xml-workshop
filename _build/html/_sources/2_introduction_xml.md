# 2. Introduction to XML 

## XML

XML stands for eXtensible Markup Language. It is a language (but not a programming language) which goal is to store and transport data in a structured manner. It was designed to be self-descriptive and to be both human and machine readable. Because XML presents data in a structured format, and because it is platform independent, it is a popular format for applications to communicate. 
XML itself does not do anything. 

XML is very common in DH research and knowing how to process XML documents is an invaluable skill. 

### XML Structure

Below is a short example of XML:

```XML
<?xml version="1.0"?>
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
		<description>An in-depth look at creating applicationswith XML.</description>
	</book>
</catalog>
```

Although at first this may look unfamiliar, the XML above is mostly self-descriptive:
- it is a catalog 
- it contains a book 
- it contains information about that book 
- it has a description of the book

This XML structure is called a *tree* and contains so-called elements. 

```{admonition} Exercise 
:class: attention
Looking at the example XML, what is the title of the book?
```

```{admonition} Solution
:class: tip, dropdown
The title of the book is: "XML Developer's Guide". This can be found by looking at the flanking *tags*, more about these later.
```

### Elements

An XML tree consists of elements.

All elements follow the same basic structure:

Opening tag + content + closing tag = element

Elements consist of tags that describe the element, and content.
Tags come in pairs, an opening tag and a closing tag. These are enclosed in **<>**.
Tags of an element must always be identical to each other, except that the closing tag includes a **/** before the tagname.

Because of this structured build elements are self-describing.
One element in the example XML above is the title:

```XML
<title>XML Developer's Guide</title>
```
```XML
<title> - is the opening tag
XML Developer's Guide - is the content 
</title> - is the closing tag
```
An element can contain other elements, such as in the example above. 
The element *book* contains the elements *author*, *title*, *genre*, *price*, *publish_date*, and *description*

Elements can also be empty, having tags but no content.

````{admonition} Exercise 
:class: attention
Looking at the example XML, what elements does the element *author* contain?
```XML
	<?xml version="1.0"?>
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
			<description>An in-depth look at creating applicationswith XML.</description>
		</book>
	</catalog>
```
````

````{admonition} Solution
:class: tip, dropdown
The element *author* contains the elements *name* and *surname*.
```XML
	<author>
		<name>Matthew</name> 
		<surname>Gambardella</surname>
	</author>
```
````

### XML Tree

Similar to a real tree, an XML tree starts at a *root element* and branches out into *child elements*.
Each of these elements can have *sub elements* or *child elements*.

The basic structure is this:
```XML
<root>
  <child>
    <subchild>.....</subchild>
  </child>
</root>
```
The relation between elements is described with the terms *parent*, *child*, and *sibling*.
Like family trees, parents are on the top level, children below parents and siblings are on the same level.

````{admonition} Exercise 
:class: attention
Looking at the example XML,
1. What is the root element?
2. Does the element *book* have subchildren?
3. What are the siblings of *author*?
```XML
<?xml version="1.0"?>
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
			<description>An in-depth look at creating applicationswith XML.</description>
		</book>
	</catalog>
```
````

```{admonition} Solution
:class: tip, dropdown
1. The root element is the first element of the tree. In this case it is *catalog*.
2. The element *book* has 2 subchildren, *name* and *surname*.
3. The siblings of author are: *title*, *genre*, *price*, *publish_date*, and *description*.
```

### Attributes

Elements can have attributes. Attributes give more information about XML elements and are used to distinguish between elements with the same name. Attributes always consists of a name-value pair.

Returning to our example XML, the element *book* has an atribute *id*.
```XML
<book id="bk101"> </book>
```
This attribute contains the unique id of the book. This is usefull as there may be books with the same name, and this way these can be identified separately. Attribute values are always quoted. 

### Namespaces *WIP*

Tag names are defined by the person or application building the XML. This can lead to problems when mixing XML from different applications. These name conflicts can be 

For example, below are two pieces of XML, *catalog* and *author*. Both contain elements of the same name: *name* and *surname*.
If these two pieces were added together, there would be a name conflict.

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
		<description>An in-depth look at creating applicationswith XML.</description>
	</book>
</catalog>

<singers>
	<name>Katy</name>
	<surname>Perry</surname>
</singers>
```
### Prolog

XML usually starts with the *prolog* a piece of code that defines the XML version and can contain character encoding. The prolog is optional, and if present it must come first in the document. It is good practice to include it.

For our example the prolog is:
```XML
<?xml version="1.0"?>
```
### Comments

In XML comments may be added, these can contain descriptions about the data or other information.
Comments are written as:
```XML
<!-- This is a comment -->
```
### Rules

There are some rules regarding XML.
As mentioned above tags must always come in pairs. Each opening tag needs its closing tag.
Tag names are case sensitive, in XML title, Title, and TITLE are three different tag names
Tag names can only begin with a letter or an underscore.
Tag names can contain letters, digits, hyphens, underscores, and periods. No other signs are allowed, mnot even spaces.
XML documents **must** have a root element.

````{admonition} Exercise 
:class: attention
Keeping the rules in mind, are the following elements correctly defined?
```XML
1.	<author>
		<name>Matthew</name>
		<surname>Gambardella</surname>
	</Author>

2.	<title>XML Developer's Guide
	
3.		<author>
			<name>Matthew</name>
			<surname>Gambardella</surname>
		</author>
		</book>
	
4.	<price>44.95</price>
	
5.	<publish_date>2000-10-01</publishdate>
	
6.	<description>An in-depth look at creating applications with XML. /description>
```
````

````{admonition} Solution
:class: tip, dropdown
```XML
1. No, the root tags are not the same, <author> and </Author>. XML is case-sensitive.
2. No, the closing tag </title> is missing. Elements must always have both tags.
3. No, the opening tag <book> is missing. Elements must always have both tags.
4. Yes, this element is correctly defined.
5. No, the tags are not the same. The closing tag misses an underscore
6. No, the closing tag misses the <.
```
````

This concludes this brief introduction to XML. The next section will forcus on some common Python packages that are used to extract data and information from XML. 



