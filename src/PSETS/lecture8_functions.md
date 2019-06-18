#  FUNCTIONS

## BASIC_FUNCTION_OPS

### P1.PY



```python
"""
Function Basics I - No Input
"""

# Write a and call a function called "rand_list" that generates a list of 5 random numbers between 1 and 500. Print out that list.


```


### P2.PY



```python
"""
Function Basics II - Arguments
"""

# Write a and call function called "names" that separately intakes a person's first name and a person's last name. It should concatenate the names and return the person's full name.


```


### P3.PY



```python
"""
Function Basics III - Default Arguments
"""

# Now write a and call function called "fave_colors" that separately intakes a person's first name, a person's last name, and **optionally** their favorite color.

# The function should create and return a dict with the full name as a key and the favorite color as the value. If the person does not enter a favorite color, you should assume they have no favorite color and assign theirs to None. Try both use cases.


```


### P4.PY



```python
"""
Function Basics IV - Multiple Return Values
"""

# Write a and call a function called "figures" that takes any two numbers and **individually** returns the following as integers:
# their sum
# their product
# the quotient for num1 / num2

"""Print each value out individually in this format:
(using 12 and 3)
sum: 15
product: 36
quotient: 4
"""


```


### P5.PY



```python
"""
Function Basics V - Indeterminate Arguments
"""

# Write a and call a function called "high_low" that takes 3 numbers and returns the highest and lowest ones.


```


## DB_SEARCH

### P1.PY



```python
"""
GPA Calculator
"""

# Write a function called "simple_gpa" to find GPA when student enters a letter grade as a string. Assign the result to a variable called "gpa".

"""
Use these conversions:
A+ --> 4.0
A --> 4.0
A- --> 3.7
B+ --> 3.3
B --> 3.0
B- --> 2.7
C+ --> 2.3
C --> 2.0
C- --> 1.7
D+ --> 1.3
D --> 1.0
D- --> 0.7
F --> 0.0
"""


```


### P2.PY



```python
"""
RGB to HEX
"""

# Write a and call a function called "rgb_hex" that takes a parameter called "color." The function should be able to intake a color in rgb format and return it in hex format as well as vice versa. A sample of color conversions are below. Write in logic so the function can interpret rgb and hex colors entered in different formats such as "rgb_hex((255,255,255))" or "rgb_hex('ffffff')". Also make sure to account for someone inputting a color not in the database.

color_conversions = {
'#4286f4': 'rgb(66, 134, 244)',
'#5905c6': 'rgb(89, 5, 198)',
'#fce702': 'rgb(252, 231, 2)',
'#ffffff': 'rgb(255, 255, 255)',
'#000000': 'rgb(0, 0, 0)',
'#0ac913': 'rgb(10, 201, 19)',
'#65c672': 'rgb(101, 198, 114)',
'#f8d6ff': 'rgb(248, 214, 255)',
'#b70782': 'rgb(183, 7, 130)',
'#001184': 'rgb(0, 17, 132)',
'#495eed': 'rgb(73, 94, 237)',
'#b7ffb8': 'rgb(183, 255, 184)',
'#ffbf00': 'rgb(255, 191, 0)',
'#7a020e': 'rgb(122, 2, 14)',
'#ff5e6e': 'rgb(255, 94, 110)',
'#22003d': 'rgb(34, 0, 61)'
}


```


## MATH

### P1.PY



```python
"""
Simple Interest Calculator
"""

# Write a function called "simple_interest" that will allow a user to find out how much they will have in savings based on their current funds and an interest rate. (Instead of collecting user input, you can directly pass values of your choosing for the arguments.)

# The formula for simple interest is...
# A = P(1 + rt), where...
# P = principal amount of money
# r = interest rate
# t = number of time periods the principal will earn interest


```


### P2.PY



```python
"""
Permutations & Combinations
"""

# Create two functions:
	# One called "perms", which outputs the **number** of possible **permutations** of rolling two 6-sided dice and assign it to a variable called "permutations".
	# One called "combs", which outputs the **number** of possible **combinations** of rolling two 6-sided dice and assigns it to a variable called "combinations".
	# Hint: The formulas for these are below, where n is the number of possible outcomes for one trial and r is the number of outcomes you will pick at a time. The contextual difference is that order matters for permutations, meaning the same two numbers in a different order count as two unique permutations. For combinations, the order doesn't matter.

# permutation formula = n! / (n-r)!
# combination formula = n! / (nâr)!r!


```


### P3.PY



```python
"""
Multiples
"""

# Write a function called "sum_multiples" that take two numbers and returns the sum of their multiples between 0 and some limit. These three items should be generalized as parameters.


```


## DATA_MANIPULATION

### P1.PY



```python
"""
File Organization
"""

# The dict "files" below contains file names and the name of the person who owns each file. Write and call a function to reorganize "files" such that it contains each person's name and the files he/she owns. Assign the resultant dict to a new dict called "grouped_by_owner". Print out the key value pairs in this format - key: value.

# Function name should be: group_by_owners
# Dict of results should be named: files_by_owner

files = {
  'Input1.txt': 'Beau',
  'Code1.py': 'Mischa',
  'Output1.txt': 'Beau',
  'Input2.txt': 'Beau',
  'Code2.py': 'Mischa',
  'Output2.txt': 'Beau',
  'Input3.txt': 'Percy',
  'Code3.py': 'Alejandra',
  'Output3.txt': 'Percy'
}



```


### P2.PY



```python
"""
Clean Pairs
"""

# Below is a list of common food pairings. Write a function called "cleaner" that cleans the data such that each list item is a tuple (e.g. ('Milk', 'Cookies')). Assign the results to a variable called "clean_pairs".

pairs = [('Milk', 'Cookies'), ('Peanut Butter - Jelly'), ('Spaghetti & Meatballs'), ('Eggs', 'Bacon'), ('Pancakes & Syrup'), ('Chicken - Waffles'), ('Peas', 'Carrots')]



```


### P3.PY



```python
"""
Password Requirements
"""

# Write a Python program called "pw_validator" to validate a password based on the security requirements outlined below.

# VALIDATION REQUIREMENTS:
## At least 1 lowercase letter [a-z]
## At least 1 uppercase letter [A-Z].
## At least 1 number [0-9].
## At least 1 special character [~!@#$%&*].
## Min length 6 characters.
## Max length 16 characters.


```


### P4.PY



```python
"""
Rainbows & Wobniars
"""

# Write a function called "wobniar", which should contain the local variable "rainbow" below. The function should collect every other color of the rainbow starting at index 0 and add each one to a new list. When you add each color, it should be spelled backwards. For example, the word 'sing' would be added to the new list as 'gnis'. Return and print the list.


```


## CHALLENGES

### P1.PY



```python
"""
Sum of Squares
"""


# Write a function called "sum_squares" that finds the sum of the squares of any number of integers passed into the function.

# For example, someone could enter three individual integers, a list of five integers, or a tuple nested in a list of eight integers.

# Hint: The solution tests out different scenarios, so you can pass those numbers into your function to see if you can get the same answer for different scenarios.


```


### P2.PY



```python
"""
Speeding Tickets
"""

# Imagine you're a cop waiting on the side of the road to pick up speeders. Write a function called "speeders" to check the speed of drivers and record their license plate numbers.
## If speed is less than or equal 70 (mph), it should print "Good". 
## If the speed is greater than 70, find the license plate number of that driver in your "driver_points" dict (see below) and add a point to their license for every 5 full mph above the speed limit.
## If at any point that driver has 12 or more points on his/her license, print "License Suspended".
## Call the function on each driver in the "passing_cars" dict below to see difference use cases work.

# p.s. Feel free to move these around in your code as needed.
passing_cars = { # license plate nums & speed
  '4GRONPH': 68,
  'OJGL6WD': 82,
  'Q5517FA': 70,
  'S0PNWEJ': 95,
  'RM23RXC': 64,
  'KH5TH8D': 100,
  'IHEHJ4P': 67,
  'SVK90LT': 73,
  'LJSV4N1': 88,
  'KDRLGXM': 91
}

driver_points = { # license plate nums & points
  '4GRONPH': 8,
  'OJGL6WD': 12,
  'Q5517FA': 1,
  'S0PNWEJ': 2,
  'RM23RXC': 6,
  'KH5TH8D': 7,
  'IHEHJ4P': 10,
  'SVK90LT': 5,
  'LJSV4N1': 3,
  'KDRLGXM': 9
  }



```

