<!---
{"next":"Topics/loops.md","title":"Dicts"}
-->

# Dicts

In addition to lists, another more comprehensive method for storing complex data are **dicts**, or dictionaries. In the example below, we associate a `key` (e.g. 'taq') to a `value` (e.g. 'karim'). The keys and values of a single dict don't have to be homogenous. In other words, you can mix and match different key, value, and key value pair data types within one dict as seen below.

```python
dict1 = {
  'taq': 'karim',
  'apple': 35,
  False: 87.96,
  35: 'dog',
  'tree': True,
  47: 92,
  # etc.
}

print(dict1) # {'taq': 'karim', 'apple': 35, False: 87.96, 35: 'dog', 'tree': True, 47: 92}
```

The `values` in a dict can be any valid Python data type, but there are some restrictions on what you can use as `keys`:

*1. Keys **CAN** be strings, integers, floats, booleans, and tuples.* 
*2. Keys **CANNOT** be lists or dicts.*

Do you see the pattern here so far? The data in a *dict key must be immutable.* Since lists and dicts are mutable, they cannot be used as keys in a dict.

*3. Also, the keys in a dict _**must be unique**_ as well.*

Be careful not to add a key to a dict a second time. If you do, the second item will _**override**_ the first item.

## Creating Dicts

There are several ways you can create your `dict`, but we'll go through the most basic ones here.

#### 1. The simplest is to create an empty list with the `dict()` method.

```python
students = dict() # this creates a new, empty dict
```

#### 2. You can create a dict by passing in key value pairs directly using this syntax:

```python
food_groups = {
	'pomegranate': 'fruit',
	'asparagus': 'vegetable',
	'goat cheese': 'dairy',
	'walnut': 'legume'
}
```

#### 3. You can also convert a *list of tuples* into a dict using `dict()`...

```python
# list of tuples   
listofTuples = [("Hello" , 7), ("hi" , 10), ("there" , 45),("at" , 23),("this" , 77)]

wordFrequency = dict(listofTuples)
print(wordFrequency) # {'this': 77, 'there': 45, 'hi': 10, 'at': 23, 'Hello': 7}
```

#### 4. ...and even combine two lists to create a dict by using the `zip()` method.

The `zip()` method takes the name of each list as parameters - the first list will become the dict's keys, and the second list will become the dict's values. **NOTE!** This only works if you're sure the key value pairs have the same index position in their original lists (so they will match in the dict).

```python
names = ['Taq', 'Zola', 'Valerie', 'Valerie']
scores = [[98, 89, 92, 94], [86, 45, 98, 100], [100, 100, 100, 100], [76, 79, 80, 82]]

grades = dict(zip(names,scores))
print(grades) # {'Taq': [98, 89, 92, 94], 'Zola': [86, 45, 98, 100], 'Valerie': [76, 79, 80, 82]}
```

## Accessing Dict Data

Once you've stored data in your dict, you'll need to be able to get back in and access it! Take a look at this dict holding state capitals.

```python
state_capitals = {
	'NY': 'Albany',
	'NJ': 'Trenton',
	'CT': 'Hartford',
	'MA': 'Boston'
}
```

### Referencing Values by Keys

You *CANNOT* access dict items with index positions like you do with lists! If you try, you'll get a `KeyError` because dict items do not have index positions. **Instead, the dict keys serve the same purpose as indeces in lists.** Accordingly, you can access each value in the list by referencing its key like so:

```python
MAcap = state_capitals['MA']
print('The capital of MA is {}.'.format(MAcap)) # 'The capital of MA is Boston.'
```

Attempting to find a key that does not exist leads to error.

```python
print(state_capitals['PA']) # KeyError from missing key
print(state_capitals[2]) # KeyError from index reference
```

Instead, it's better to look up a key in a dict using `.get(key, [])`. The `.get()` method takes the key argument just as above EXCEPT it allows you to enter some default value it should return if the key you enter does not exist. Usually, we use `[]` as that value.

```python
print(state_capitals.get('PA', []))
# PA is not in our dict, so .get() returns []
```

### Retrieving All Keys, Values, & Key/Value Pairs

Now, this dict has 4 keys, but what if it had *hundreds?* We can  retrieve data from large dicts using `.keys()`, `.values()`, or `.items()`.

```python
pets_owned = {
  'Taq': ['teacup pig','cat','cat'],
  'Francesca': ['llama','horse','dog'],
  'Walter': ['ferret','iguana'],
  'Caleb': ['dog','rabbit','parakeet']
}

a = pets.keys() # ['Taq', 'Francesca', 'Walter', 'Caleb']
print(f'Keys: \n{a} \n\n')

b = pets.values() # [['teacup pig','cat','cat'], ['dog','rabbit','parakeet'], etc ]
print(f'Values: \n{b} \n\n')

c = pets.items() # [('Taq', ['teacup pig','cat','cat']), ('Francesca', [['llama','horse','dog']), etc]
print(f'Key/Value Pairs: \n{c}')
```

## Built-in Operators for Manipulating Dicts

Just like lists, you can edit, analyze, and format your dicts. Some work the same for dicts and lists such as `len()`. However, adding, deleting, and updating data requires a little more detail for dicts than for lists.

### Add or Edit Dict Items

You can add a single item to dict in two ways. The first way is similar to updating a list...

```python
state_capitals = {
	'NY': 'Albany',
	'NJ': 'Trenton',
	'CT': 'Hartford',
	'MA': 'Boston'
}

state_capitals['CA'] = 'Sacramento'

print(state_capitals) # {'NY': 'Albany', 'NJ': 'Trenton', 'CT': 'Hartford', 'MA': 'Boston', 'CA': 'Sacramento'}
```

...but more likely you'll want to use the `.update(key, value)` method.

```python
state_capitals = {
	'NY': 'Albany',
	'NJ': 'Trenton',
	'CT': 'Hartford',
	'MA': 'Boston'
}

state_capitals.update('CA': 'Sacramento')

print(state_capitals) # {'NY': 'Albany', 'NJ': 'Trenton', 'CT': 'Hartford', 'MA': 'Boston', 'CA': 'Sacramento'}
```

The `.update()` method also allows you to make bulk updates. In that case, you can simply pass it a variable containing another dict to add to the first one.

```python
state_capitals = {
	'NY': 'Albany',
	'NJ': 'Trenton',
	'CT': 'Hartford',
	'MA': 'Boston',
	'CA': 'Sacramento'
}
more_states = {
	'WA': 'Olympia',
	'OR': 'Salem',
	'TX': 'Austin',
	'NJ': 'Hoboken',
	'AZ': 'Phoenix',
	'GA': 'Atlanta'
}

state_capitals.update(more_states)

state_capitals = {
	'NY': 'Albany',
	'NJ': 'Hoboken',
	'CT': 'Hartford',
	'MA': 'Boston',
	'CA': 'Sacramento',
	'WA': 'Olympia',
	'OR': 'Salem',
	'TX': 'Austin',
	'AZ': 'Phoenix',
	'GA': 'Atlanta'
}
```

**Notice something?** It's easy to accidentally override items when you're merging datasets. *Oops, we just changed the capital of NJ to Hoboken!* Don't worry though - we'll learn an easy way to check for duplicate keys in the next section on loops.

### Remove Items from a Dict

#### `.clear()` simply empties the dict of all items.

```python
state_capitals = {
	'NY': 'Albany',
	'NJ': 'Hoboken',
	'CT': 'Hartford',
	'MA': 'Boston',
	'CA': 'Sacramento',
	'WA': 'Olympia',
	'OR': 'Salem',
	'TX': 'Austin',
	'AZ': 'Phoenix',
	'GA': 'Atlanta'
}

state_capitals.clear()
print(state_capitals) # {}
```

#### `.pop(key, value)`:

This removes an item, which you must specify by key. There are two things to note here -

1. **First**, you *cannot delete a dict item by specifying a value*. Since values do not have to be unique the way keys are, trying to delete items by referencing values could cause issues.
2. **Second**, just like we saw earlier with `.get(key, value)`, `.pop(key, value)` will raise a `KeyError` if you try to remove a key that does not exist in the dict. We avoid this in the same way, by setting a default value - typically `[]` - for the program to return in case of a missing key.

Unfortunately, you *can't* use the same method as we did for `.update()` to delete larger portions of data. We'll learn a way to do that in the next section on loops as well.

```python
state_capitals = {
	'NY': 'Albany',
	'NJ': 'Hoboken',
	'CT': 'Hartford',
	'MA': 'Boston',
	'CA': 'Sacramento',
	'WA': 'Olympia',
	'OR': 'Salem',
	'TX': 'Austin',
	'AZ': 'Phoenix',
	'GA': 'Atlanta'
}

state_capitals.pop('AZ', [])
# removes 'AZ': 'Phoenix' from our dict
```

#### `popitem()`:
This one just removes an arbitrary key value pair from dict and returns it as a tuple. For instance, you might do this if you're randomly sampling your data for QA purposes.

```python
state_capitals = {
	'NY': 'Albany',
	'NJ': 'Hoboken',
	'CT': 'Hartford',
	'MA': 'Boston',
	'CA': 'Sacramento',
	'WA': 'Olympia',
	'OR': 'Salem',
	'TX': 'Austin',
	'AZ': 'Phoenix',
	'GA': 'Atlanta'
}

seceded1 = state_capitals.popitem()
# ^ removes a random item and returns it as a tuple
print(seceded1) # ('GA': 'Atlanta') for example
```

## Summary

<img src="https://github.com/mottaquikarim/PYTH2/blob/master/assets/Dicts_Summary.png?raw=true" width="100%" align="left"/>


