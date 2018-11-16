#    =================================
#    === Python Programming Basics ===
#    ===      Xiaojuan Zhu         ===
#    ===      xzhu8@utk.edu        ===
#    =================================  

# ---HOW TO PREPARE YOUR COMPUTER---
#       FOR THIS WORKSHOP
#
# ---STEP 1. INSTALLING RODEO ---
# What is Rodeo?
# A PYTHON IDE BUILT FOR ANALYZING DATA.
# Install Rodeo from this sites:
# https://www.yhat.com/products/rodeo

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
# window or in the python command line.
# To use them, we import them. Submodeles can be stored 
# in packages, and accessed with dot syntax.
# Some packages, such as sys and os, have already installed
# in python, you do not need to install again. We can import
# it directly.
# Official Python description of modules and importing them:
# https://docs.python.org/2/tutorial/modules.html
# Check where is python installed and used by Rodeo/Spyder
import sys
print(sys.executable)

# Install a package using CMD
# Python Path\python -m pip install seaborn patsy statsmodels
# For example:
# C:\Users\XZHU8\AppData\Local\Continuum\anaconda3\python -m pip install seaborn patsy statsmodels

# If you want to update the python path, 
# click Tools -> Preference.
# Find the Python interpreter and click 
# Check Use the following python interpreter

# Start Spyder, and open this file by
# going to the "File" menu and choosing
# "Open file". 
# Use pip.main(['install', 'Library name')
# function to install a package. Select the following 
# lines and click "Run Line".
# Do this only one time after you install Spyder:
import pip

# Check the version of pip
print("pip", pip.__version__)
# If pip's version is under 10.0, use the following code to
# install seaborn, pasty and statsmodels packages
pip.main(['install', 'numpy', 'scipy', 'seaborn', 'patsy', 'statsmodels'])

# If pip's version is more than 10.0, like current is 18.0, 
# use the following code to install seaborn, pasty and statsmodels.
from pip._internal import main
main(['install', 'numpy', 'scipy', 'seaborn', 'patsy', 'statsmodels'])

# Update a pacakge installed using pip
import pip
# pip version <10.0, upgrade a package, like pip
pip.main(['install', '--upgrade', 'pip'])
# pip version >=10.0, upgrade a package, like seaborn
from pip._internal import main
main(['install', '--upgrade', 'seaborn'])

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
import statsmodels as sms

print('Python version ' + sys.version)
print('Pandas version: ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)
print('Numpy version: ' + np.__version__)
print('Scipy version: ' + sp.__version__)
print('Seaborn version ' + sns.__version__)
print('Statsmodels version ' + sms.__version__)

# python path use "/" or "\\" instead of "\"
# put a r before the path string without using / or \\.
mydata = pd.read_csv(r'I:\Classes\OIT_Training\Intro to Python\mydata.csv', sep=',', na_values=".")
print(mydata.head())
# Look at the first 3 rows
mydata[:3]


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
# in the terminal window at the bottom left.
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
import pandas as pd
import matplotlib
import numpy as np
import seaborn as sns

# ---FINDING FILES---
#
# To tell Python the folder to read from or
# write to, set your "working directory" (wd)
#
# This sets it from your Documents folder:
import os
print(os.getcwd()) # Prints the working directory


# Set the working directory:

os.chdir(r"C:\Users\XZHU8\Documents\python4stats") # Provide the path here
# Note put "r" before the path by using "copy path" in windows
# or use of forward slash or double backward slashes ("/" or "\\")

# Show the work directory again:
print(os.getcwd()) 

# ---ASSIGNMENT OPERATOR--- 
#
# When creating objects, you give them
# values using the assignment operator
# "=" as here:
mydata = pd.read_csv("mydata.csv")

#---PYTHON VARIABLES---
#
# Python's variable Types:
# Number (int, long, float, Complex)
# String
# List
# Tuple
# Dictionary
# Boolean
# We focus on list today. For details, see
# https://www.tutorialspoint.com/python/python_variable_types.htm
# Example
x =  1 
type(x)

a = "string"
type(a)

# create a list
# A list contains items separated by commas and enclosed within square brackets ([]).
# variables can be mixed types.
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
# Tuples:Like lists, but immutable, and usually used for smaller sequences
# of things that are related to each other.
# Think of Cartesian coordinates:(x, y, z)
# The differences between tuples and lists are, the tuples cannot be changed 
# unlike lists and tuples use parentheses, whereas lists use square brackets.
aTuple = ("foo", "bar")
len(aTuple)

# Following action is not valid for tuples
# aTuple[0] = 100
aTuple[0] = 100
# list can be changed.
alist=["foo", "bar"]
alist[0] = 100
alist

# Dicitonairy: A collection of variables indexed by other, "key" variable.
aDict = {}
aDict["a"] = 364936
aDict["b"] = 12.4 
aDict[7] = "hi"

aDict
aDict["a"]
aDict["b"]
aDict[7]

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
# Object names should begin with a letter 
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

# ---PYTHON FUNCTIONS---

# As you already know, Python gives you many built-in 
# functions e.g. print(mydata), dir(), type()

# When you use a function, you "call" it
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
# Parameters/keywords in a function are called "arguments"
# Arguments follow function name in parentheses
# and are separated by commas
#
# In python, user-defined functions can take four
# different types of arguments. The argument types
# and their meanings, however, are pre-defined and
# can’t be changed. a function is defined using 
# the def keyword, and end with a colon ":"
# and use indentation to define the content of the function.
#
# Python use indentiation to mark blocks of code.
# Indent four spaces to show what block of code
# a statement belongs to. Tab key is the shortcut 
# for 4 spaces indentation. The colon is used to 
# declare the start of an indented block. 
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
namelist = ["Bob", "Josh", "Cary","Cristina", "Harshita", "Jaewoo", "Jialin", "Jose", "Katie", "Lu",
"Matthew", "Michael", "Mohmad", "Paychuda", "Rochelle", "Saad Abd Ar", "Stone", "Tracey", "Xiaocun", 
"Yaxiong", "Lauren"]

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
    

# ---WHILE STATEMENT ---
# Blocks of code under while statements repeat themselves until a
# specified condition is detected as false - they make a while loop.
# Before the indented block is (re)run, the condition is evaluated. It
# runs only if the condition is true. 

i = 0
while i < 10:
    print(str(i) + " is less than 10")
    i =  i + 1

i
# If we left out the increment, we could always be <10,
# and we'd get an infinite loop.
# Use Ctrl+C to terminate a loop.

#---QUESTIONS?---
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread('Capture.jpg')
imgplot = plt.imshow(img)
plt.show()

####################################### 
#### WORKING WITH DATA USING PYTHON ###
#######################################
#
# ---CREATE A DATAFRAME MANUALLY---
# First, we create three list variables.
id = [1, 2, 3, 4, 5, 6, 7, 8]
workshop = [1, 2, 1, 2, 1, 2, 1, 2]
gender = ['f', 'f', 'f', ''  ,'m', 'm', 'm', 'm',]

# Merge these three lists together we will use the zip function
help(zip)
zip?

mydatalist = list(zip(id, workshop, gender))
# show mydatatest
mydatalist
# use pandas to create df as a data frame object. 
import pandas as pd
df = pd.DataFrame(data = mydatalist, columns=['id', 'workshop', 'gender'])

# Check data type of the columns
df.dtypes

# Check data type of id column
df.id.dtype
df.workshop.dtype

# ---DATA MODIFICATION---

# Add a new column
df['newcol'] = 5
df
# rename a column 
df = df.rename(columns = {'newcol':'rev'})
df.columns    # return all the column names

# add a column from a list
df['q1'] = [1, 2, 2, 3, 4, 5, 5, 4]

# Add a column from another dataframe's variable.
df['q2'] = mydata['q2']
df[['q3','q4']] = mydata[['q3','q4']]

# Create some columns based on the other columns.
df['diff'] = df['q1'] - df['q2']
df['ratio'] = df['q1'] / df['q2']
df['meanQ'] = (df['q1'] + df['q2'] )/2

# Log transform
import numpy as np
df['logq1'] = np.log(df['q1'])
df

# look at the first 5 rows of a column:
df['meanQ'][:5]
df.meanQ[:5]
df[:5]['meanQ']
df
# Use index to subset simliar to R
df.loc[0:4, 'meanQ']  #df.loc: Access group of values using labels
df.iloc[0:5, 10]      #df.iloc: Access group of rows and columns by integer position(s)

# ---TABLE OF TRANFORMATIONS---
#
# Addition           x+y
# Subtraction	     x-y
# Multiplication	 x*y
# Dividison          x/y
# Antilog, base 10   10**x 
# Antilog, Natural   numpy.exp(x)
# Division	         x/y
# Exponentiation	 x**2 
# Logarithm, base 10 numpy.log10(x) 
# Logarithm, Natural numpy.log(x) 
# Round off	         round(x) 
# Square Root	     numpy.sqrt(x)

# --- BASIC DESCRIPTIVE ANALYSIS---
df.mean()
df.sum()
df.max()
df.min()
df['q2'].mean()
# return all numeric variables' descriptive statstics
df.describe()

# We saw describe get frequencies on
# workshop and mean, sd, on q variables
#
# df is a data frame
df.mode()
df['q1'].mode() 

#Return the count/frequency for each level
df['gender'].value_counts()

#---TRANSFORM TO NUMERIC VARIABEL---

mydata.dtypes # data.frame, 
# check a variable's type.
mydata['q3'].dtype

#Convert q3 from object/catergorical to numeric
mydata['q3'] = pd.to_numeric(mydata['q3'], errors='coerce') #If ‘coerce’, then invalid parsing will be set as NaN
mydata['q3'].dtype
mydata['q3']

# ---CREATING SUBSETS USING PANDAS ---
#Select the oberservations for a new dataset, 
#if the observationsmeet a condition.
import pandas as pd
mydata100 = pd.read_csv(r'mydata100.csv', sep=',')
print(mydata100[:6])

# Subset selects rows
mydata100['gender'] =='Female'

females = mydata100[mydata100['gender'] =='Female']
females

femalesr = mydata100[(mydata100['gender'] =='Female') & (mydata100['workshop'] == 'R')]
femalesr

# selecting vars from subset of females
femaleQs = females[['q1','q2','q3','q4']]
femaleQs

# Not valid below
femaleQs = females['q1':'q4']

# Use index to subset the data, similar to R
femaleQsloc = mydata100.loc[mydata100['gender']=='Female', 'q1':'q4']
femaleQsloc


# More details about subsetting data, see
# https://stackoverflow.com/questions/10665889/how-to-take-column-slices-of-dataframe-in-pandas

# ---MISSING VALUSE---
# 
raw_data = {'first_name': ['Jason', np.nan, 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', np.nan, 'Ali', 'Milner', 'Cooze'], 
        'age': [42, np.nan, 36, 24, 73], 
        'sex': ['m', np.nan, 'f', 'm', 'f'], 
        'preTestScore': [4, np.nan, np.nan, 2, 3],
        'postTestScore': [25, np.nan, np.nan, 62, 70]}
missdata = pd.DataFrame(raw_data, columns = ['first_name', 
'last_name', 'age', 'sex',  'preTestScore', 'postTestScore'])

missdata
# Test for missing use isnull function

missdata.isnull()  

# Count missing by columns
missdata.isnull().sum()

# Count all missing values
missdata.isnull().sum().sum()

# Find non Missing values
missdata.notnull()

#---ACTION ON MISSING VALUES---
#
#
# Drop missing observations
missdata.dropna()


# Drop rows where all cells in that row is NA
missdata.dropna(how='all')

#Drop column if they only contain missing values
missdata['missingcol'] = [np.nan, np.nan, np.nan, np.nan, np.nan]
missdata

missdata.dropna(axis=1, how='all')

#Keep only the rows that contain at least two non-missings
#This is really mostly useful for time series

missdata.dropna(thresh=2)

#Fill in missing data with 999
missdata.fillna(999)

# For detials, please see 
# https://www.tutorialspoint.com/python_pandas/python_pandas_missing_data.htm
# https://chrisalbon.com/python/data_wrangling/pandas_missing_data/

# ---MATRIX AND ARRAY OPERATION---
#
#Matrix like a data frame, usually all numeric

# ---ARRAYS---
#
# A set of matrices stacked like pages in a book
#
# vectors and matrices are simple arrays (1D, 2D)   
# 1D = list
# 2D = matrix, dataframe
# 3D (or higher) = array

import numpy as np

# Generate a matrix 
#  a =|  1  0 |   b= | 4  1|
#     |  0  1 |      | 2  2|

a = [[1, 0],
     [0, 1]]
b = [[4, 1],
     [2, 2]]

# Matrix/array addition
import numpy as np
np.add(a, b)
# Cannot use a+b
a + b

# Matrix/array subcration, element-wise
np.subtract(a, b)

# matrix multiplication

np.matmul(a, b)
np.dot(a,b)

#numply.multiply; perform element wise multiplication.
np.multiply(a, b)

# The element wise division of a matrix/arrary.
np.divide(a, b)

# Use numpy zeros function to create a 2 by 2 by 2 array
ThreeDarray = np.zeros((2, 2, 2))

ThreeDarray

#---BASE GRAPHICS USING SEABORN---

import seaborn as sns
import matplotlib

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
sns.scatterplot(x="pretest", y="posttest", data=mydata100);
# Draw a scatterplot of two variables, x and y, 
# and then fit the regression model y ~ x 
# and plot the resulting regression line 
# and a 95% confidence interval for that regression:
sns.regplot(x="pretest", y="posttest", data=mydata100)

# Histogram
from scipy.stats import norm
sns.distplot(mydata100['posttest'], fit=norm)
# Get rid of kernel fit
sns.distplot(mydata100['posttest'], fit=norm, kde=False)

# For many more examples, 
# see: https://seaborn.pydata.org/tutorial.html


# ---UNIVARIATE STATISTICS---
#    
# describe() function return summary statistics

mydata100.describe()

# ---CROSSTABULATIONS---
#
# Tests for factor independence, e.g. do
# males prefer different workshops than females
#
# Crosstabs with format=SAS or format=SPSS
#
# Row/Column/Total percents
#
# It does not perform a Chi-squared test 
# unless you request it

import pandas as pd

pd.crosstab(mydata100['workshop'],mydata100['gender'])

# Return row percentage
pd.crosstab(mydata100['workshop'],mydata100['gender'], normalize='index' )

# Return column percentage
pd.crosstab(mydata100['workshop'],mydata100['gender'], normalize='columns' )

# Return total percentage.
pd.crosstab(mydata100['workshop'],mydata100['gender'], normalize='all')

# Chi-squared test
import scipy.stats as scs
result = pd.crosstab(mydata100['workshop'],mydata100['gender'])

chi2, p, dof, ex = scs.chi2_contingency(result)
print("Chi-square: ", str(chi2),  ", df:" , dof, ", p-value: ", str(p))


# ---CORRELATIONS---
#
# Measure strength of linear association
#
# Assume variables are normally distributed
#
# corr() function from dataframe provides 
#
# load smaller data frame.

mydata100.loc[:, 'q1':'q4'].corr(method='pearson')  

# Use type = "spearman" if not normally distributed
mydata100.loc[:, 'q1':'q4'].corr(method='spearman')  

# ---LINEAR MODELS WITH THE OLS() FUNCTION---
#
# Tests linear relationship between one variable
# and a set of predictors
#
# Assumes:
#   -Model errors are normally distributed
#   -Variance is constant across variable's range
#
# In python, you create a model object and use 
# "extractor functions" to see the parts you want
# like, summary, resid, and other functions have specialized 
# methods for model objects 
#
import statsmodels as sms
import statsmodels.api as sm
from statsmodels.formula.api import ols

result = ols(formula="q4 ~ q1 + q2 + q3", data=mydata100).fit()
print(result.summary())

# see, https://www.accelebrate.com/blog/interpreting-results-from-linear-regression-is-the-data-appropriate/

# Anova table
table = sm.stats.anova_lm(result, typ=3)
print(table)
# Residuals QQ plot.
res = result.resid 
fig = sm.qqplot(res, line='s')
plt.show()

# Mulitple regression with a catergorical variable
result = ols(formula="q4 ~ q1 + q2 + q3 + C(workshop)", data=mydata100).fit()
print(result.summary())
sm.stats.anova_lm(result, typ=3)

# ---TABLE OF COMMON FORMULAS---

# Simple Regression       y ~ x
# Multiple Regression 
#   with Interaction      y ~ x1 + x2 + x1:x2  or  y ~ x1*x2
# Regression 
#   without Intercept     y ~ -1 + x
# One-way ANOVA           y ~ C(a) or y ~ a 
# Two-way ANOVA 
#   with interaction      y ~ C(a) * C(b) or y ~ a * b
# Analysis of Covariance  y ~ C(a) + x or y ~ a + x

# --------COMPARING GROUPS----------

# ---T-TEST FOR TWO INDEPENDENT GROUPS---
#
# Compare whether two groups' means are equal
# Continuous variable should be normally distributed
# 
# With statsmodels that also give degrees of freedom
female_q1 = mydata100[mydata100['gender'] == 'Female']['q1']

male_q1 = mydata100[mydata100['gender'] == 'Male']['q1']

# check equal variance
import scipy as sp
sp.stats.levene(female_q1, male_q1)


# 'pooled' or 'unequal', pooled: the standard deviation of 
# the samples is assumed to be the same. # unequal:  Welsh 
# ttest with Satterthwait degrees of freedom is used.
from statsmodels.stats.weightstats import ttest_ind
t, p, df = ttest_ind(female_q1, male_q1, usevar='pooled' )
print("t statistic:", t, "; df:", df, "; p-value:", p  )

  
# ---ANALYSIS OF VARIANCE FOR 3 OR MORE GROUPS---
# 
# Continuous variable should be normally distributed
# 
# Getting descriptive statistics for each workshop
# groupby() function repeats a function for each factor group
mydata100.groupby(['workshop'])['posttest'].describe()

# Box plot for four workshops
ax = sns.boxplot(x="workshop", y="posttest", data=mydata100)

# ANOVA test
model = ols(formula="posttest ~ C(workshop)", data=mydata100).fit()
print(model.summary())

# ANOVA type 3 table
aov_table = sm.stats.anova_lm(model, typ=3)
print(aov_table)

#check residuals
res = model.resid 
fig = sm.qqplot(res, line='s')
plt.show()

# Test normality of residuals
import scipy as sp
sw, pvalue=sp.stats.shapiro(res)
print("W statistics:", sw, "; P-value:", pvalue)

# ---POST-HOC COMPARISONS---
#
# Show which groups differ
from statsmodels.sandbox.stats.multicomp import MultiComparison
mc = MultiComparison(mydata100['posttest'], mydata100['workshop'])

# Tukey HSD
result = mc.tukeyhsd()
print(result)

# Bonferroni 
from scipy import stats
resultB = mc.allpairtest(stats.ttest_ind,  method='bonferroni')[0]
print(resultB)

#---Table of Correcton Methods---
#
#`bonferroni` : one-step correction
#`sidak` : one-step correction
#`holm-sidak` : step down method using Sidak adjustments
#`holm` : step-down method using Bonferroni adjustments
#`simes-hochberg` : step-up method  (independent)
#`hommel` : closed method based on Simes tests (non-negative)
#`fdr_bh` : Benjamini/Hochberg  (non-negative)
#`fdr_by` : Benjamini/Yekutieli (negative)
#`fdr_tsbh` : two stage fdr correction (non-negative)
#`fdr_tsbky` : two stage fdr correction (non-negative)
#
# See,https://www.statsmodels.org/0.8.0/generated/statsmodels.sandbox.stats.multicomp.multipletests.html

# Mean and 95% confident plot
result.plot_simultaneous()  

# ---GETTING HELP---
#
# Get help on any function
help(zip)

# Get help on a object's methods and attributes
help(mydata)

# Help on a method
help(mydata.mean)

# Help on package functions
import pandas as pd
help(pd)

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

# see https://www.statsmodels.org/dev/stats.html

# ---In a New Browser Tab---
#
# http://workshop.utk.edu

# --- QUESTIONS? ---

