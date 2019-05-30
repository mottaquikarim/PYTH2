#  LISTS

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


#  DICTS

## DICT_OPS

### P1.PY



```python
"""
Basic Dict Concepts
"""

# A) Declare an empty dict as d1.



# B) Create a dict called d2 containing the first and last names below:
# Anthony Paollelo, Ping Qiao, Enrique Alvarez, Arjun Dhir 




# C) Add Allison Zhang person to d2.



# D) How many people are now in d2? Print out all their *first* names in the vars below.

### num_people = 

### first_names = 


# E) Delete a random person from d2 and print his/her name in the var below.

### x = 


# F) Re-add the name you deleted to the end of d2.





```


### P2.PY



```python
"""
Merging Dicts
"""

# Merge these two dicts without creating a new one.

d1 = {'a': 100, 'b': 200}
d2 = {'c': 300, 'd': 400, 'e': 500}


```


### P3.PY



```python
"""
Math with Girl Scout Cookies
"""

# Print out the number of boxes of girl scout cookies that each girl in the troop sold in the below format:
	# Wendy: _____
	# Connie: _____
	# Francesca: _____

Wendy = {'tagalongs': 5, 'thin mints': 12, 'samoas': 8}
Connie = {'tagalongs': 10, 'thin mints': 4, 'samoas': 12}
Francesca = {'tagalongs': 18, 'thin mints': 14, 'samoas': 10}

### salesW = 
### salesC = 
### salesF = 


# For each type of girl scout cookie, print out the total number of boxes sold in the below format:
	# tagalongs: _____
	# thin mints: _____
	# samoas: _____

### total_tagalongs = 
### total_thinmints = 
### total_samoas = 


# For each type of girl scout cookie, print out the average number of boxes sold in the below format:
	# tagalongs: _____
	# thin mints: _____
	# samoas: _____

### avg_tagalongs = 
### avg_thinmints = 
### avg_samoas = 

# Print out total the number of boxes of cookies the girls sold collectively as follows:
	# "This year we sold ______ boxes!"

### boxes_sold = 
```


### P4.PY



```python
"""
Inverting Keys & Values
"""

# Invert dict1 - make the current keys into values and the current values into keys.


dict1 = { "k1" : "v1", "k2" : "v2", "k3" : "v1" }


```


### P5.PY



```python
"""
Lists to Dicts
"""

# Turn these two lists into a dict called grades.

names = ['Taq', 'Zola', 'Valerie', 'Valerie']
scores = [[98, 89, 92, 94], [86, 45, 98, 100], [100, 100, 100, 100], [76, 79, 80, 82]]

### grades = 
```


## SEARCH_VALIDATION

### P1.PY



```python
"""
Basic Login
"""

# Imagine you work for a movie streaming service. You're in charge of safeguarding user privacy by ensuring the login feature remains secure. For the sake of example only, below is the dict of user login info. Normally, you wouldn't have access to see this unencrypted of course!

users = {
	'person@email.com': 'PassWord',
	'someone@email.com': 'hiitsme',
	'me@email.com': 'myPassword',
	'anyone@email.com': 'IMawesome',
	'guy@email.com': 'pa$$wordz'
	# etc
}


# A user enters the below login info (email and password) for your app. Search your database of user logins to see if this account exists and if the password matches what you have on file. If the login credentials are correct, print "Successful login!". Otherwise, print "The login info you entered does not match any of our records."

current_user = { 'me@email.com': 'myPassword' }
```


## COUNTERS_CHALLENGE

### P1.PY



```python
"""
Word Frequency
"""

# Print out the number of words in this movie quote. Find and print out the most common word in the quote and how many times it was used.
### Hint: You do not need a loop for this. Look up the Counter docs in python3.

from collections import Counter

princess_bride = [
'Hello', 'my', 'name', 'is', 'Inigo', 'Montoya',
'You', 'killed', 'my', 'father',
'Prepare', 'to', 'die'
]

### fave_word = 

# p.s. You might use this to help analyze the most common topic in comments or reviews from your users to help understand the best places to improve you product.
```


### P2.PY



```python
"""
Summing Dict Values
"""

# Two Kindergarten teachers poll their classes for what fruit they want to eat for snacktime tomorrow. Only one of them is going shopping, so she needs to know how many of each fruit she needs to buy in total. Tally these up and assign them to the "shopping_list" dict.

poll1 = {'apples': 8, 'bananas': 12}
poll2 = {'apples': 6, 'bananas': 6, 'clementines': 8}

### shopping_list = 


```

