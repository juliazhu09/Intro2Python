#    =================================
#    === Python Programming Basics ===
#    ===      Xiaojuan Zhu         ===
#    ===      xzhu8@utk.edu        ===
#    =================================

# ---HOW TO PREPARE YOUR COMPUTER---
#       FOR THIS WORKSHOP
#
# ---STEP 1. INSTALLING SPYDER ---
# What is Spyder?
# A PYTHON IDE BUILT FOR ANALYZING DATA.
# Install Spyder from this sites:
# https://www.spyder-ide.org/
#
# Spyder has three windows:
# Syntax window: show you the python syntax, you can edit and store the syntax
# variable explorer window: show the variables created by the syntax
# Ipython Console window: run the python syntax and show the output 

# ---STEP 2. STORE WORKSHOP FILES---
#
# In your "Documents" folder,
# create a new folder named "Intro2Python"
# unzip the files and store them there.
#
# Run Spyder and open Intro2Python.py file.

# ---STEP 3. INSTALL ADD-ON PACKAGES---
#
# A Python package refers to a directory of Python
# module(s). A module in python is a .py file that
# defines one or more function/classes which you
# intend to reuse in different codes of your program.
# Use PIP to install a package either in a command prompt
# window or in the python command line, or in Anaconda.
# To use them, we import them. Submodeles can be stored
# in packages, and accessed with dot syntax.
# Some packages, such as sys and os, have already been installed
# in python, you do not need to install it again. We can import
# it directly.
# Official Python description of modules and importing them:
# https://docs.python.org/2/tutorial/modules.html
# Check where is python installed and used by Rodeo/Spyder
import sys
print(sys.executable)

# Install a package using CMD
# Python Path\python -m pip install seaborn 
# For example:
# C:\Users\XZHU8\AppData\Local\Continuum\anaconda3\python -m pip install seaborn 


# Show all of the packages installed under Python
import pkg_resources
packages = [d for d in pkg_resources.working_set]
packages

# ---STEP 4. TEST YOUR INSTALLATION---
#
# Open this file in Spyder,
# select the following commands
# and click "Run Current Cell" or "Run Current Line". If you see
# the output, you're set.
# If not, don't worry, you can watch
# the workshop and fix this later.
#
import os
import sys
import pandas as pd
import matplotlib
import numpy as np
import scipy as sp
import seaborn as sns


print('Python version ' + sys.version)
print('Pandas version: ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)
print('Numpy version: ' + np.__version__)
print('Scipy version: ' + sp.__version__)
print('Seaborn version ' + sns.__version__)


# ---GOOD SOURCES OF PYTHON HELP---
#
# UT people get 15 hours per semester of
# free help in 540 Greve Hall:
#
#   HelpDesk: 974-9900
#   Walk-in Schedule:
#   http://oit.utk.edu/research/schedule
#
# Python & R cheat sheets: https://www.datacamp.com/community/data-science-cheatsheets?page=3
# R & SAS/SPSS/Stata:      http://www.r4stats.com
# Statckoverflow:          https://stackoverflow.com/questions

# ---RUNNING PYTHON COMMANDS---
#
# As you've done above, you can
# Use File> Open or File> New
# to enter Python commands into a
# "script" file and run them.
#
# You can also enter commands one at a time
# in the terminal window at the bottom right.
# Do this sparingly as you can't save
# commands easily.

# ---TERMINAL WINDOW PROMPTS---
#
# ">>>" is the standard command prompt
#
# "..." is the prompt when continuing on a new line
#
# If you see "..." prompt when not trying to
# continue, look for a missing ")"
#
# To get rid of an unexpected "..." continuation
# prompt
#   -Submit the missing piece of the command, or
#    use Ctrl+C


# ---DOCUMENTING YOUR PROGRAMS---

# Comments go from "#" to the end of the line


# ---IMPORTING A PACKAGE TO PYTHON ---
#
# You only install a package once,
# but you need to import it from the package
# each time when you start python
#
# I do it repeatedly in this workshop to
# emphasize that a package is being used.
#
import os
import sys
import pandas as pd

# ---FINDING FILES---
#
# To tell Python the folder to read from or
# write to, set your "working directory" (wd)
#
# This sets it from your Documents folder:
import os
print(os.getcwd()) # Prints the working directory


# Set the working directory:

# python path use "/" or "\\" instead of "\"
# put a r in front of the path string without using / or \\.

os.chdir(r"C:\Users\XZHU8\Documents\Intro2python") # Provide the path here

# if your run spyder on Apps.utk.edu, use the code below
os.chdir(r"\\client\C$\Users\XZHU8\Documents\Intro2python")
# if "r"\\client\C$" does not work.
os.chdir(r"I:\Classes\OIT_Training\Intro to Python")

# Note put "r" before the path by using "copy path" in windows
# or use of forward slash or double backward slashes ("/" or "\\")

# Show the work directory again:
print(os.getcwd())

# ---ASSIGNMENT OPERATOR---
#
# When creating objects, you give them
# values using the assignment operator
# "=" as here:
import pandas as pd
mydata = pd.read_csv("mydata.csv")
mydata.head()
mydata
#---PYTHON VARIABLES---
#
# Python's variable Types:
# Number (int, long, float, Complex)
# String
# Boolean: Ture of False
# List
# Tuple
# Dictionary
# We focus on list today. For details, see
# https://www.tutorialspoint.com/python/python_variable_types.htm
# Example
x =  1
type(x)

x=1.2
type(x)

a = "string"
type(a)

## exercise 1 ##
## Write a program that assigns three variables, one each of types string, int, and float. Variable
##  names and values can be arbitrary. Print each variable out to the screen.

# create a list
# A list contains items separated by commas and enclosed within square brackets ([]).
# Variables can be mixed types in a list.
mixlist = ["a", 1]
mixlist
# Note: first item's index is 0 not 1.
id = [1, 2, 3, 4, 5, 6, 7, 8]
# Show the first item of id.
id[0]
id[7]

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread('apples.png')
imgplot = plt.imshow(img)
plt.show()

## exercise 2##

# The top five highest mountain peaks on Earth, according to Wikipedia, are as follows:
# 1) Mount Everest / Sagarmatha / Chomolungma 8,848 m
# 2) K2 / Qogir / Godwin Austen 8,611 m
# 3) Kangchenjunga             8,586 m
# 4) Lhotse                    8,516 m
# 5) Makalu                    8,485 m
# Use five mountain names, but store them as only names in a list (you 
# can use one name of your choice for those with multiple names). 
# Then, print to the screen the name of Kangchenjunga by referencing 
# its index position in the list.


# Tuples:Like lists, contains several items enclosed within parenthesis.
# but immutable, and usually used for smaller sequences
# of things that are related to each other.
# Think of Cartesian coordinates:(x, y, z)
# The differences between tuples and lists are, the tuples cannot be changed
# unlike lists and tuples use parentheses, whereas lists use square brackets.
aTuple = ("foo", "bar")
len(aTuple)

# Following action is not valid for tuples
# aTuple[0] = 100
aTuple[0] = 100
aTuple[2] = 100
# list can be changed.
alist=["foo", "bar"]
alist[0] = 100

alist

## exercise 3 ##

# create a tuple use Kangchenjunga's name and height and then query the height
# of the Kanchenjuga
# hint:  mtn = ("K2", 8611)


# Dicitonairy: A collection of variables indexed by other, "key" variables.
# Instead of using numeric or default index in python, if you want to
# create your own index, you need to use dictionary.
aDict = {}
aDict["a"] = 364936
aDict["b"] = 12.4
aDict[7] = "hi"

aDict
aDict["a"]
aDict["b"]
aDict[7]

## exercise 4 ##
# Mary’s favorite candy is chocolate, Rodrigo’s favorite is bubble gum, and
# Larry’s is gummy bears. Write a dictionary that stores, for each person, 
# their favorite candy. Then, pick a person among the three, and, using the 
# dictionary keys you defined, print to the screen a statement something to 
# the effect of “Mary’s candy of choice is chocolate.” Make sure that your 
# print() statement is a concatenation of some text and the result of querying 
# your dictionary for that person’s favorite candy. 
# Hint: print("Mary's candy of chocie is" + aDict["Mary"])


# Keywords: reserved words in python.
# Cannot be used as a variable name.
import keyword
print(keyword.kwlist)

# ---OBJECTS & THEIR NAMES---
#
# Python is object oriented
#
# Everything: data, functions (procedures), models,
# etc. are objects, with its properties/attributes
# and methods/functions.
#
# The object names should begin with a letter
# and can contain letters, numbers,
# underscores.
# But cannot have space or period.
# Case matters, e.g. myvar is not MyVar
#

# ---OBJECT ATTRIBUTES AND METHODS---
#
# To access an attributes or a method, use dot syntax.
mydata.workshop

# For example, mean() is a method of a dataframe
mydata.mean()

# list all the attributes and methods of mydata.
dir(mydata)

## exercise 5 ##
# use describe() method to get the deserptive statstics of mydata.
# hint: describe() is a method stored in the mydata.

# ---PYTHON FUNCTIONS---

# As you already know, Python gives you many built-in
# functions e.g. print(mydata), dir(), type()

# When you use a function, you "call" its name.
#
# print() is the default function
#   so this function call:  print(q1)

print(mydata)

# ---NESTING FUNCTIONS---
#
# You can create a variable in
# one step and use it in others
#
import numpy as np
mydata['logq1'] = np.log(mydata['q1'])
np.sum(mydata['logq1'])
#
# or you can "nest" one function
# call within another:
#
np.sum(np.log(mydata['q1']))


# ---USER-DEFINED FUNCTIONS---
#
# A function statement starts with the def keyworkd, followed by
# the function name, parameters and keywords.
#
# Parameters/keywords in a function are called "arguments"
# Arguments follow function name in parentheses
# and are separated by commas
#
# In python, user-defined functions can take four
# different types of arguments. The argument types
# and their meanings, however, are pre-defined and
# can’t be changed. A function is defined using
# the def keyword, and use indentation
# to define the content of the function.
# The content indents four spaces.
# Use Tab key as the shortcut
# The colon is used to declare the start of an indented block.
# When we need to use indentation:
#    if/else statement
#    for/while statement
#    def statement
#    class statement
#
# example:
def my_function():
  print("Hello from a function")
# Calling a function
# To call a function, use the function name followed by parenthesis:
my_function()

# examples
def my_function_with_args(username, greeting):
    print("Hello, {} , From My Function!, I wish you {}!".format(username, greeting))

#prints - "Hello, Julia, From My Function!, I wish you a great year!"
my_function_with_args("Mary", "a great year")

##  exercies 6 ##
# Define a function that will print the string “Hello X!” to the screen, where
# X is a name passed to the function as an argument. Then, call your function, 
# having it greet you by name.
# Hint: string = "Hello" + aName + "!"


#---FUNCTION OUTPUT---
#
#  Returning a value from a function, Not only can
#  you pass a parameter value into a function, a function
#  can also produce a value, i.e., Output.
#  For example,

len(id)

#
#  That value is a single object that may contain
#  much information (e.g. data frame, list)
#
#  Example
def square(x):
    y = x * x
    return y

result = square(10)
result
# Notice: Cannot use print to return a value

## exercies 7 ##
# write a function that will return a person's BMI, where height and weight are
# two names passed to the function as the argument. Then call your function to 
# compute a person's BMI with heigh of 1.6 and weight is 75kg. 
# Hint: BMI = weight / (height * height)


#---CONDITION STATEMENTS---
#
# In the real world, we commonly must evaluate information
# around us and then choose one course of action or another
# based on what we observe: For example,
#
# If the weather is nice, then I’ll mow the lawn.
# Otherwise, I won’t mow.
#
#   if/else-statement
#   if/elif/else-statement
#
# Blocks of code under if statements are executed as long
# as the stated condition is true.
# Can have elif (which is a contraction of "else if") and/or
# else statements associated, when the condition is not true.

# Here is an if/else-statement example:
weather = str(input('How is the weather today, nice or not? '))
if weather == "nice":
    print('I will mow the Lawn')
else:
    print("I won't mow the Lawn")


# If/elif/else statement example,
i = 1
j = 2
if i + j == 3:
    print("three")
elif i + j == 2:
    print("two")
else:
    print("neither!")

# Create a function

def checkNumber(i, j):
    if i + j == 3:
        print("three")
    elif i + j == 2:
        print("two")
    else:
        print("neither!")

checkNumber(1, 1)
checkNumber(10, 1)

## exercise 8 ##
# Import the random module, and use the random function in it that gives you
# a value in the range [0.0, 1.0), multiply it by 10,000, and round it to zero
# decimal places using round() print to the screen a message saying the
# number is odd or even. Part of the code are shown below,
import random
# generate a random number
n = random.random()
ni = round(n*1000.0, 0)
m = ni % 2 # Modulo (%) calculates the remainder after division.
if ():
    print()
else:
    print()

# ---TABLE OF LOGICAL COMPARISONS---
#
# Equals              ==
# Less than           <
# Greater than        >
# Less or equal       <=
# Greater or equal    >=
# Not equal           !=
# And                 &
# Or                  |
# 0<=x<=1             (x >= 0) & (x <=1)


# --- ITERATION---
#
# Iteration is typically done by means of a loop,
# being a piece of code that is executed repeatedly.
# We can control how often a loop repeats, or whether it repeats at all,
# with control flow statements, which evaluates conditions.
# Control flow statements can control more than just loops.
# For more control flow statements, see
# https://docs.python.org/2.7/tutorial/controlflow.html

# --FOR STATEMENT---
#
# Blocks of code under for statements repeat themselves for each
# elements of some iterable object. They make a for loop.
# Iterable objects are those that have a defined sequence of zero or more objects.
# e.g. lists, strings, tuples, etc.
namelist = ["Bob", "Josh", "Cary","Michael","Rochelle", "Sun"]

for name in namelist:
    print ("Hello, " + name + "!")


aText = "Hello world!"

for l in aText:
    print(l)

#---RANGE FUNCTION---
#
# Often we want to repeat an action some specified number of
# times, rather than over a collection of objects.
# The range() function returns an iterable object of numbers, of size
#(and optionally, starting value and increment) you ask for. In python,
# we iterate on that.
# Ask for a range of itegers, starting at zero and ending before 7.
aRange =  range(7)
for i in aRange:
    print(str(i))


for i in range(3, 7): # start at 3 end before 7
    print(str(i))

for i in range(2, 12, 3): #start at 2, end before 12, increment by 3
    print(str(i))
    
## exercise 9 ## 
# Use the range() function to do exercise 8 five times. 
import random
# generate a random number
aRange= range()
for i in aRange:



# ---WHILE STATEMENT ---
#
# Sometimes we use a condition statment to control the number of times
# a loop repeated. As long as the condistion is true, the program
# will repeated execute. So we need to use while statement.
# Blocks of code under while statements repeat themselves until a
# specified condition is detected as false - they make a while loop.
# Before the indented block is (re)run, the condition is evaluated. It
# runs only if the condition is true.

i = 0
while i < 10:
    print(str(i) + " is less than 10")
    i = i + 1
i
# If we left out the increment, 1 could always be <10,
# and we'd get an infinite loop.
# Use Ctrl+C to terminate a loop.

## exercise 10 ##
# To make things concrete and numerical, suppose the following: 
# The tea starts at 115 degrees Fahrenheit. You want it at 112 degrees.
# A chip of ice turns out to lower the temperature one degree each time. 
# You test the temperature each time, and also print out the temperature 
# before reducing the temperature. In Python you could write and run the code
# below, saved in example program cool.py:
temperature = 115  
while temperature ?: # first while loop code
    print(temperature)
    ?
    
print('The tea is cool enough.')

#---QUESTIONS?---
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread('Capture.jpg')
imgplot = plt.imshow(img)
plt.show()

#---BASE GRAPHICS USING SEABORN---

import seaborn as sns
import matplotlib
import pandas as pd

mydata100 = pd.read_csv(r'mydata100.csv', sep=',')
print(mydata100[:6])

import pandas as pd
mydata100 = pd.read_csv(r'mydata100.csv', sep=',')
print(mydata100[:6])

# Barplot

# Barplot stacked
sns.set(color_codes=True) #Change how matplotlib color shorthands are interpreted.
sns.catplot(x="workshop", kind="count", color="b", data=mydata100)

# Boxplot
# Draw a single horizontal boxplot:
ax = sns.boxplot(x=mydata100["posttest"])

#Draw a vertical boxplot grouped by a categorical variable:
ax = sns.boxplot(x="workshop", y="posttest", data=mydata100)

#Draw a boxplot with nested grouping by two categorical variables:
ax = sns.boxplot(x="workshop", y="posttest", hue="gender",
                 data=mydata100)


# Scatterplot

sns.set_style("whitegrid")
sns.scatterplot(x="pretest", y="posttest", data=mydata100)
# Draw a scatterplot of two variables, x and y,
# and then fit the regression model y ~ x
# and plot the resulting regression line
# and a 95% confidence interval for that regression:
sns.regplot(x="pretest", y="posttest", data=mydata100)

# Histogram

sns.distplot(mydata100['posttest'])

from scipy.stats import norm
# Get rid of kernel fit
sns.distplot(mydata100['posttest'], fit=norm, kde=False)

# For many more examples,
# see: https://seaborn.pydata.org/tutorial.html

# ---LISTING OBJECTS IN YOUR WORKSPACE---
#
# dir(): a list of in scope variables
# %who: Print all interactive variables, with some minimal formatting.
# %whos: like %who, but gives some extra information about each variable.
dir()
%who
%whos
# ---DELETING OBJECTS---

# The del() function deletes (ReMoves) objects
del(df)
df

# You can remove a list using:
# del list

del gender
gender

# ---SAVING YOUR WORK---
#
# Save your progs & results with File: Save as...
#
# Export a dataframe in your workspace as csv: dataframe.to_csv('test.csv')

mydata.to_csv( r'C:\Users\XZHU8\Documents\test.csv')

# Save a datafram as excel: dataframe.to_excel('test.xls', index=False)

mydata.to_excel('test.xls', index=False)

# --- QUESTIONS? ---

# ---In a New Browser Tab---
#
# https://workshop.utk.edu/feedback.php
