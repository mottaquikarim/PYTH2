#  CONDITIONALS

## WEATHER

### P1.PY



```python
"""
Weather I - Do you need boots?
"""

# Use the values of the vars defined below to ouput the correct contextual answer to the questions below. (Note: The variables themselves ARE the questions.)

# Example:
## am_i_hungry = False
## am_i_tired = True
## do_i_need_to_stay_awake = False

## should_i_drink_coffee_now = am_i_tired and do_i_need_to_stay_awake

## ^^ This ^^ evaluates to False. If you're tired and don't need to stay awake, you don't need to drink coffee!


is_it_raining = True
is_it_snowing = False


do_i_need_snow_boots = None
can_i_skip_snow_boots = None
do_i_need_rain_boots = None
can_i_skip_rain_boots = None
```


### P2.PY



```python
"""
Weather II - Precipitation
"""

# Repeat the same process as p1, using this new set of variables.

sunny = True
raining = True
snowing = False

is_it_sunny = None
is_there_precipitation = None
is_it_sleeting = None
is_there_rainbow = None
```


### P3.PY



```python
"""
Weather III - Describe Conditions
"""

# Repeat the same process as p1, using this new set of variables.


is_it_warm = True
is_it_humid = True
is_it_cold = False
is_it_icy = False
is_it_foggy = False
is_it_windy = False
is_it_overcast = True


is_it_summer_weather = None
is_rain_coming = None
is_it_muggy = None
do_i_need_coat = None


```


## LOGIC

### P1.PY



```python
"""
Calculate Grade
"""

grade = 15  # expect this to be a number

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


### P2.PY



```python
"""
Sign of Product
"""

# Given three numbers, a, b, c, without multiplying, determine the sign of their product.

# EXAMPLE: a = -5, b = 6, c = -4, print 1

# EXAMPLE: a = 5, b = 6, c = -4, print -1

```


### P3.PY



```python
"""
Any Uppercase
"""

# Given a string str, determine if there are any uppercase values in it. Use only conditional statements and string methods (you may have to look some up!)

# EXAMPLE: str = "teSt", print True

```


### P4.PY



```python
"""
Empty Strings
"""

# Given any empty string, of the form:

# ''
# ' '
# '  '
# any other num of spaces...

# determine if the str is empty or not (print True or False). Hint: You'll need to look up how to remove trailing spaces from a string.

```


### P5.PY



```python
"""
truthTableEvaluator
"""

# Given the following inputs:


# P = # True or False
# Q = # True or False
# op = # '^' (logical AND, conjunction)
#      # OR, 'v' (logical OR, disjunction)
#      # OR, '->' (logical conditional, implication)
#      # OR, '<->' (biconditional)
# determine the correct outcome.

# https://medium.com/i-math/intro-to-truth-tables-boolean-algebra-73b331dd9b94

```


## RANDOM_NUMS

### P1.PY



```python
"""
Generate Traffic Light
"""

# import python randomint package


# generates a random number from 1 to 3


# if 1, print 'red'
# if 2, print 'green',
# if 3, print 'yellow'

```


### P2.PY



```python
"""
Generate Phone Number w/Area Code
"""

# Generate a random phone number using these SPECS:
### Should be a string in this format: 1-718-786-2825
### Must randomly choose one of these area codes: 646, 718, 212
```


## RPS

### P1.PY



```python
"""
Play RPS
"""

p1 = 'r'  # or 'p' or 's'
p2 = 'r'  # or 'p' or 's'

# Given a p1 and p2
# print 1 if p1 has won
# print 2 if p2 has won
# print 0 if tie
# print -1 if invalid input
# expects both p1 and p2 inputs to be either
# "r", "p", or "s"

```


### P2.PY



```python
"""
Play RPS w/Computer
"""

import random

p1 = None  # randomly choose 'r' or 'p' or 's'
p2 = None  # randomly choose 'r' or 'p' or 's'

# Given a p1 and p2
# print 1 if p1 has won
# print 2 if p2 has won
# print 0 if tie
# print -1 if invalid input
# expects both p1 and p2 inputs to be either
# "r", "p", or "s"

```


### P3.PY



```python
"""
Play RPS w/Input
"""

p1 = None  # from user input
p2 = None  # from user input

# Given a p1 and p2
# print 1 if p1 has won
# print 2 if p2 has won
# print 0 if tie
# print -1 if invalid input
# expects both p1 and p2 inputs to be either
# "r", "p", or "s"

```


### P4.PY



```python
"""
Play RPS against Computer
"""

p1 = None  # from user input - we still want validation from above!
p2 = None  # randomly generated against computer

# Given a p1 and p2
# print 1 if p1 has won
# print 2 if p2 has won
# print 0 if tie
# print -1 if invalid input
# expects both p1 and p2 inputs to be either
# "r", "p", or "s"

```


### P5.PY



```python
"""
Play RPS w/Bad Input
"""

p1 = None  # can be invalid!
p2 = None  # can be invalid!

"""
This is the same as the original RPS problem, 
except that cannot expect the input to be valid. 
While we *want* `r` or `p` or `s`, there is a possibility 
that input can be anything like...

* `ROCK` (all caps)
* `R` (`r` but capitalized)
* `PAPrrRR` (incorrectly spelled, upper/lowercased)

Implement conditional statements that will sanitize the 
user input or let user know that input is invalid.
"""

```

