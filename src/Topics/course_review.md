<!---
{"next": "Topics/project_ideas.md","title": "Course Review"}
-->

# Course Review
## Data Structures

### Lists

```python
colors = ['red', 'yellow', 'green'] #strings
grades = [100, 99, 65, 54, 19] #numbers
bools = [True, False, True, True] #booleans
```

```python
grades = [100, 99, 65, 54, 19]
grades[0] # 100
len(grades) # 5
sum(grades) # 337

ascending = sorted(grades) # [19, 54, 65, 99, 100]
descending = sorted(grades, reverse=True) # [100, 99, 65, 54, 19]
```

```python
# UPDATE
my_class = ['Brandi', 'Zoe', 'Steve', 'Dayton', 'Dasha', 'Sonyl']
my_class[3] = "Aleksander"
# changes in place to ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha', 'Sonyl']

# REMOVE
student_that_left = my_class.pop() # Sonyl
	# or
student_that_left = my_class.pop(3) # Steve
print(my_class) # ['Brandi', 'Zoe', 'Aleksander', 'Dasha']


# ADD
new_students = ["Raju", "Chloe"]
my_class.extend(new_students)
# changes in places to ['Brandi', 'Zoe', 'Aleksander', 'Dasha', 'Raju', 'Chloe']

my_class.insert(1, "Phoebe")
# changes in places to ['Brandi', 'Zoe', 'Aleksander', 'Dasha', 'Raju', 'Chloe']
```

```python
# JOIN
words = ['this', 'is', 'fun']
sentence = ' '.join(words)
print(sentence) # 'this is fun'

words = ['this', 'is', 'fun']
sentence = ' '.join(words)
print(f'{sentence}.') # 'this is fun.'

# SPLIT
person = 'Sandra,hi@email.com,646-212-1234,8 Cherry Lane,Splitsville,FL,58028'
contact_info = person.split(',')
print(data) # ['Sandra', 'hi@email.com', '646-212-1234', '8 Cherry Lane', 'Splitsville', 'FL', '58028']
```

### Dicts

Creating Dicts:

```python
names = ['Taq', 'Zola', 'Valerie', 'Valerie']
scores = [[98, 89, 92, 94], [86, 45, 98, 100], [100, 100, 100, 100], [76, 79, 80, 82]]

grades = dict(zip(names,scores))
print(grades) # {'Taq': [98, 89, 92, 94], 'Zola': [86, 45, 98, 100], 'Valerie': [76, 79, 80, 82]}
```

Accessing Dict Data:

```python
state_capitals = {
	'NY': 'Albany',
	'NJ': 'Trenton',
	'CT': 'Hartford',
	'MA': 'Boston',
	'CA': 'Sacramento'
}

MAcap = state_capitals['MA'] # Boston
print(state_capitals.get('PA', []))
# PA is not in our dict, so .get() returns []

state_capitals.keys()
# dict_keys(['NY', 'NJ', 'CT', 'MA'])

state_capitals.values()
# dict_values(['Albany', 'Trenton', 'Hartford', 'Boston'])

state_capitals.items()
# dict_items([('NY', 'Albany'), ('NJ', 'Trenton'), ('CT', 'Hartford'), ('MA', 'Boston')])
```

```python
more_states = {
	'WA': 'Olympia',
	'OR': 'Salem',
	'AZ': 'Phoenix',
	'GA': 'Atlanta'
}

# Add or update group of key/value pairs
state_capitals.update(more_states)

# Remove item by key
state_capitals.pop('AZ', [])
```

## Control Flow

### Conditionals

```python
speed_limit = 65
my_speed = 32

my_speed < speed_limit # True
my_speed > speed_limit # False
my_speed <= speed_limit # True
my_speed >= speed_limit # False
(speed_limit == my_speed) # False
(speed_limit != my_speed) # True
```

```python
if temp < 65 and is_it_raining:
	print('wear a raincoat and bring an umbrella!')
elif temp > 65 and is_it_raining:
	print('bring an umbrella!')
elif temp < 65:
	print('wear a jacket!')
else:
	print('the weather is beautiful!')

temp = 41
is_it_raining = True
# wear a raincoat and bring an umbrella!

temp = 73
is_it_raining = True
# bring an umbrella!

temp = 56
is_it_raining = False
# wear a jacket!

temp = 80
is_it_raining = False
# the weather is beautiful!
```

### Loops

While Loops:

```python
s = ''
n = 5

while n > 0:
    n -= 1
    if (n % 2) == 0:
        continue

    a = ['foo', 'bar', 'baz']
    while a:
        s += str(n) + a.pop(0)
        if len(a) < 2:
            break

print(s) # '3foo3bar1foo1bar'

###############################

a = ['foo', 'bar', 'baz', 'qux', 'corge']
while a:
    if len(a) < 3:
        break
    print(a.pop())
print('Done.')

## This loop will output...
"""
corge
qux
baz
Done.
"""
```

For Loops: 

```python
transaction = {
  "amount": 10.00,
  "payee": "Joe Bloggs",
  "account": 1234
}

for key, value in transaction.items():
    print("{}: {}".format(key, value))

# Output:
account: 1234
payee: Joe Bloggs
amount: 10.0

###############################

# else DOES execute
for i in ['foo', 'bar', 'baz', 'qux']:
  print(i)
else:
  print('Done.') # foo, bar, baz, qux, Done.

# else DOES NOT execute
for i in ['foo', 'bar', 'baz', 'qux']:
  if i == 'bar':
    break
  print(i)
else:
  print('Done.') # foo
```

Infinite Loops (Yikes!)

```python
# Infinite Loop
a = ['foo', 'bar', 'baz', 'qux', 'corge']
while a:
    if len(a) < 3:
        continue
    print(a.pop())
print('Done.')

# Fixing the Infinite Loop
while a:
    if len(a) < 3:
        break
    print(a.pop())
print('Done.', a) # Done. ['foo', 'bar']
```

## OOP (Object-Oriented Programming)

### Functions

```python
def function_name(parameters):
	"""docstring"""
	# statement(s)

def num_squared(num):
	"""Find the square of some number passed in"""
	square = num*num # code to find the square
	return square

sq12 = num_squared(12)
print(sq12) # 144
```

### Classes

Parent class:

```python
class Animal:
    def __init__(self, species = '', diet= ''):
        self.species = species
        self.diet = diet

    kingdom = 'Animalia'

    def my_kingdom(self):
        print(self.kingdom)

    def feed_me(self):
        if self.diet == 'omnivore':
            food = 'plants and meat'
        elif self.diet == 'carnivore':
            food = 'meat'
        elif self.diet == 'herbivore':
            food = 'plants'
        print(f'{self.species} eat {food}!')
        return None
```

Child class w. inheritance:

```python
class Elephant(Animal):
    def __init__(self, name, genus = '', species = '', habitat = '', age = None):
        self.name = name
        self.genus = genus
        self.species = species
        self.habitat = habitat
        self.age = age
        self.taxonomy = {'Kingdom': Animal.kingdom, 'Class': self.common_taxonomy['Class'], 'Family': self.common_taxonomy['Family'], 'Genus': self.genus, 'Species': self.species} # C.

    diet = 'Herbivore'

    common_taxonomy = {
    'Class': 'Mammalia',
    'Family': 'Elephantidae',
    }

    def summary(self):
      print(f'All about {self.name} -')
      print(f'Elephant, age {self.age}\nHabitat: {self.habitat}\nDiet: {self.diet}\n\nTaxonomy:')
      for k,v in self.taxonomy.items():
        print(f'{k}: {v}')
```

## Data Science Strategy

*More coming soon...*

## Pandas

### Basic Objects: ndarrays, Series & DataFrames

### Data Vizualization


