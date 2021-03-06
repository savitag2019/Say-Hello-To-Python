'''
This is a starter code to help you learn the basics of Python
It covers standard data types and data manipulation in Python

Next, we will try a similar starter code for Numpy and Pandas
'''


# This is single-line comment

'''
This is a multi-line comment,
mostly used for docstrings
'''


# The quintessential print command
print("I am learning Python.")
# with two pieces put together
print("I am learning Python.")
# or with a line break in between
print("Hello 2020!", "\nI am learning Python.")
# or with a specified format
print("I think {} is a number.".format(23))
print("Indeed, {} is a number with {} digits.".format(23,2))
print("and {:.2f} is a rational with {} decimal places.".format(1.4323,2))


# You have some basic data types, as follows
n = 143                 # integers (int)
f = 1.43                # rationals (float)
s = "Sourav"            # strings (str)
b = True                # boolean (bool)

# You may check their types
print("{} is of type :".format(n), type(n))
print("{} is of type :".format(f), type(f))
print("{} is of type :".format(s), type(s))
print("{} is of type :".format(b), type(b))

# and use them in arithmetic operations
n = 143
n + 5               # addition
n * 5               # multiplication
n / 5               # exact division
n // 5              # rounded division
n % 5               # remainder
n ** 5              # exponentiation

f = 1.43
f + 5               # addition
f * 5               # multiplication
f / 5               # exact division
f // 5              # rounded division 
f % 5               # remainder
f ** 5              # exponentiation

s = "Sourav"
s + s               # concatenation
s * 5               # repeated concatenation
len(s)              # length of a string

# or in logical operations
b = True
not b               # logical NOT
b and b             # logical AND
b or b              # logical OR

s = 143
s == 143
s == 10
s != 10
s > 10
s < 10


# You have some data containers too, for example, Lists
L = [10, 0, -2, 13, 3, 523]           # initialize a list
print(L)
type(L)

L[0]                                  # single position
L[0:3]                                # the first three elements
L[-2:]                                # the last two elements
L[2:]                                 # all elements from third position
L[1:4]                                # three elements from the second one

L[1] = 23                             # substitute element
print(L)
L[1:3] = [7, -10]                     # substitute part of list
print(L)
L[1:5] = [-17, 8]                     # substitute any part of list
print(L)

del L[2]                              # remove an element
print(L)
del L[1:3]                            # remove part of a list
print(L)
L.append(0)                           # append to the list
print(L)
L.extend([-2, 13, 3])                 # extend the list
print(L)
L.remove(0)                           # remove if element exists
print(L)

L.pop()                               # return last element
print(L)
L.sort()                              # sort list
print(L)

0 in L                                # check membership
2 in L                                # check membership
L.index(0)                            # index of the first occurrence
L.index(2)                            # returns error if not present

K = L                                 # shallow copy a list
print(K)
K[0] = -34                            # changing copied list
print(L)                              # affects the original

K = L.copy()                          # deep copy a list
print(K)
K[0] = -212                           # changing copied list
print(L)                              # does not affect the original

# Lists support list comprehension, a neat tool
[x for x in L]
[x*5 for x in L]
[x*5 for x in L if x > 0]
[x**2 for x in L if x < 10]

# and can contain elements of arbitrary types!
L = [11, 67, "abc", 3.14, [-2, 0, 10]]
L[0]
L[2]
L[4]
L[4][0]

# Double indexing using list of lists
L = [[10, 20, 30], 
     [40, 50, 60], 
     [70, 80, 90]]
L[0][0]
L[2][2]
L[1][2]


# Another interesting container : Tuple
x = 10, 20, 30, 40, 50          # initialization
x = (10, 20, 30, 40, 50)        # clearer initialization

x[1]                            # indexing similar to lists
x[1:]
x[:-1]
x[1:4]

a,b,c,d,e = x                   # reverse assignment
print(a)
print(d)

x[1] = 12       # DOES NOT support replacement/change : Immutable


# Another interesting container : Set
S = {1, 3, 5, 10, 2}
print(S)                        # always sorted and unordered
S = {1, 3, 5, 3, 2}
print(S)                        # always without duplicates

0 in S                          # check membership
2 in S                          # check membership

S = {1, 2, 3, 5, 10}
R = {1, 2, 7, 9}
S | R                           # set union
S & R                           # set intersection
S - R                           # set difference
S ^ R                           # set exclusive or


# The most interesting container : Dictionary
D = {"Name": "Sourav", 
     "Age": 33, 
     "Institute": "ISI Kolkata", 
     "Teaching": "CDS 2017"}          # key:value pairs
D.keys()
D.values()
list(D.keys())                        # list of keys
list(D.values())                      # list of keys
sorted(D.keys())                      # sorted list of keys

k = ('Name', 'Age', 'Institute')
D = dict.fromkeys(k)                  # set keys, empty values
print(D)

D["Name"] = "Debapriyo"               # assign new values to keys
D["Age"] = "NA"
D["Institute"] = "ISI Kolkata"
print(D)


# Most data types and containers lend themselves to conversion
int("143")
int(1.56)
round(1.56)
float("1.43")
float("-1.34e8")
float("-1.34e-3")
str(143)
str(-0.00134)
list("Sourav")
set([1,3,1,4,1,5])
dict([("Name","Sourav"), ("Age",33), ("Institute", "ISI Kolkata")])

# Note that a variable may also be reassigned to something else
x = 143
type(x)
x = "Sourav"
type(x)
# due to the loosely typed property of Python. Be very careful!


# You may code conditional statements
x = 143
if x > 100:
    print(x, "is greater than", 100)
elif x == 100:
    print(x, "is equal to", 100)
else:
    print(x, "is smaller than", 100)

if ((x > 100) and (x < 120)):
    print(x, "lies in between 100 and 120")
else:
    print(x, "is either <= 100 or => 120")    


# or iterative statements (loops)
x = 143
while x > 100:
    print(x)
    x = x - 1

for i in range(1,10): 
    print(i)

for i in range(-5,5): 
    print(i)

for i in range(1,10,2): 
    print(i)

for i in range(-10,10,2): 
    print(i)

# may be over lists
L = [-10, 0, 20, 23, 1, -12]
for x in L:
    print(x)

for x in sorted(L):
    print(x)

for x in reversed(L):
    print(x)

# or over key:value pairs in dictionaries or lists
D = {"Name": "Sourav", 
     "Age": 33, 
     "Institute": "ISI Kolkata", 
     "Teaching": "CDS 2017"}          # key:value pairs

for (k, v) in D.items():              # tuples with keys and values
    print("Key", k, "contains", v) 

L = [11, 67, "abc", 3.14, [-2, 0]]    # treating lists like dicts
for (i, x) in enumerate(L):
    print("Index", i, "contains", x)  

# or over "zipped" lists
L = [-10, -5, 0, 5, 10]
K = [12, 4, 0, 4, 12]
for (x, y) in zip(L, K):
    print(x, "zipped with", y)


# You may also write iterative and conditionals together
L = [-10, 0, 20, 23, 1, -12]
s = 20
for x in L:
    if x == s:
        print("Found it!")
        break

# REALLY IMPORTANT : Note the indentation of the code block above


# One may also define functions/subroutines to make life easier
def linearSearch(L, s):
    '''
    This function checks linearly if an element is present in a list
    '''
    for x in L:
        if x == s:
            return True
    return False

help(linearSearch)              # Check the help on the function
linearSearch.__doc__            # or the documentation/docstring

linearSearch([1,2,3,4,5], 3)    # calling the function with input
linearSearch([1,2,3,4,5], 7)

# and functions, thankfully, may return (almost) anything
def linearSearch(L, s):
    '''
    This function checks linearly if an element is present in a list
    '''
    for x in L:
        if x == s:
            return "Found it!"
    return "Sorry, not found."

print(linearSearch([1,2,3,4,5], 3))
print(linearSearch([1,2,3,4,5], 7))

# or perform recursive calls to itself, if required
def factorial(n):
    '''
    Returns the factorial of a positive integer
    '''
    if (n == 1):
        return 1                   # base case or stopping criteria
    return (n * factorial(n-1))    # recursion in other cases

factorial(10)
factorial(-3)  # this will fail, as the function is not sanity checked


# By the way, you may take user input too
name = input("What is your name? ")
print("Hi {}, how you doin'?".format(name))

# input is generally treated as string, and so
x = input("Please enter a number: ")
y = input("Enter another, please: ")
s = x + y
print("Sum of the numbers is: ", s)    # shocked?

# You should carefully typedef the inputs after receiving
x = input("Please enter a number: ")
y = input("Enter another, please: ")
s = int(x) + int(y)
print("Sum of the numbers is: ", s)    # that's better

# or before, if you already know the types
x = int(input("Please enter a number: "))
y = int(input("Enter another, please: "))
s = x + y
print("Sum of the numbers is: ", s)    # similar results
# but generally better, as wrong input is auto-prevented


# In certain cases, file handling is preferred/essential
f = open("testFile.txt", "w")    # check out w, wb, r, r+, rb, rb+
f.write("This is CDS 2017,\n")
f.write("and we are learning Python.\n")
f.write("I am not so sure why.\n")
f.write("Hopefully, it will help!\n")
f.close()
# what are the commands returning/printing?

# Moreover, where the hell did the file "testFile.txt" go?
# Check in you home folder (Unix) or default working directory
# You may set your default working directory from "Preferences"
# It is not automatically set as where the python files are

# Note that when you read a file, it is basically a list of lines
f = open("testFile.txt", "r")
L = f.readlines()
f.close()
print(L)
# and a line/string is basically a list of characters (convert it)
l = L[0]
C = list(l)
print(l)
print(C)

# If you want the words, you will have to "split" the line at spaces
W = l.split(" ")
print(W)
w = W[0]
print(w)


# You may "import" useful modules/packages in Python too
import random
for i in range(0,10):
    print(random.randint(0,10))    # random integers >= 0 and <= 10

# Your test cases for 1-D Peak Search may be generated as follows
L = [random.randint(0,10) for i in range(10)]
print(L)
L = [random.randint(-10,10) for i in range(1000)]
print(L)

# Similarly, you may generate test case for 2-D Peak Search as
N = 5        # set the size N x N for the 2-D grid
nMin = -10   # set the minimum value for randint
nMax =  10   # set the maximum value for randint
L = [[random.randint(nMin,nMax) for j in range(N)] for i in range(N)]

# you may now traverse through the grid as a simple 2-D array
for i in range(N):
    for j in range(N):
        print("{:4d}".format(L[i][j]), end=" ")
    print("\n")

# If you were observant, you must have noticed function calls as
L.copy()
random.randint()
l.sort()
# with syntax of the call similar to "someObject.someFunction()"

# Every "object" in Python has associated "methods" or "functions"
# and you get a list of them if you press <tab> after "someObject."

# By the way, pressing <tab> also performs auto-completion of code.
# Try it out with everything that you define from now on. Enjoy!
