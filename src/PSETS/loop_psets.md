#  LOOPS

## LOOP_BASICS

### P1.PY

```python
"""
Odds & Evens
"""

# Use a loop to make a list of all odd numbers between 1 and 10 and another list with all the evens. When done, print the lists.

# odds = 

# evens = 


```


### P2.PY



```python
"""
Lists with Duplicates
"""

# First, print list a below as it is now.

a = [2, 4, 10, 20, 5, 2, 20, 4]
b = [13, 2, 25, 20, 4, 8]

# Using a loop, remove the duplicate items from list a and print out the updated list.


# Using a loop, merge list b into list a without adding any duplicates.
```


### P3.PY



```python
"""
Temperature Conversions
"""

# You're studying climate change, and over the last 3 years, you've recorded the temperature at noon every day in degrees Fahrenheit (F). The var sampleF holds a portion of those recordings. 

sampleF = [71.6, 82.4, 91.4, 107.6, 125.6]

# Convert each item in this list into degrees Celsius and add the results to a dict called sample_temps so that the conversion of each day's temperature is easily accessible. For reference, the conversion equation between F and C is:
# Celsius = (Fahrenheit - 32) * 5.0/9.0


# sample_temps = 


```


### P4.PY



```python
"""
Factorial
"""

# Find the factorial of a number input by a user. Then print out the factors within the factorial and then print out the actual numeric answer. Hint: The formula for a factorial is n! = (n-1)*n.


# Example output:
"""
8! = 8*7*6*5*4*3*2*1
8! = 40320
"""

user_input = input('Enter a number to find its factorial: ')
```


### P5.PY



```python
"""
Factors
"""

# Find all factors of a number that a user inputs and print out 'The factors of <the_user_input_number> are: '.

user_input = input('Enter a number to find its factors: ')

```


### P6.PY



```python
"""
GCD
"""

# Find the greatest common denominator (GCD) of two number input by a user. Then print out 'The GCD of <first number> and <second number> is <your result>.'

print('Enter two numbers to find their greatest common denominator.')

user_input1 = input('First number: ')
user_input2 = input('Second number: ')
```


## DICT_LOOPS

### P1.PY



```python
"""
Contacts
"""

# You went to a conference and got people to sign up for text updates from your startup. Go through this dict to make the phone numbers readable to a computer. 

# Hint: It can't include any non-numeric
# characters.

contacts = {
	'Jamie': '1.192.168.0143',
	'Kartik': '1.837.209.1121',
	'Grant': '1.826.386.1758',
	'Brandon': '1.935.297.9447',
	'Monique': '1.702.716.5353',
	'Sohom': '1.576.619.6100',
}

```


### P2.PY



```python
"""
Grades
"""
# Here's a dict containing students' grades from the semester's assignments.

students = {
  'Ashton': [86, 45, 98, 100],
  'Sierra': [100, 100, 100, 100],
  'Zach': [38, 49, 90, 87],
  'Manuel': [98, 92, 86, 100],
  'Felicia': [94, 87, 89, 95],
  'Ankur': [75, 77, 77, 85],
  'Ananya': [98, 94, 87, 92],
  'Nick': [79, 84, 89, 90],
  'Olivia': [83, 91, 69, 85],
  'Molly': [83, 74, 72, 90]
}

# p 1.1) Create a dict called num_grades to store each student's average numerical grade for the semester.

# num_grades = 



# p 1.2) Create a dict called letter_grades to store each student's final letter grade for the semester. Use A, B, C, D, and F as grades per the standard grading scale.

# letter_grades = 



# p 1.3) Create a list of honor roll students (i.e. students who got A's).

# honor_roll 
```


### P3.PY



```python
"""
Price Inventory
"""

# Imagine you're the owner of an Italian restaurant. You're evaluating your pricing to make sure it's up to date with the latest costs of making each menu item (see the menu prices and costs dicts below). Evaluate whether each item's price returns a profit margin of at least $1.00. If it doesn't, update the menu_prices dict with a new price that gives the item a $1.00 profit margin. Then print out the items which you've repriced in a new dict called price_increases.

menu_prices = {
	'fettuccine bolognese': 14.99,
	'gnocchi gorgonzola': 10.99,
	'chicken parmigiano': 13.99,
	'butternut squash risotto': 9.99,
	'spaghetti carbonara': 12.99,
	'pizza margherita': 12.99,
	'chicken marsala': 13.99
}

menu_costs = {
	'fettuccine bolognese': 12.50,
	'gnocchi gorgonzola': 11.25,
	'chicken parmigiano': 11.75,
	'butternut squash risotto': 6.33,
	'spaghetti carbonara': 12.90,
	'pizza margherita': 14.00,
	'chicken marsala': 11.75
}

# price_increases = 


```


## CONTROL_FLOW

### P1.PY



```python
"""
Control Flow - I
"""

# Print the numbers in the range (5:12) until you find a factor of 4. If the range the user enters contains no factors of 4, print "There are no factors of 4 in this interval."
# HINT: for the range 5,12 there will likely be multiples of 4 present - to assert the final requirement, try changing range boundaries



```


### P2.PY



```python
"""
Control Flow II
"""

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. Note : Use 'continue' statement. 


```


## SHAPES

### P1.PY



```python
"""
Build a Triangle
"""

# Use a while loop to print a 5-level triangle of stars that looks like this:

"""
*
**
***
****
*****
"""

```


### P2.PY



```python
"""
Build a Pyramid
"""

# Use a while loop to print a pyramid of stars that looks like this:

"""
    *
   ***
  *****
 *******
*********
"""


```


### P3.PY



```python
"""
Build a Diamond
"""

# Use a while loop to print a diamond of stars that looks like this:

"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""

```


## LOOP_CHALLENGES

### P1.PY



```python
"""
Valid Passwords
"""

# Check the validity of password input by users based on the below security requirements: At least 1 letter between [a-z] and 1 letter between [A-Z].
"""
# At least 1 letter between [a-z] and 1 letter between [A-Z].
#At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
"""


# Hint: Look up the documentation for the "re" library and it's ".search()" method.

# p = input("Input your password: ")
```


### P2.PY



```python
"""
Prime Numbers I
"""

# Check if a number input by a user is prime or not. If it is NOT a prime number, print out that it is not a prime number. If it IS a prime number, print out that it is a prime number and give an example of two of its factors. Hint: Prime numbers must be greater than 1.

# Example of output for a NON-prime:
# 12 is not a prime number
# For example, 2 x 6 = 12



# user_input = input("Enter a number to check if it's prime: ")


```

