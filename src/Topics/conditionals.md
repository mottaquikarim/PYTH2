<!---
{"next": "Topics/lists.md","title": "Conditionals"}
-->

# Conditionals

In order for code to be useful, it is imperative to have the ability to make decisions. In most languages, we use the **conditional** statement to facilitate decision making. 

Before we dig deeper into conditionals, let us first examine the `Boolean` datatype.

## Booleans

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

## Greater Than / Greater Than or Equal To

```python
my_money = 37.00
total = 35.00

enough_money = my_money > total # True
just_enough_money = my_money >= total # also True
```

## Less Than / Less Than or Equal To

```python
speed_limit = 65
my_speed = 32

under_speed_limit = my_speed < speed_limit # True
at_or_under_speed_limit = my_speed <= speed_limit # also True
```

## Equal to / Not equal to

Because we use the `=` symbol for identity (ie: to set a variable), it is not available for comparison operations. Instead, we must use the `==` and `!=` symbols. 

```python
speed_limit = 65
my_speed = 32

are_they_equal = (speed_limit == my_speed) # False
are_they_not_equal = (speed_limit != my_speed) # True
```

Note that the parens are unnecessary here, but we add them anyways for the sake of clarity.

Also worth noting that the `is` keyword can be used in lieu of the `==`:

```python
pi = 3.14

result = pi is 3.14 # True
``` 

## Chaining comparison operators

```python
x = 2
# a
1 < x < 3 # True

# b
10 < x < 20 # False

# c
3 > x <= 2 # True

# d
2 == x < 4 # True
```

For **a**, we check to see if 1 is less than `x` AND `x` is less than 3.

For **b**, we check to see if 10 is less than `x` (it is not) and stop right there

For **c**, we check to see if 3 is greater than `x` AND `x` is less than or equal to 2.

For **d**, we check to see if `x` is equal to 2 AND `x` is less than 4.

## Logical operators

In addition to comparison operators, python also offers support for *logical* operators - in the form of:

1. **not**
2. **or**
3. **and**

### `not` operator

The **not** operator simply negates. For instance,

```python
is_it_cold = True

result = not is_it_cold # False
```

Likewise,

```python
is_it_hot = False

result = not is_it_hot # True
```

### `or` operator

The **or** operator evaluates to `True` if any one of the operands is true.

```python
is_it_warm = True
is_it_cold = False
is_it_foggy = False

result = is_it_warm or is_it_cold or is_it_foggy # True
```

Will be true since at least once of the items is `True`

### `and` operator

The **and** operator evaluates to `True` is all of the operands are true.

```python
is_it_warm = True
is_it_foggy = True
is_it_humid = True

result = is_it_warm or is_it_humid or is_it_foggy # True
```

Will be true since at ALL of the items are `True`

## Membership operators

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

## 🚗 [PSETS](https://github.com/mottaquikarim/pydev-psets)

The problems are reproduced below, but you will want to run on github. First,

```bash
$ . ./update
```

## 🚗 1. Generate Traffic Light

```python
from random import randint

randn = randint(1,3) # generates a random number from 1 to 3
# if 1, print 'red'
# if 2, print 'green',
# if 3, print 'blue'
```

## 🚗 2. Generate Phone Number w/Area Code

```python
from random import randint

# generate a random phone number of the form:
# 1-718-786-2825
# This should be a string
# Valid Area Codes are: 646, 718, 212
# if phone number doesn't have this area code, pick
# one of the above at random
```
## 🚗 3. Play RPS

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

## 🚗 6. Play RPS w/Bad Input

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

## 🚗 7. Play RPS against Computer

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

## 🚗 8. Calculate Grade

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

## 🚗 9. Sign of Product

Given three numbers, `a, b, c`, **without** multiplying, determine the **sign** of their product.

**EXAMPLE**: `a = -5, b = 6, c = -4`, print `1`

**EXAMPLE**: `a = 5, b = 6, c = -4`, print `-1`

## 🚗 10. Any Uppercase

Given a string `str`, determine if there are any uppercase values in it. Use only conditional statements and string methods (you may have to look some up!)

**EXAMPLE**: `str = "teSt"`, print `True`

## 🚗 11. IsEmptyString

Given any empty string, of the form:

```python
''
' '
'  '
# ...
'        ' # etc
```

determine if the `str` is empty or not (print `True` or `False`)

## 🚗 12. truthTableEvaluator

Given the following inputs:

```python
P = # True or False
Q = # True or False
op = # '^' (logical AND, conjunction)
	 # OR, 'v' (logical OR, disjunction)
	 # OR, '->' (logical conditional, implication)
	 # OR, '<->' (biconditional)
```

determine the correct outcome. 

**[Info on truthtables](https://medium.com/i-math/intro-to-truth-tables-boolean-algebra-73b331dd9b94)**

