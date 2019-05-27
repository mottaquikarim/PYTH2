#  DICTS

## DICT_OPS

### P1.PY



```python
"""
Basic Dict Concepts
"""

# 1. Declare an empty dict as d1.



# 2. Create a dict called d2 containing the first and last names below:
# Anthony Paollelo, Ping Qiao, Enrique Alvarez, Arjun Dhir 




# 3. Add Allison Zhang person to d2.



# 4. How many people are now in d2? Print out all their *first* names in the vars below.

### num_people = 

### first_names = 


# 5. Delete a random person from d2 and print his/her name in the var below.

### x = 


# 6. Re-add the name you deleted to the end of d2.





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

# Please use all provided vars for these problems so that the tests work seamlessly!

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


# A user enters the below login info (email and password) for your app. Search your database of 


	# .haskey ? ; if True: print('Successful login!')



current_user = { 'me@email.com': 'myPassword' }
```

