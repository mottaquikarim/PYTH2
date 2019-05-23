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

### Practice PSET 1: Basic Data Types


## Typecasting

### `type()`

Check what data type is stored in a variable using the `type()` statement or the `isinstance()` statement.

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

### Convert Values Into Different Data Types

**Typecasting** is a way to convert an instance of one data type to another. Numbers are the most flexible for converting, while strings are very inflexible. Booleans get a bit more complicated, so we'll look at those last!

#### Converting Numbers

```python
"""INTEGERS"""
int_to_float = float(10) # 10.0, <class 'float'>
int_to_string = str(10) # 10, <class 'str'>

"""FLOATS"""
float_to_int = int(2.5) # 2, <class 'float'>
# Notice it does NOT ROUND!
float_to_string = str(2.5) # '2.5', <class 'str'>
```

#### Converting Strings

```python
string_to_int = int('mango') # ERROR!
string_to_float = str('strawberry') # ERROR!
```

#### Converting Booleans

As you'll see below, you can convert any number to a True boolean, BUT a True boolean will only ever become 1 or 1.0.

```python
"""EVALS TO TRUE"""
int_to_boolean = bool(10) # True, <class 'bool'>
float_to_boolean = bool(2.5) # True, <class 'bool'>
string_to_boolean = bool('peach') # True, <class 'bool'>

"""EVALS TO FALSE"""
int_to_boolean = bool(0) # False, <class 'bool'>
float_to_boolean = bool(0.0) # False, <class 'bool'>
string_to_boolean = bool('') # False, <class 'bool'>
```

Notice that the **ONLY** way a string converted into a boolean will be False is if it's empty. Spaces count as characters even though they wouldn't display anything if printed.

**Pro Tip**: You can use the `.strip()` function to remove trailing spaces from strings.

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

### Practice PSET 3: Simple Operators



### Practice PSET 4: Put it all together!



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
