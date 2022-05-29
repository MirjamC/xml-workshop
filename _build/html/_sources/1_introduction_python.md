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

# 1. Introduction to Python and Jupyter Notebooks
This lesson will give a short introduction on how to work with Notebooks in combination with Python. 
It consists of explanation followed by pratical exercises. To get the most out of this lesson it is best to manually type the code into your Jupyter Notebook instead of copy-pasting.

## Notebooks
First, lets start up Jupyter and open a Notebook.
In the taskbar searchbox, type 'jupyter' and open *jupyter notebook*.
This should open a tab in your browser with the jupyter hub in the installation folder. 
This folder will act as your home folder for jupyter.
All Notebooks you make will be stored here unless explicitely saved elsewhere or moved.

To open a new Python Jupyter Notebook click the **new** button in the topright corner and select **python3** from the dropdown list.
A new tab should open dispaying your new Notebook, usually called *Untitled*

Notebooks can be renamed by clicking on the name and typing a different name. It is best to make these names descriptive so they are still recognizable after a while. 

**To add:** screenshots 

## How does a Notebook work?

A Notebook is not a static page, but an interactive enviroment. Within the blocks (cells) of a Notebook code can be written ánd executed.

### Different cell types

Notebooks are compromised of different types of cells. 
The main cell types are *text cells* and *code cells*.

Text cells are generally used for descriptions and explanations. These cells are inactive and code written in these cells cannot be executed.

**To add:** screenshot text cell

The layout is managed through *markdown* (see [markdown syntax](https://www.markdownguide.org/basic-syntax/) for more information).

The second main type of cell is the code cell. 
Code cells are used to write and execute code. In our case Python. When a code cell is run, Python will execute the code in the cell. More information about Python will follow in the next section.

**To add:** screenshot code  cell

Code cells are easily recognized by the 'In [ ]:' to the left of the cell.

The type of a cell can be changed by selecting a cell and either going through the menu (Cell/Cell Type/<option>) or by selecting a cell and pressing either **Y** for a code cell or **M** for a text cell.

**To add:** printscreen menu celltype

```{admonition} Exercise
:class: attention
Select a cell in the Notebook and change the type by using the hotkeys or the menu. 
```

### Running cells
There are multiple ways to run a cell:
* By clicking the 'Run' button in the taskbar;
* By pressing 'shift + enter when the cell is selected (green frame)'
	*Note that this will add move the selection box down one cell. When the end of the cells is reached this will add new empty cells to the Notebook.*

The moment a cell generates *output* the output is displayed beneath the cell, keeping code and output together.

```{admonition} Exercise 
:class: attention
Type the code below in a cell in your Notebook and run the cell.
```

```{code-cell} 
2*8
```

### Adding new cells

One cell is rarely enough to make a clearly structured Notebook. Adding more cells can be done by pressing the '+' button in the taskbar. 

**To add** printsscreen +

This will add a new cell directly below the currently active cell.

Another way is to use the menu 'Insert', where the choice is given between adding a cell above or below the current active cell.

**To add** printscreen menu

### Comments

Comments can be added to a code cell. Comments can be used to describe what a piece of code does, or can be used to tell where values can be changed. 

```{code-cell} 
# This is an example of a comment in a code cell.
```

The moment a # is typed in a code cell, everything after it *on the same line* will be regarded as a comment. Lines that have been marked as a comment will **not** be executed by Python when the cell is run.

```{admonition} Exercise 
:class: attention
Type the code below in a cell in your Notebook and run the cell. Does Python return output?
```

```{code-cell}
:tags: [hide-output]

#print("The solution to 35+12 is:")
#print(35+12)
```

```{admonition} Solution
:class: tip, dropdown
The cell should not return any output as the code is commented out by the #.
```

When the **#** is removed and the cell is run again, Python wil recognize the code and execute it.

```{admonition} Exercise
:class: attention
Alter the cell so the code is no longer seen as a comment.
```

```{admonition} Solution
:class: tip, dropdown
Removing the # from the code should enable Python to recognize the code return output when the cell is run
```
```{code-cell}
:tags: [remove-input, hide-output]
print("The solution to 35+12 is: ")
print(35+12)
```

## Python

Python was developed in 1991 by Guido van Rossum. The purpose of Python was to create a programming language that is both simple to understand and readable. Python works on different platforms such as Windowns, Mac, Linux, etc. It is a very popular programming language in data analysis and data science because of its versatality.
Python is open source, and can be used for free.

### Input and variables

When using Python there are multiple types of input data, such as lists, numbers, text, and even whole tables.
We put this input into *variables*. Essentially a container for the data. The name of a variable is up to your own discretion, although there are some [rules and guidlines](https://www.w3schools.com/python/gloss_python_variable_names.asp). 

Python remembers which input was loaded into which variable. This means that the variables can be used in the code instead of the data itself.

It is important to input data correctly, for numbers *no* quotation marks are used, for text quotation marks *must be* used!

The command *type()* can be used to determine what type of input a variable contains. 

*int* indicates a variable contains an integer, or whole number.
*str* indicates a variable contains a string, a piece of text. 

```{admonition} Exercise
:class: attention
Type the code below in a cell in your Notebook and run the cell.
```

```{code-cell} 
:tags: [hide-output]

number = 9
text = "this is a text"
```

```{code-cell} 
:tags: [hide-output]

type(number)
```

```{code-cell} 
:tags: [hide-output]

type(text)
```

```{admonition} Note
**Important!** If you input a number *with* quotation marks Python will see it as text!
```

```{admonition} Exercise 
:class: attention
Type the code below in a cell in your Notebook and run the cell. What data type is the number?
```

```{code-cell}
:tags: [hide-output]
number_but_wrong = "9"
type(number_but_wrong)
```

```{admonition} Solution
:class: tip, dropdown
The cell should return 'str'. The number is seen as a string because of the quotation marks. Sometimes an error in the code is due to the wrong data type, checking data type is always a good start when error checking.
```

As mentioned above it is possible to use previously assigned variables in your code. 
This makes it possible to input a value just one time when it is needed more than once in the code.

```{admonition} Exercise
:class: attention
 Type the code below in a cell in your Notebook and run the cell.
```

```{code-cell} 
:tags: [hide-output]

number_1 = 3
number_2 = 6

number_1 + number_2 
```

Python simply adds the original numbers as it remembers which input belongs to which variable.

```{admonition} Exercise
:class: attention
Using Python variables, calculate the sum of "35 + 69" in the cell below. Start with making two variables to assign the numbers *35* and *69* to. Calculate the sum using these variables.
```

```{code-cell} 
:tags: [hide-output]

# Make a variable for the number 35

# Make a variable for the number 69

# Calculate the sum using the variables
```

```{admonition} Solution
:class: tip, dropdown
Your code should look a bit like this:
	
	number_1 = 35
	number_2 = 69
	number_1 + number_2 
```

```{code-cell} 
:tags: [remove-input,hide-output]
number_1 = 35
number_2 = 69
number_1 + number_2 
```


The plus sign can be used to calculate sums, as you did in the above exercise. However, the plus sign can also be used to stick different strings together. 

```{admonition} Exercise
:class: attention
Type the code below in a cell in your Notebook and run the cell.
```

```{code-cell} 
:tags: [hide-output]

line_1 = "This is a "
line_2 = "stuck together text"

line_1 + line_2
```

As you can see Python adds the text elements together to form a longer sentence. This also works with multiple variables.

```{admonition} Exercise
:class: attention
Ensure that the four lines below are printed as one sentence in the output.
```

```{code-cell} 
:tags: [hide-output]

line_1 = "Because of this Notebook "
line_2 = "I now know "
line_3 = "that programming with Python "
line_4 = "is very fun!"
```

```{admonition} Solution
:class: tip, dropdown
Your code should look a bit like this:

	line_1 + line_2 + line_3 + line_4
```
```{code-cell} 
:tags: [remove-input, hide-output]
line_1 + line_2 + line_3 + line_4
```


Now, what about adding text and numbers from variables together?

```{admonition} Exercise
:class: attention
Type the code below in a cell in your Notebook and see what happens when you run the code.
```

```{code-cell} 
:tags: [hide-output,raises-exception]
line_1 = "The amount of abstracts for DHBenelux is: "
amount_1 = 43
line_1 + amount_1
```

```{admonition} Solution
:class: tip, dropdown
This gives an error:
	
	TypeError: unsupported operand type(s) for +: 'int' and 'str'

Just adding numbers and text does not work. Some extra work needs to be done in order for Python to correctly return output without errors
```

There are multiple options to convince Python to return combinations of numbers and  text:
- force numbers to text with *str()*
- *f strings*

To force Python to interpret a number as text its type can be changed with str(number).

```{admonition} Exercise
:class: attention
Type the code below in a cell in your Notebook and run the cell.
```

```{code-cell} 
:tags: [hide-output]
line_1 = "The amount of abstracts for DHBenelux is: "
amount_1 = 43
line_1 + str(amount_1)
```

This also works with multiple variabeles and pieces of text outside of variables.

```{admonition} Exercise
:class: attention
Type the code below in a cell in your Notebook and run the cell.
```

```{code-cell} 
:tags: [hide-output]

line_1 = "coffee breaks "
amount_1 = 2
 
"The amount of " + line_1 + "in this workshop is: " + str(amount_1)
```

```{note}
Notice the space after each of the pieces of text (either in or outside a variable).
Try removing it to see what happens
```

Another option is the use of *f strings*. This is a way of telling Python where to insert the contents of a variable into a string. 

The syntax for *f strings* is:

```python
f"This is the string we type and {this_is_the_variable}"
```


```{admonition} Exercise
:class: attention
Type the code below in a cell in your Notebook and run the cell.
```

```{code-cell} 
:tags: [hide-output]

line_1 = "coffee breaks "
amount_1 = 2
 
f"The amount of {line_1} in this workshop is: {amount_1}"
```

### Output

As you have already seen, executing code can produce output. In Jupyter Notebooks the output is presented within an output cell. Errors will be printed here too. 
Not all code will produce output, so don't be alarmed.

Output should generally be created by printing using:
```{code-cell}
print("whatever you wish to print") 
```

Text must be put between quotes or Python will assume you are wishing to print variables.

Variables can be printed the same way as text, but must **not** have quotation marks.

```{admonition} Exercise
:class: attention
In a new code cell, create the variable **print_me* and assign to it "I was printed with the print function"
Using the print function, print out the variable.
```

```{admonition} Solution
:class: tip, dropdown
	print_me = "I was printed with the print function"
	print(print_me)
```
```{code-cell}
:tags: [remove-input, hide-output]
print_me = "I was printed with the print function"
print(print_me)
```
As you can see prints the contents of the variable to the output cell.

However, using Jupyter Notebooks there is also another way to create output. You have seen, and used, this before. The last line of a cell will always create output, if there is any output to create. 

To demonstrate this, let's reuse some of our variabeles.

```{admonition} Exercise
:class: attention
In a new code cell, type out the variables *line_1*, *amount_1*, *print_me* below each other. Run the cell.
Which variable is printed to the output?
```

```{admonition} Solution
:class: tip, dropdown
Only the last variable *print_me* is printed.
Try changing the order and see if this behaviour is consistent.
```
```{code-cell}
:tags: [remove-input, hide-output]
line_1
amount_1
print_me
```

These two ways of printing output are not completely the same. Printing using the print() function removes some of the layout that Jupyter creates for you. This is very noticible when printing tables.

We have created a variable table for you that contains a table of numbers. Which we will use to demonstrate the difference in printing.

```{admonition} Exercise
:class: attention
In a new code cell, print out the variable *table* using the print() function and by executing the variabel
Which variable is printed to the output?
```

````{admonition} Solution
:class: tip, dropdown
You will have used 
```print(table)```
or 
```table```
to print out the table. You can check below of the output matches yours.
````

```{code-cell}
:tags: [remove-input, hide-output]
import pandas as pd
data = [32,6,7,5,34534,7], [123,543,3,7,8,43],[12,34,8,6,34,65],[12,32,56,873,56,3]
table = pd.DataFrame(data, columns = ["I","am","a","table","of","numbers"])
print("This was printed with the print() function.")
print(table)
```
```{code-cell}
:tags: [remove-input, hide-output]
print("This was printed by executing table")
table
```
While this diffence is purely aesthetic, it is good to know, especially when working with table formatted data.
 
### Functions

When you program in Python you will make use of functions. The *str()* code used in the previous exercise to make Python recognize numbers as text was an example of a function. Python contains a lot of built-in functions that are ready to use. Saving us a lot of manual coding!

Functions need to be passed one or more parameters as input. The syntax of a function is as follows: *functionname(parameters)*. When there are multiple parameters these are seperated with a comma.

You can find some examples below.

```{admonition} Exercise
:class: attention
Type the code below in a cell in your Notebook and run the cell
```

```{code-cell} 
:tags: [hide-output]

# Calculate the highest number using the max() function.
max(5, 8, 35, 4, 75, 2)
```

```{admonition} Exercise
:class: attention
Round the number below using the round() function. The first parameter is the number to round. The second number is the required number of decimals. Type the code below in a cell in your Notebook and run the cell
```

```{code-cell} 
:tags: [hide-output]

round(36.53343, 2)
```

```{admonition} Exercise
:class: attention
Calculate the *lowest* number using the function min(). This functions works similarly to the previously used max() function.
Use the following numbers: 6, 24, 8, 2, 14. 
```

````{admonition} Solution
:class: tip, dropdown
The code should look like this
```
min(6, 24, 8, 2, 14)
```
and the min() function should return **2**
````
### Conditional statements, *if else*

Python is able to use conditional statements. These are control structures that enable us to decide what to do based on what happens in our code and input. It requires that that one or more conditions are specified to be evaluated or tested by the program, along with something that the code must do if the condition is determined to be true, and optionally, something else if the condition is determined to be false. 

For example:
```
	if "hungry":
		to_do = "Lunch!"
	else:
		to_do = "Work!"
```
These can also be extended using multiple choices:
```
	if "hungry":
		to_do = "Lunch!"
	elif "tired": 
		to_do = "Coffee!" 
	else:
		to_do = "Work!"
```
Instead of coding out conditions directly into the *if else*, it is also possible to evaluate the contents of a variable. This enables us to reuse an *if else* block multiple times. 
```
## First we put the condition into a variable 
	current_state == "hungry"
## then we evaluate the variable
	IF current_state == "hungry":
		to_do = "Lunch!"
	ELIF current_state == "tired": 
		to_do = "Coffee!" 
	ELSE:
		to_do = "Work!"
```
It we would now print the contents of the variable *to_do* we would get:
```
Output:
"Lunch!"
```

### Packages

The last important thing to know is that Python works with packages. A package is a collection of modules with predefined functions. These functions can than be used in your own code. Using packages can save a lot of programming work and enhances the functionality of base Python. Most Python programmers regularly use packages.

Before using a Python package it needs to be *installed*. This preferably done using the command line but can also be done within your Jupyter Notebook.
Afterwards the package needs to be *imported* into the Notebook. After importing the package is ready for use.

To demonstrate this we will install, import and use a package to display some information about the contents of DHBenelux 2022. 

First you will need to download the dataset.

**To Add** download link and dataset

Now lets install and import the packages we need.
We will need three packages:
- Pandas, for easy data manipulation 
- matplotlib, for plotting in Python
- WordCloud, for generating a wordcloud 

```{admonition} Exercise
:class: attention
Type the code below in a cell in your Notebook and run the cell
```

```
# Install the package
!pip install pandas
!pip install WordCloud
!pip install matplotlib
```
```{note}
The exclamation mark before *pip* is needed to activate *pip* within the Notebook enviroment. When installing from the command line this is not needed.
```

```{code-cell} 
:tags: ["hide-output"]

# Import the packages
import pandas
from wordcloud import WordCloud
import matplotlib.pyplot as plt
```
```{note}
There is a difference between the import statements of the three packages. In the case of *pandas* and *wordcloud* we import the whole package. 
For *matplotlib* we only want the *pyplot* module, so we added this explicitly after the package name. This ensures that ony that module is imported. The *as plt* statement renames package to a shorter and easier typable code. You will see this used below.
```

A package can be used in the same way as a function. 
We will use the *pandas* package to load data into the Notebook in a way that is digestable for the creation of a wordcloud.
Many packages feature multiple functions for data manipulation, calculation or visualisation. The function you wish to use is added after the package name.

Syntax: *packagename.function(parameters)*

The package name points Python to the location of the function. 

```{admonition} Exercise
:class: attention
Type the code below in a cell in your Notebook and run the cell
```


```{code-cell} 
:tags: ["hide-output"]
# Read the dataset into Python using pandas
wordcloud = pandas.read_csv("data/wordcloud_dataset.csv", header=None, index_col=0, squeeze=True)
# Transform into dictionary for use in the WordCloud
wordcloud_dict = wordcloud.to_dict()
```
```{note}
As you can see, the *pandas* name precedes the option *read_csv*. 
```

Now we have data it is good practice to have a quick look at it to ensure the data is loaded correctly.

```{admonition} Exercise
:class: attention
Type the name of the dataset in a cell and run the cell
```

The data should look like the example below.

```{code-cell} 
:tags: [remove-input,output_scroll]
wordcloud_dict
```

When the data is correctly loaded we can use the *WordCloud* and *matplotlib* packages to create a wordcloud from the data.

```{admonition} Exercise
:class: attention
Type the code below in a cell in your Notebook and run the cell
```

```{code-cell} 
:tags: ["hide-output"]
# initialise the wordcloud
wc = WordCloud(background_color="white", max_words=20)
# generate the wordcloud 
wc.generate_from_frequencies(wordcloud_dict)
# plt the wordcloud to the output
plt.figure()
plt.imshow(wc,interpolation="bilinear")
plt.axis("off")
plt.show()
```

This should plot a wordcloud showing maximally 20 word in different sizes. Each word is sized by the amount of times it occurs in the titles of the DHBenelux 2022 abstract. Common words have already been removed.
This visualiation can give quick insight to which items are popular at the moment. 

Well done! Now you know the basics of working with Jupyter Notebooks and Python. We will use this in the coming chapters. 
