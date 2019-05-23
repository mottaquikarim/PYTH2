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

#### p1. Placeholders

You're writing a program, and you don't know what your starting value for your 'initial' variable is yet. The program won't run if you leave it blank, but you don't want to forget you need it! Make a workaround.

```python

```

#### p2. Basic Variables

* A) Create a variable that represents your favorite number, and add a note to remind yourself what this variable represents. Now print it out without re-typing the number.

* B) Create another variable that represents your favorite color, and do the same steps as above.


```python

```

#### p3. String Formatting

Create a variable that contains the first 4 lines of your favorite song. Add a comment that includes the song title and artist **each on their own line**! Now print out this variable.

```python

```

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

#### p1. Typcasting w. Integers & Floats

Convert the below numbers into floats and back. Print out each result as well as its data type.


```python
five = 5
zero = 0
neg_8 = -8
neg_22 = -22

```

#### p2. Typcasting w. Strings

Convert the below numbers into floats and back. Print out each result as well as its data type.

```python
five = 5
zero = 0
neg_8 = -8
T = True
F = False

```

#### p3. Typecasting Booleans I

* A) Use typecasting to turn the below variables into boolean values. Print the result and the datatype of the result.
* B) Use typecasting to turn the resultant variables from part A into floats. Print the result and the datatype of the result.
* C) Use typecasting to turn the resultant variables from part B back into booleans. Print the result and the datatype of the result.
* D) Use typecasting to turn the resultant variables from part C into integers. Print the result and the datatype of the result.
* E) Use typecasting to turn the variable below into a boolean value. Print the result and the datatype of the result.

```python
one = 1
zero = 0

```

#### p4. Typecasting Booleans II

* A) Use typecasting to turn the below variables into boolean values. Print the result and the datatype of the result.
* B) Use typecasting to turn the latest values for variables 'one' and 'zero' back into integers. Print the result and the datatype of the result.
* C) Use typecasting to turn the latest values for variables 'bool_true' and 'bool_false' back into boolean values. Print the result and the datatype of the result.

```python
one = 1
zero = 0
T = True
F = False

```

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

#### p1. Integer & Float Operators

Complete the specified math operations. Do the next operation on the result from the previous operation.

orig_var = 100

* A) Add 50
* B) Subtract 90
* C) Multiply 10
* D) Divide 150
* E) Modulus 3

```python

```

#### p2. String Operators

Create two variables, each of which is half of a compound sentence. Do NOT add any punctuation up front. Add the two variables together, and print the result.

*Example compound sentence:* "I'll go to the beach today and I'll go snorkeling"

```python

```

### Practice Problem Set 4: Put it all together!

#### p1. Shopping List Calculator I

*(see directions in code below)*

**Hint**: You can decide the number of decimal places to show from floats using the below. However, it returns a string! If you want to do math with it, you have to convert it back to a float.

```python
print(format(3.14159, '.2f')) # 3.14
```

```python
# A) Create five variables, and set them to strings that represent 5 common shopping list items
item_name_1 = None
item_name_2 = None
item_name_3 = None
item_name_4 = None
item_name_5 = None


# B) Create five more variables, and set them to floats that represent the prices of each of the items above
item_price_1 = None
item_price_2 = None
item_price_3 = None
item_price_4 = None
item_price_5 = None

# C) Create five more variables, and set them to ints that represent the quantity of each of the items above
item_quant_1 = None
item_quant_2 = None
item_quant_3 = None
item_quant_4 = None
item_quant_5 = None

# D) *Print to the console the name and price of each item defined above per the following example:*
"""
1 Coco Puffs = $8.95, where:
   1 would be item_quant_1
   Coco Puffs would be item_name_1
   8.95 would be item_name_2
"""


```

#### p2. Shopping List Calculator II

* Rewrite p1, but this time use the `input()` function to solicit user input for name, price, quantity. Here's how it works:

```python
item_name_1 = input('Name your first item')
# this will ask user to input value of item_name_1
```

```python
# A) Create five variables, and set them to strings that represent 5 common shopping list items
item_name_1 = None
item_name_2 = None
item_name_3 = None
item_name_4 = None
item_name_5 = None


# B) Create five more variables, and set them to floats that represent the prices of each of the items above
item_price_1 = None
item_price_2 = None
item_price_3 = None
item_price_4 = None
item_price_5 = None

# C) Create five more variables, and set them to ints that represent the quantity of each of the items above
item_quant_1 = None
item_quant_2 = None
item_quant_3 = None
item_quant_4 = None
item_quant_5 = None

# D) *Print to the console the name and price of each item defined above per the following example:*
"""
1 Coco Puffs = $8.95, where:
   1 would be item_quant_1
   Coco Puffs would be item_name_1
   8.95 would be item_name_2
"""


```


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
