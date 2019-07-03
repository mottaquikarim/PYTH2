#  BASIC DATA TYPES

## BASICS

### P1.PY



```python
"""
Placeholders
"""

# You're writing a program, and you don't know what your starting value for your 'initial' variable is yet. The program won't run if you leave it blank, but you don't want to forget you need it! Make a workaround.


```


### P2.PY



```python
"""
Basic Variables
"""

# Create a variable that represents your favorite number, and add a note to remind yourself what this variable represents. Now print it out without re-typing the number.



# Create another variable that represents your favorite color, and do the same steps as above.


```


### P3.PY



```python
"""
String Formatting
"""

# Create a variable that contains the first 4 lines of your favorite song. Add a comment that includes the song title and artist **each on their own line**! Now print out this variable.


```


## OPERATORS

### P1.PY



```python
"""
Integer & Float Operators
"""

# Complete the specified math operations. Do the next operation on the result from the previous operation.

orig_var = 100

# Add 50

# Subtract 90

# Multiply 10

# Divide 150

# Modulus 3

```


### P2.PY



```python
"""
String Operators
"""

# Create two variables, each of which is half of a compound sentence. Do NOT add any punctuation up front. Add the two variables together, and print the result.
## Example compound sentence: "I'll go to the beach today, and I'll go snorkeling." 
```


### P3.PY



```python
"""
Addition I - Numbers & Strings
"""

# Add the below sets of variables together.

# A)
a = 0
b = 2



# B)
c = '0'
d = '2'



# C)
e = "0"
f = 2
```


### P4.PY



```python
"""
Addition II - Booleans
"""

# Add the below sets of variables together.

# A)
a = True
b = True



# B)
c = False
d = False



# C)
e = True
f = False
```


## TYPECASTING

### P1.PY



```python
"""
Typcasting w. Integers & Floats
"""

# Convert these numbers into floats and back. Print out each result as well as its data type.

five = 5
zero = 0
neg_8 = -8
neg_22 = -22
```


### P2.PY



```python
"""
Typcasting w. Strings
"""

# Convert these variables into strings and then back to their original data types. Print out each result as well as its data type. What do you notice about the last one?

five = 5
zero = 0
neg_8 = -8
T = True
F = False
```


### P3.PY



```python
"""
Booleans I - Typecasting w. Numbers
"""

# A) Use typecasting to turn these variables into boolean values. Print the result and the datatype of the result. 

one = 1
zero = 0


# B) Use typecasting to turn the resultant variables from part A into floats. Print the result and the datatype of the result.


# C) Use typecasting to turn the resultant variables from part B back into booleans. Print the result and the datatype of the result.


# C) Use typecasting to turn the resultant variables from part C into integers. Print the result and the datatype of the result.


# E) Use typecasting to turn the variable below into a boolean value. Print the result and the datatype of the result. 

ten = 10


```


### P4.PY



```python
"""
Booleans II - Typecasting w. Strings
"""

# A) Use typecasting to turn these variables into boolean values. Print the result and the datatype of the result. 

one = 1
zero = 0
bool_true = True
bool_false = False


# B) Use typecasting to turn the latest values for variables 'one' and 'zero' back into integers. Print the result and the datatype of the result.



# C) Use typecasting to turn the latest values for variables 'bool_true' and 'bool_false' back into boolean values. Print the result and the datatype of the result.





```


## SHOPPING_LIST

### P1.PY



```python
"""
Shopping List Calculator I
"""

# Create five variables,
# set them to strings that represent 5 common shopping list items


item_name_1 = None
item_name_2 = None
item_name_3 = None
item_name_4 = None
item_name_5 = None

# Create five more variables,
# set them to floats that represent the prices of each of the items above

item_price_1 = None
item_price_2 = None
item_price_3 = None
item_price_4 = None
item_price_5 = None

# Create five more variables,
# set them to ints that represent the quantity of each of the items above
item_quant_1 = None
item_quant_2 = None
item_quant_3 = None
item_quant_4 = None
item_quant_5 = None

# Print to the console the name and price of each item defined above as follows:
# 1 Coco Puffs = $8.95.
# where:
# 1 would be item_quant_1
# Coco Puffs would be item_name_1
# 8.95 would be item_name_2

```


### P2.PY



```python
"""
Shopping List Calculator II
"""

# Rewrite p1, but this time use the input() command to solicit user input for name, price, quantity. Here's how it works:

item_name_1 = input('Name your first item: ') 
	# ^ this will ask user to input value of item_name_1

# use input() function and ask user to name items
item_name_1 = None
item_name_2 = None
item_name_3 = None
item_name_4 = None
item_name_5 = None

# use input() function and ask user to name prices
item_price_1 = None
item_price_2 = None
item_price_3 = None
item_price_4 = None
item_price_5 = None

# use input() function and ask user to name quants
item_quant_1 = None
item_quant_2 = None
item_quant_3 = None
item_quant_4 = None
item_quant_5 = None

# Print to the console the name and price of each item defined above as follows:
# 1 Coco Puffs = $8.95.
# where:
# 1 would be item_quant_1
# Coco Puffs would be item_name_1
# 8.95 would be item_name_2

# JUST REMEMBER: now this will be defined by the user!!

```


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

# import python randomint package


# generate a random phone number of the form:
# 1-718-786-2825
# This should be a string
# Valid Area Codes are: 646, 718, 212
# if phone number doesn't have [646, 718, 212]
# as area code, pick one of the above at random

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


#  LISTS

## LIST_OPS

### P1.PY



```python
"""
Basic List Operations I
"""

# Create a list including these five animals - elephant, tiger, otter, orangutan, and penguin.


# Print the 4th animal on the list.


# Add 'tortoise' to the beginning of the list.


# Print the length of the list.


# Remove 'orangutan' from the list.


# Sort the list alphabetically and print it out.

```


### P2.PY



```python
"""
Basic List Operations II
"""

# Declare a list with 5 names, and print out the length of that list.
names = None

# Print the 3rd name on the list



# Delete the first name on the list



# Re-add the name you deleted to the end of the list



# Replace the 2nd name on the list with a new name.



# Add 3 new names to the end of the list.



```


### P3.PY



```python
"""
Math Operations
"""

# Save a list with the numbers `2`, `4`, `6`, and `8` into a variable called `numbers`. Use this variable for all the problems in this PSET.

numbers = None

# Print the max of `numbers`.


# Pop the last element in `numbers` off; re-insert it at index `2` and print the resultant list.



# Pop the second number in `numbers` off.



# Append `3` to `numbers`.



# Print out the average number.



```


### P4.PY



```python
"""
Ordering Random Numbers
"""

# Create a list of 6 randomly generated numbers called numbers and sort it in descending order.


```


## LIST_MANIPULATION

### P1.PY



```python
"""
Phone Numbers
"""

# Parse this phone number so that a computer can process
# it. (Hint: It can't include any non-numeric
# characters.)

cell = '1.192.168.0143'
```


### P2.PY



```python
"""
Basic Math Ops
"""

# Given the list below, assign the correct values to the variables below.
	# my_sum = 
	# my_min = 
	# my_max = 
	# my_range = 
	# my_mean =

nums = [2, 19, 20, 12, 6, 24, 8, 30, 28, 25]


# Once you finish, print out each value **on its own line** in this format: "my_median = " etc.


```


### P3.PY



```python
"""
Merge Lists with Duplicates
"""

# Use the two lists below to solve this problem. Print out the result from each section as you go along.

list1, list2 = [2, 8, 6], [10, 4, 12]


# A) Add another instance of each item in list1 to list1 again and assign the results to list3.
list3 = None


# B) Combine the two given lists and assign them to list4.
list4 = None


# C) Replace the first 3 items in list 3 with the numbers 13, 16, 9.
list3[:2] = None

# D) Merge list3 and list4 to create a list containing no duplicates and store this in list5.
list5 = None


# Take a look at your printed statements to see the evolution of your lists with each step of this problem.

```


### P4.PY



```python
"""
Spotify Playlists - Sorting
"""

# You work for Spotify and are creating a feature for users to alphabetize their playlists by song title. Below is a list of titles from a sample playlist.

playlist_titles = ['Tiny Dancer', 'At Last', 'Fortunate Son', 
'Hey Jude', 'Isn\'t She Lovely', 'Just the Way You Are', 'I\'m Yours',
'Vienna', 'Roxanne', 'Dancing in the Moonlight']

# Alphabetize these songs and print the result.



# Now do the reverse.


```


### P5.PY



```python
"""
Cool Runnings!
"""

# Here's a quote from the movie 'Cool Runnings'. :)

# Replace the word bobsled with "YOLO" and print the resultant list as 4 sentences (i.e. NOT a list), each on a new line.

cool_runnings = [
	'Feel', 'the', 'rhythm.',
	'Feel', 'the', 'rhyme.',
	'Get', 'on', 'up.',
	'It\'s', 'bobsled', 'time!'
]


```


## LIST_CHALLENGES

### P1.PY



```python
"""
CHALLENGE - Extensions
"""

# ** Challenge** Add each element of the tuple1 to list1 *individually* and print the result.

list1 = [6, 12, 9, 4, 10, 1]
tuple1 = [(15,3), (6,2), (1, 8)]

```


### P2.PY



```python
"""
CHALLENGE - Core Statistics Calculations
"""

# Given the sample below, find the mean, median, mode, variance, and standard deviation of this sample. Print them out separately, but in the same format as before.
	# my_median = 
	# my_mode = 
	# my_variance = 
	# my_sd = 

sample = [6, 19, 20, 12, 6, 24, 8, 30, 28, 25]


# Once you finish, print out each value **on its own line** in this format: "median = " etc.

```

