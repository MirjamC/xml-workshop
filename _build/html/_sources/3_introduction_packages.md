# 3. Introduction to the packages ElemenTree and Beautiful Soup

In the previous two sections we introduced Python and XML. The structured way XML is built makes it relatively easy to navigate it and obtain the required data programmatically. With Python there are multiple ways of extracting data and information from XML files. The most straightforward is to use packages that are specifically built to deal with XML.

In this section we will introduce two packages that are commonly used when dealing with XML: *ElementTree* and *Beautiful Soup*.

## Elementree

*ElemenTree* is a built-in package of Python. The benefit of this is that it is already present in the base Python installation and therefore no extra packages need to be installed. This means less complexity and dependencies, which can make it more reproducable and easier to maintain.
*ElemenTree* has specifically been designed to work with XML files. It features tools to navigate and manipulate XML files in multiple ways and is generally held to be intuitive.

## beautiful Soup
 
*Beautiful Soup* is one of the most popular packages for webscraping with Python. Not specificially built for XML, HTML and XML have a very similar structure. Because of this similarity *Beautiful Soup* is also able to parse XML files. However, it is best to use it in conjunction with the *lxml* package.
*Beautiful Soup* comes with numerous methods for searching XML and is very popular due to its neat style. It is also one of the few packages that has no problems dealing with broken or non-standard XML.
 
## Which is best?

Which package is the right tool for a project depends on the requirements. Each has its own benefits and drawbacks. 

ElemenTree is included with Python, which means there are less dependencies on other packages and less chance of version. This also makes it slightly easier to maintain. 
ElemenTree has also been developed with XML parsing in mind, the whole package is geared towards XLM.

Beautiful Soup is very versatile and can parse HTML and XML with ease. This is especially good if the project involves XML and HTML in any way.
Beautiful Soup is also able to work with broken and non-standard XML. Which can be very benificial in research settings.
A downside of Beautiful Soup is that is requires an additional package to be installed for optimal use. While this should not give any problems, it does increase the chance of version and dependency conflicts.

Switching between packages can be somewhat challenging as both implement their code is slightly different ways. However, when running into problems parsing a certain XML file it is always good to know that there may be another package that may be able to help.


