<!---
{"next": "Topics/lists.md","title": "Conditionals"}
-->

# Conditionals

In order for code to be useful, it is imperative to have the ability to make decisions. In most languages, we use the **conditional** statement to facilitate decision making. 

Before we dig deeper into conditionals, let us first examine the `Boolean` datatype.

## Booleans & Their Operators

In short, a boolean represents a "yes" or "no" value. In python, booleans are written as:

```python
True # this is a boolean, for "yes"
False # this is a boolean, for "no"
```

Because booleans are just datatypes, we can store them into variables.

```python
is_it_summer = False
will_it_be_summer_soon = True
```

Moreover, because booleans are data types, certain operators will *evaluate* to booleans:

```python
age = 13
is_eligible_to_buy_lotto = age > 13

# ^^ this will evaluate to False and then 
# that value, False, will be stored in variable
# is_eligible_to_buy_lotto
```

The operator above, `>` is called a **boolean** operator. Notice how we stored the evaluation of the `>` expression into a variable. Remember, booleans are just datatypes, therefore they work the same way we would expect numbers and strings to work - except that the operators look / do different things (but in principle they are one and the same!)

Let's now explore the *boolean operators* available in python.

## Boolean Comparison Operators

**Comparison operators** make a statement about the relative value of two items and return a boolean based on whether that statement is True or False. These operators include:

* Less than: <
* Greater than: >
* Less than or equal to: <= 
* Greater than or equal to: >=
* Equal to: == or `is`
* Not Equal to: != `is not`

**Special note on "equality operators":** 

Because we use the `=` symbol for identity (i.e. to set a variable), it is not available for comparison operations. Instead, we must use the `==` and `!=` symbols.

Now, let's walk through this contextual example where we'll compare a driver's speed to the speed limit.

```python
# Speed Limit Example

speed_limit = 65
my_speed = 32


# Less Than <
under_speed_limit = my_speed < speed_limit # True


# Less Than or Equal To <=
at_or_under_speed_limit = my_speed <= speed_limit # True


# Greater Than >
above_speed_limit = my_speed > speed_limit # False


# Greater Than or Equal To >=
at_or_under_speed_limit = my_speed > speed_limit # False


# Equals ==
exactly_at_speed_limit = my_speed == speed_limit # False
exactly_at_speed_limit = my_speed is speed_limit # also False

# Not Equal To !=
not_exactly_at_speed_limit = my_speed != speed_limit # True
not_exactly_at_speed_limit = my_speed is not speed_limit # also True
```

### Chaining Comparison Operators

When you chain comparison operators, it's simply a way of succintly checking whether **BOTH** comparison expressions are `True` or `False`. 

Python checks each one separately from left to right. Both comparisons must be `True` for the result to evaluate to `True`. Even if only one of them is `False`, the whole expression will evaluate to `False`. Thus, if any comparisons are `False`, it stops before evaluating the rest of them. 

Let's see this in action...

```python
x = 2

# A)
1 < x < 3 # True

# B)
10 < x < 20 # False

# C)
3 > x <= 2 # True

# D)
2 == x < 4 # True
```

For the above examples, we check whether...

* A) 1 is less than `x` **AND** `x` is less than 3.
* B) 10 is less than `x` (*it is not) and we stop right there*
* C) 3 is greater than `x` **AND** `x` is less than or equal to 2.
* D) `x` is equal to 2 **AND** `x` is less than 4.

## Boolean Logical Operators

**Logical operators** ALSO make a statement about the relative value of two items and return a boolean based on whether that statement is True or False. The logical operators include `not`, `or`, and `and`.

**The `not` operator** simply negates. The statement evaluates to `True` if item is False and vice versa. For instance,

```python
sky_is_blue = True
result = not sky_is_blue # False


sky_is_green = False
result = not sky_is_green # True
```

A statement with **The `or` operator** evaluates to `True` if **AT LEASE ONE** of the items are `True.` For instance, 

```python
layla_is_maine_coon = True
layla_is_black = False
layla_is_female = True

result = layla_is_maine_coon or layla_is_black or layla_is_female # True
```

Because at least one of the items above is `True`, the full expression will evaluate to `True`.

**The `and` operator** evaluates to `True` if **ALL** of the operands are true.

```python
layla_is_maine_coon = True
layla_is_white = True
layla_is_orange = True
layla_is_black = False

result1 = layla_is_maine_coon and layla_is_orange and layla_is_female # True

result2 = layla_is_maine_coon and layla_is_black and layla_is_female # False
```

`result1` above will be true since **ALL** of the items are `True`. Conversely, `result2` above will be `False` because **at least one** of the items is `False`.

### Chaining Logical Operators

When you chain logical operators, it's simply a way of succintly checking whether **ALL** logical expressions are `True`. When you combine chains of logical operators, you have to pay close attention to the **order of operations**: `not` then `and` then `or`.

Let's break down a few examples:

A) **and THEN or**

```python
layla_is_white = True
layla_is_orange = True
layla_is_black = False


result1 = (layla_is_white and layla_is_orange) or layla_is_black
# (True and True) or False evals to...
### True or False evals to evals to...
### True

result2 = layla_is_white or (layla_is_black and layla_is_orange)
# True or (False and True) evals to...
### True or False evals to...
### True

result3 = (layla_is_white and (not layla_is_black)) or layla_is_orange
# (True and (True)) or True
# layla_is_white and (True) or layla_is_orange
# True and True or True
### True and True evals to True
### True or True evals to True

result4 = layla_is_white and layla_is_black or not layla_is_orange
# True and False or not True
# True and False or False
# False
# STOP! No need to eval rest

result5 = layla_is_white or layla_is_black and not layla_is_orange
# True or False and not True
# True or False and False
# True or False
# True

result6 = layla_is_white and layla_is_black and not layla_is_orange
# True and False and not True
# True and False and False
# True and False
# False
```

Summarized, the results above are:

* results1 = `True`
* results2 = `True`
* results3 = `True`
* results4 = `False`
* results5 = `True`
* results6 = `False`

## Boolean Membership Operators

Membership operators are: `in` and `not in`. They are used to determine if a value is in a sequence, for instance:

```python
line = 'a b c d e f g'

result = 'a' in line # True
result = 'z' in line # False
result = 'k' not in line # True
result = 'a' not in line # False
```

## Conditional Statements

A conditional will attempt to evaluate an expression down to a boolean value - either `True` or `False`. Based on the boolean evaluation, the program will then execute or skip a block of code.

So for instance:

```python
if True:
	print("this will always run!")

if False:
	print("this will NEVER run!")
```

However, since we know booleans to be datatypes, *any* of the operators discussed above can *also* be used:

```python
temp = 43

if temp < 65:
	print("wear a jacket!")
```

The code above will only run if `temp` is less than 65.

We can also do something like:

```python
temp = 43
is_it_raining = True

if is_it_raining and temp < 65:
	print('wear a jacket and bring an umbrella!')
```

In the example above, we make use of comparison operators *and* logical operators in a compound statement.

## `else`s and `elif`s

If we have a condition that can only go two ways (ie: it will only be true or false), we can leverage the `else` statement:

```python
temp = 43

if temp < 65:
	print('wear a coat!')
else:
	print('you will not need a coat!')
```

But what if we wanted support for multiple possibilities? That's where the `elif` statement comes in:

```python
temp = 43

if temp < 30:
	print('wear a heavy jacket')
elif temp < 50:
	print('wear a light jacket')
elif temp < 60:
	print('wear a sweater')
else:
	print('you do not need any layers!')
```

In the example above, we print one of 4 possibilities - the elif allows us to go from 2 potential conditions to N potential conditions.

## [PSETS](https://github.com/mottaquikarim/pydev-psets)

The problems are reproduced below, but you will want to run on github. First,

```bash
$ . ./update
```

## 1. Generate Traffic Light

```python
from random import randint

randn = randint(1,3) # generates a random number from 1 to 3
# if 1, print 'red'
# if 2, print 'green',
# if 3, print 'blue'
```

## 2. Generate Phone Number w/Area Code

```python
from random import randint

# generate a random phone number of the form:
# 1-718-786-2825
# This should be a string
# Valid Area Codes are: 646, 718, 212
# if phone number doesn't have this area code, pick
# one of the above at random
```
## 3. Play RPS

```python

p1 = 'r' # or 'p' or 's'
p2 = 'r' # or 'p' or 's'

# Given a p1 and p2
# print 1 if p1 has won
# print 2 if p2 has won
# print 0 if tie
# print -1 if invalid input
# expects both p1 and p2 inputs to be either
# "r", "p", or "s"
```

## 🚗 4. Play RPS w/Computer


```python
from random import randint

p1 = # randomly choose 'r' or 'p' or 's'
p2 = # randomly choose 'r' or 'p' or 's'

# Given a p1 and p2
# print 1 if p1 has won
# print 2 if p2 has won
# print 0 if tie
# print -1 if invalid input
# expects both p1 and p2 inputs to be either
# "r", "p", or "s"

```

## 🚗 5. Play RPS w/Input

```python

p1 = # from user input
p2 = # from user input

# Given a p1 and p2
# print 1 if p1 has won
# print 2 if p2 has won
# print 0 if tie
# print -1 if invalid input
# expects both p1 and p2 inputs to be either
# "r", "p", or "s"
```

## 6. Play RPS w/Bad Input

This is the same as the original RPS problem, except that cannot expect the input to be valid. While we *want* `r` or `p` or `s`, there is a possibility that input can be anything like...

* `ROCK` (all caps)
* `R` (`r` but capitalized)
* `PAPrrRR` (incorrectly spelled, upper/lowercased)

Implement conditional statements that will sanitize the user input or let user know that input is invalid.

```python
p1 = # from user input
p2 = # from user input

# Given a p1 and p2
# print 1 if p1 has won
# print 2 if p2 has won
# print 0 if tie
# print -1 if invalid input
# expects both p1 and p2 inputs to be either
# "r", "p", or "s"
```

## 7. Play RPS against Computer

```python

p1 = # from user input - we still want validation from above!
p2 = # randomly generated against computer

# Given a p1 and p2
# print 1 if p1 has won
# print 2 if p2 has won
# print 0 if tie
# print -1 if invalid input
# expects both p1 and p2 inputs to be either
# "r", "p", or "s"

```

## 8. Calculate Grade

```python
grade = 15 # expect this to be a number

# write a program that will print the "letter" 
# equivalent of the grade, for example:
# when grade = 90 # -> expect A
# when grade = 80 # -> expect B
# when grade = 70 # -> expect C
# when grade = 60 # -> expect D
# when grade = 54 # -> expect F
# when grade = -10 # -> expect Error
# when grade = 10000 # -> expect Error
# when grade = "lol skool sucks" # -> expect Error
```

**Challenge**: Can you `raise` an error if unexpected input supplied vs just printing out `Error`? What's the difference?

## 9. Sign of Product

Given three numbers, `a, b, c`, **without** multiplying, determine the **sign** of their product.

**EXAMPLE**: `a = -5, b = 6, c = -4`, print `1`

**EXAMPLE**: `a = 5, b = 6, c = -4`, print `-1`

## 10. Any Uppercase

Given a string `str`, determine if there are any uppercase values in it. Use only conditional statements and string methods (you may have to look some up!)

**EXAMPLE**: `str = "teSt"`, print `True`

## 11. IsEmptyString

Given any empty string, of the form:

```python
''
' '
'  '
# ...
'        ' # etc
```

determine if the `str` is empty or not (print `True` or `False`)

