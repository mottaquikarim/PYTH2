<!---
{"next": "Topics/conditionals.md","title": "Basic Data Types"}
-->

# Basic Data Types

Let's discuss data types, variables, and naming.

## Variables

A data type is a unit of information that can be stored and retrieved using a program language. **Variables** store different types of data. You can display the value stored in a variable on the screen using the `print()` statement. Because variables are so ubiquitous, there are some **rules for naming variables** that help avoid confusion.

- **Rule:** snake_case with the underscore character
- **Rule:** Can’t use keywords as var names, e.g. True, None, function, class, object
- **Rule:** Can’t start with a numeric value, e.g. can't name something "1var", but you CAN do function1
- **Best Practice:** You COULD use CamelCase to name a variable, but this is typically reserved for naming a different Python object called a "class".

#### Creating & Reading a Variable

```python
first_prime = 2
print(first_prime) # expect to see 2
```

#### Comments

Real quick, let's see how we create comments so that you can write notes to yourself in your code - **very** useful!

```python
# I'm a comment!


# Here is a multi-line comment:
"""
'Cause if you liked it, then you should have put a ring on it
If you liked it, then you should have put a ring on it
Don't be mad once you see that he want it
If you liked it, then you should have put a ring on it
"""
```

## Fundamental Python Data Types

These are the most basic data types, which compose the more complex data types we'll learn about later:

* Strings: alphanumeric characters read as text
	* **Important takeaway!** If you use a `'`, say in a contraction, the string might misinterpret it as the ending `'` for the string. To avoid this, add `\` right before that `'` like this: 'I\'ll`.
* Integers: whole numbers
* Floats: decimals
* Booleans: represents True or False values; used for evaluating conditional statements
* Nonetype: represents variables not yet defined or essentially blank values (shown as None, used as placeholder to avoid error)

```python
# Strings
cat = 'Layla' # or "Layla" because single & double quotes are both valid
cat_description = 'Layla\'s a mischievous, but very cute kitty!' # Note the use of \' here.

# Integers
age = 8

# Floats
weight = 10.5

# Booleans
vaccinated = True
good_with_other_cats = False

# Nonetype
good_with_other_dogs = None
```


### String Formatting

Strings have some special qualities that make dealing with them easier. For instance, you can store several separate snippets of text within a single string. One way to do this is adding `\n` to signify that you want to create a new line. However, there's another way to do this that makes it much more readable! To do this, you can use triple quotes i.e. `'''` or `"""`. You can use single and double quotes within the string freely, so no need to worry about that detail!

Let's say you're storing song lyrics, so you want to have a line break between each line of the song.

```python
'Cause if you liked it, then you should have put a ring on it\nIf you liked it, then you should have put a ring on it\nDon\'t be mad once you see that he want it\nIf you liked it, then you should have put a ring on it'

'''
'Cause if you liked it, then you should have put a ring on it
If you liked it, then you should have put a ring on it
Don't be mad once you see that he want it
If you liked it, then you should have put a ring on it
'''
```

If you want to insert variables within a string, you can do this:

```python
cat = 'Layla'

print(cat, 'is a mischievous, but very cute kitty!')
# Note that the ',' automatically adds a space character.
```

But that can be annoying if you're inserting multiple variables. To simplify this, you dynamically add variables directly within a string like this:

```python
cat = 'Layla' # or "Layla" because single & double quotes are both valid
age = 8
weight = 10.5


print(f'{cat} is {age} years old.\n{cat} weighs {weight} pounds.')
print(f'''
{cat} is {age} years old.
{cat} weighs {weight} pounds.
''')

"""
Both of these print...

Layla is 8 years old.
Layla weighs 10.5 pounds.
"""
```

### Practice Problem Set 1: Basic Data Types

Open these notebooks and add your own code to solve these problems. **MAKE SURE YOU MAKE A COPY OF THE NOTEBOOK FIRST!!!**


* [PRACTICE 1](https://colab.research.google.com/github/mottaquikarim/pydev-psets/blob/master/pset_basic_data_types/basics/nb/p1.ipynb)
* [PRACTICE 2](https://colab.research.google.com/github/mottaquikarim/pydev-psets/blob/master/pset_basic_data_types/basics/nb/p2.ipynb)
* [PRACTICE 3](https://colab.research.google.com/github/mottaquikarim/pydev-psets/blob/master/pset_basic_data_types/basics/nb/p3.ipynb)
* [PRACTICE 4](https://colab.research.google.com/github/mottaquikarim/pydev-psets/blob/master/pset_basic_data_types/shopping_list/nb/p1.ipynb)
* [PRACTICE 5](https://colab.research.google.com/github/mottaquikarim/pydev-psets/blob/master/pset_basic_data_types/shopping_list/nb/p2.ipynb)

## Typecasting

#### Check what data type is stored in a variable using the `type()` statement or the `isinstance()` statement.

```python
# Example 1 - type()
a = 1
print(type(a)) # <class 'int'>

b = '2.5'
print(type(b)) #  


# Example 2 - isinstance()
c = -1
print(f'Is {c} a boolean?', isinstance(c, bool)) # False

d = False
print(f'Is {d} a boolean?', isinstance(d, bool)) # True
```

#### Typecasting is a way to convert an instance of one data type to another.

```python
# Convert int to str
a = str(10)
print(f'{a} is a {type(a)} type.') # '10'


# Convert str to int
b = int('10')
print(f'{b} is a {type(b)} type.') # 10
### int('tasdfa') # throws a ValueError


# Convert int to bool
c = bool(10) # True
d = bool(0) # False

# Convert bool to int or float
e = int(True) # 1
f = float(True) # 1.0
g = int(False) # 0
h = float(False) # 0.0
"""You can convert any number to a True boolean,
BUT a True boolean will only ever become 1 or 1.0."""
```

### Practice Problem Set 2: Typecasting

* [PRACTICE 1](https://colab.research.google.com/github/mottaquikarim/pydev-psets/blob/master/pset_basic_data_types/typecasting/nb/p1.ipynb)
* [PRACTICE 2](https://colab.research.google.com/github/mottaquikarim/pydev-psets/blob/master/pset_basic_data_types/typecasting/nb/p2.ipynb)
* [PRACTICE 3](https://colab.research.google.com/github/mottaquikarim/pydev-psets/blob/master/pset_basic_data_types/booleans/nb/p1.ipynb)
* [PRACTICE 4](https://colab.research.google.com/github/mottaquikarim/pydev-psets/blob/master/pset_basic_data_types/booleans/nb/p2.ipynb)

## Simple Integer, Float, & String Operators

**Operators** are shortcuts for manipulating values stored in variables.

### Integer/Float Operators

We can operate on integers/floats in the following ways:

* Addition
* Subtraction
* Multiplication
* Division
* Modulus (This one divides and returns **only the remainder**.)

```python
orig_num = 10

# Addition
num1 = orig_num + 5 # 15

# Subtraction
num2 = orig_num - 5 # 5

# Multiplication
num3 = orig_num * 5 # 50

# Division
num4 = orig_num / 5 # 2

# Modulus
num5 = orig_num % 5 # 0
num6 = orig_num % 3 # 1
```

### String Operators

* We can "add" strings
* We CANNOT add strings to non strings

```python
a = 'this string'
b = 'that string'

print(a + b) # 'this stringthat string'


print(a + ' and ' + b) # 'this string and that string'
print(a, 'and', b) # 'this string and that string'


"""ERROR!!!
print('this will not work' + 4) doesn't work 
because you can't add a number to a string"""
```

### Practice Problem Set 3: Simple Operators

* [PRACTICE 1](https://colab.research.google.com/github/mottaquikarim/pydev-psets/blob/master/pset_basic_data_types/operators/nb/p2.ipynb)
* [PRACTICE 2](https://colab.research.google.com/github/mottaquikarim/pydev-psets/blob/master/pset_basic_data_types/operators/nb/p1.ipynb)

## Additional Resources

* [A Repl.it Summarizing Print Statements](https://repl.it/@brandiw/Python-01-Variables-4?lite=true)
* [Python For Beginners](http://www.pythonforbeginners.com/basics/python-variables)
* [Python Programming Tutorial: Variables](https://www.youtube.com/watch?v=vKqVnr0BEJQ)
* [Variables in Python](https://www.guru99.com/variables-in-python.html)
* [Operators Cheatsheet](http://python-reference.readthedocs.io/en/latest/docs/operators/)
* [Python Style Guide: Naming](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles)
* [Python-Strings](https://www.tutorialspoint.com/python/python_strings.htm)
* [String Concatenation and Formatting](http://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python)
* [String Concatenation and Formatting - Video](https://www.youtube.com/watch?v=jA5LW3bR0Us)

