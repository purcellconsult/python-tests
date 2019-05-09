################################################
# A general python assessment test to evaluate
# potential mentees.
#
#
# BY Doug Purcell
# http://www.purcellconsult.com
#
#
################################################


"""

1) Python is commonly referred to as a scripting language, while some languages like Java and C++ are referred to as compiled languages.
a) Can python be compiled. If so, why is it referred to as an interpreted language?
b) What’s the difference between a compiled and  interpreted language?
c) CPython is the reference implementation of the python programming language. Are there other implementations? If so then what’s the point of having several implementations for one language?


Answer:
_ _ _ _

a) Yes, it depends on the version. For example, in CPython or the standard implementation
of python is translated to bytecode, and then the bytecode is executed by the python
virtual machine (PVM). If you're using Jython then the bytecode is executed on the Java
Virtual Machine (JVM).
Learn about the Python Virtual Machine here: https://www.ics.uci.edu/~brgallar/week9_3.html

b) This question can have many answers. Some languages like Java can be compiled and
interpreted, so thus it's hybrid. A language like C is typically compiled but
it too has interpreters available. Therefore, 'compiled' and 'interpreted' are an implementation
of the language. When a language is compiled the source code (human readable portion)
is converted to machine instructions which can be executed by the hardware. In an
interpreted implementation, the program is translated to something other than
machine readable instructions. This depends on the language and the implementation.

c) CPython is the default version of python and is written in C and python. In other
words it's the version you download from python.org. So, the python that you know
and love is technically CPython. The reason why it's name this is because there's
several other implementations of python and there needs to be a way to distinguish them.
Here's some other implementations of python:

Jython ==> https://www.jython.org
IronPython ==> https://ironpython.net
PyPy ==> https://pypy.org
MicroPython ==> https://micropython.org
CLPython ==> https://common-lisp.net/project/clpython

"""

"""

2) Is python considered a C-style programming language? If not, then why is its 
standard implementation CPython written primarily in C?

Answer:
_ _ _ _

A less confusing question would be C-syntax. The answer to that is no
because it doesn't follow the syntax that typically C style languages follow. 
For example, it doesn't require curly braces or semicolons. 

"""


"""

3) Is there any difference between the following snippets of code?

>>> a = 'Hello World'
>>> b = "Hello World"
>>> c = \"""Hello World"""

"""
Answer:
_ _ _ _

There's no difference between a and b. However, with c this is a triple
quote and therefore can span multiple lines, don't need escapes
or less you're including other triple quotes like in this example, and
can generate docstrings for functions, classes, etc: https://www.python.org/dev/peps/pep-0257
"""


"""
4) Python has several ways to format strings. You can use the % sign, the builtin 
format() method, or template strings. Read the python docs to discover the various 
ways in which you can format strings: https://docs.python.org/3.4/library/string.html

Here’s how to format a string in python using the % operator:

>>> 'Today is a good day. It is between %d and %d degrees F' % (75, 85)
'Today is a good day. It is between 75 and 85 degrees F'

Format the above string using the format() method and template strings. 

"""


"""
#4 Answer:
"""
today_1 = 'Today is a good day. It is between {} and {} degrees F'.format(75, 85)
print(today_1)

# demo of the Template string
from string import Template
today_2 = Template('Today is a good day. It is between $x and $y degrees F')
print(today_2.substitute(x=75, y=85))

"""

5) What’s the difference between a while and for loop? If you used a while loop in 
your code can it be rewritten so that a for loop is used?

Answer:

A while loop will do something as long as a condition is meet.
A for loop will do something to everything you wish to iterate through.
They can be used interchangeably but in some cases one loop makes more sense.
I.e, if you want the loop to run indefinitely use a while loop. If you want
to iterate over a list structure use a for loop. 

"""

"""

6)
a) Write a while loop that sums the numbers from 1 – 1000.
b) Translate the above while loop to a for loop. Research the range() function. 
c) Modify b so that all of the numbers from 1-1000 are printed except for any number that’s divisible by 75.


"""

"""
a
"""
i, count = 0, 1
while i <= 1000:
    count += i
    i += 1

print(count)

"""
b
"""

count = 1
for x in range(1001):
    count += x
print(count)

"""
c
"""

count = 1
for x in range(1001):
    if x % 75 == 0:
        pass
    else:
        print(x)

"""

7) Python has a list of builtin functions which you can view here: 
https://docs.python.org/3/library/functions.html

Analyze the definition of the min() and max() functions. Create your own functions 
called minimum() and maximum() that replicates the logic of the min() and max() 
functions in the python core. 

Answers:

min
"""

def minimum(the_list):
    min = the_list[0]
    i = 0
    while i < len(the_list):
        if the_list[i] < min:
            min = the_list[i]
        i += 1
    print(min)


"""
max
"""
def maximum(the_list):
    max = the_list[0]
    i = 0
    while i > len(the_list):
        if the_list[i] < min:
            max = the_list[i]
        i += 1
    print(max)


minimum([382, 372, 72, 32, 2])
maximum([382, 372, 72, 32, 2])
"""
max
"""


"""
8) Write a function named fo_shizzle_my_nizzle() that prints a string contingent on the following conditions:

The letter n is used as input.

fo → n is less than 0. 
shizzle → n is in the range of 1-49, 1 is inclusive, and 49 is exclusive. 
my → n is in the range 50-100, with 50 and 100 being inclusive. 
nizzle → n is even, divisible by 3, and greater than 100. 
'' ''→ if none of the above conditions are met then an empty string is printed by default. 

Write a loop that tests the input in the range of -10...150. 

"""

"""

Answer:function
"""
def fo_shizzle_my_nizzle(n):
    if n < 0:
        n = "fo"
    elif n >= 1 and n < 50:
        n = "shizzle"
    elif n >= 50 and n <= 100:
        n = "my"
    elif n % 2 == 0 and n % 3 == 0 and n > 100:
        n = "nizzle"
    else:
        n = ""
    return n

"""
test loop
"""

i = -10
while i < 150:
    print(fo_shizzle_my_nizzle(i))
    i +=1

