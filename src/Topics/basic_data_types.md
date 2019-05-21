<!---
{"next": "Topics/conditionals.md","title": "Basic Data Types"}
-->

# Basic Data Types

Let's discuss data types, variables, and naming.

### Variables

A data type is a unit of information that can be stored and retrieved using a program language. We store data into, and retrieve data from, **variables**.

### Creating a Variable

```python
first_prime = 2
```

### Reading a Variable

```python
print(first_prime) # expect to see 2
```

#### [PRACTICE](https://mottaquikarim.github.io/pydev-psets/#pset_basic_data_types/basics/p2.ipynb)

### Naming Variables

In python, the best practice is to **snake_case** variables, where we delimit spaces within variable names with the `_` character.

```python
this_is_snake_cased = 1
```

## Integers

```python

example_int = 1
example_int_type = type(1) # <class 'int'>

```

## Floats

Floats are defined as decimals

```python

example_float = 1.001
example_float_type = type(1.001) # <class 'float'>

```

## Int/Float Operators

We can operate on integers/floats in the following ways

```python
example_int = 1

another_int = example_int + 5 # addition
another_int = example_int * 5 # multiplication
another_int = example_int - 5 # subtraction
another_int = example_int / 5 # division
another_int = example_int % 5 # modulus operator
```

## Strings

Sequences of characters are called "strings"

```python
my_name = 'Taq Karim'
your_name = "John Smith" # single or double quotes are valid

string_type = type("testing") # <class 'str'>
```
You can also store several separate snippets of text within a single string. Let's say you're storing song lyrics, so you want to have a line break between each line of the song. To do this, you can use triple quotes i.e. `'''` or `"""`. You can use single and double quotes within the string freely, so no need to worry about that detail!

```python
'''
'Cause if you liked it, then you should have put a ring on it
If you liked it, then you should have put a ring on it
Don't be mad once you see that he want it
If you liked it, then you should have put a ring on it
'''
```

## String operators

We can "add" strings

```python
print("this string" + "that string") # what does this output?
```

We cannot add strings to non strings

```python
print("this will not work" + 4) # 4 is not stype str
```

As a convenience, we can format strings like so:

```python
a = 1
b = 2

formatted_string = f"{a} is {b}" # notice how a, b are formatted into string even tho they are ints

print(formatted_string) # "1 is 2"
```


## Booleans

Booleans represent true/false

```python

is_it_winter = True
is_it_warm_out = False

boolean_type = type(True) # <class 'bool'>

```

We use booleans primarily in conditional statements

## Nonetype

`None` represents variables that have not yet been defined.

```python
print(type(None)) # <class 'NoneType'>
```

## Typecasting

Sometimes, we need to convert one datatype to another. Typecasting allows us to convert between types

```python

# convert string to int
int('10') # 10 - but as type int
int('tasdfa') # throws a ValueError

```

```python

# convert int to str
str(10) # '10' - but as type str

```

```python

# convert int to bool
bool(10) # True
bool(0) # False
```

To check the type of a data type:

```python

# check types
isinstance(-1, bool) # False
isinstance(False, bool) # True

# ..etc

```

## 🚗 Problems

**[How to use the PSETS Repo](https://github.com/mottaquikarim/pydev-psets#getting-started)**

* **[PRACTICE: Shopping List Calculator I](https://github.com/mottaquikarim/pydev-psets/blob/master/pset_basic_data_types/shopping_list/p1.py)**


* **[PRACTICE: Shopping List Calculator II](https://github.com/mottaquikarim/pydev-psets/blob/master/pset_basic_data_types/shopping_list/p2.py)**


* **[PRACTICE: Shopping List Calculator III](https://github.com/mottaquikarim/pydev-psets/blob/master/pset_basic_data_types/shopping_list/p3.py)**

## 🚗 Additional Resources

* [A Repl.it Summarizing Print Statements](https://repl.it/@brandiw/Python-01-Variables-4?lite=true)
* [Python For Beginners](http://www.pythonforbeginners.com/basics/python-variables)
* [Python Programming Tutorial: Variables](https://www.youtube.com/watch?v=vKqVnr0BEJQ)
* [Variables in Python](https://www.guru99.com/variables-in-python.html)
* [Operators Cheatsheet](http://python-reference.readthedocs.io/en/latest/docs/operators/)
* [Python Style Guide: Naming](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles)
- [Python-Strings](https://www.tutorialspoint.com/python/python_strings.htm)
- [String Concatenation and Formatting](http://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python)
- [String Concatenation and Formatting - Video](https://www.youtube.com/watch?v=jA5LW3bR0Us)

