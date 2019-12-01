#  DICTS

## DICT_BASICS

### P1.PY



```python
"""
Intro to Dict Concepts
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
Predators & Prey
"""

# A) Create a dict called "pred_prey", containing:
### 3 carnivorous marine animals
### For each carnivore, 3 examples of its prey

pred_prey = None



# B) Print out the 2nd predator and its prey in this format:
#### predator2: prey1, prey2, & prey3




# C) Print a unique collection of all the prey in a variable called "prey".

prey = None
```


### P3.PY



```python
"""
Merging Dicts
"""

# Merge these two dicts without creating a new one.

d1 = {'a': 100, 'b': 200}
d2 = {'c': 300, 'd': 400, 'e': 500}


```


### P4.PY



```python
"""
Lists to Dicts
"""

# Turn these two lists into a dict called grades.

names = ['Taq', 'Zola', 'Valerie', 'Valerie']
scores = [[98, 89, 92, 94], [86, 45, 98, 100], [100, 100, 100, 100], [76, 79, 80, 82]]

### grades = 
```


## DICT_MANIP_OPS

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

