<!---
{"next":"Topics/dicts.md","title":"Lists"}
-->

# Lists

In order to begin to truly write dynamic programs, we need to be able to work with *dynamic* data where we do not know how much of a certain type of variable we have.

The problem, essentially is, *variables hold only one item*.

```python
my_color = 'red'
my_peer = 'Brandi'
```

**Lists** hold multiple items, called **elements**. List elements can represent any data type, and *a single list can hold any mix of different data types, including **other lists**.*

## Creating lists

To declare a new list varaible, you have two options -- `[]` or `list()`. The `[]` syntax is a bit more straightforward, as seen below.

```python
blank = []
print(f'Blank: {blank}\n')

colors = ['red', 'yellow', 'green']
print(f'Strings: {colors}\n')

grades = [100, 99.5, 65, 54.1, 19]
print(f'Numbers: {grades}\n')

coin_flips = [True, False, True, True]
print(f'Booleans: {coin_flips}\n')

nested_lists = [['circus', 'clown'], ['trapeze', 'artist']]
print(f'Nested Lists: {nested_lists}\n')

mix = [True, ['seal', 'spider monkey'], 22, 'lion', [False, 13]]
print(f'Mixed Data Types: {mix}\n')
```

If you choose to use the `list()` method, there are a couple things to remember. First, you can only add **one** parameter into `list()`. So if you want to add multiple items, you have to pass them to `list()` within the `[]` syntax anyway.

```python
blank = list() # blank list
print(blank)

colors = list(['red', 'yellow', 'green']) # strings
print(colors)

# etc...

mix = list([True, ['seal', 'spider monkey'], 22, 'lion', [False, 13]])
print(f'Mixed Data Types: {mix}\n')
```

Take a look at what happens if you don't pass your desired item or items using the `[]` for list syntax.

```python
colors = list('red', 'yellow', 'green')
print(colors)
### TypeError: list() takes at most 1 argument (3 given)

grades = list(100) # or any float e.g. 100.0
print(grades)
### TypeError: 'int' object is not iterable

coin_flips = list(True) # booleans
print(coin_flips)
### TypeError: 'bool' object is not iterable
```

The one use case that does not throw an error is if you pass a single string value. Still, this doesn't have the intended output of adding a single names to a list of names!

```python
names = list('Julianna')
print(names)
# ['J', 'u', 'l', 'i', 'a', 'n', 'n', 'a']
```

And if you think it works for sentences by parsing a new list element at each space character...*nope!*

```python
sentence = list('I like to sing!')
print(sentence)
# ['I', ' ', 'l', 'i', 'k', 'e', ' ', 't', 'o', ' ', 's', 'i', 'n', 'g', '!']
```

## Accessing Elements in the List

The **list index** means the location of something (an *element*) in the list.

List indexes start counting at 0!

|  List | "Brandi" | "Zoe" | "Steve" | "Aleksander" | "Dasha" |
|:-----:|:--------:|:-----:|:-------:|:------:|:------:|
| Index |     0    |   1   |    2    |    3   |    4   |


```python
"""list_name[index]"""

my_class = ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha']
print(my_class[0]) # Prints "Brandi"
print(my_class[1]) # Prints "Zoe"
print(my_class[4]) # Prints "Dasha"
```

To select multiple items from a list, simply pass the range of indeces which hold the desired elements, e.g. `[2:7]`.

**NOTE!** It's important to remember that the upper bound is NOT inclusive. If you want the elements and index 1 through at including index 4, you have to write `[2:5]`. See this in action below:

```python
"""list_name[start_index:end_index_+1]"""

my_class = ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha']
print(my_class[1:4])
```

Here are a few examples that illustrate what happens when you don't specify a bound:

```python
my_class = ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha']

my_class = ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha']

print('[:2] -- ', my_class[:2]) # All indeces up to, but NOT including index 2

print('[2:] -- ', my_class[2:]) # Index 2 through end of list

print('[:] -- ', my_class[:]) # Prints WHOLE LIST

print('[1:1] -- ', my_class[1:1]) # Prints NOTHING
```

If you have nested lists, you simply add another level of index selection, like so:

```python
nested_lists = list([['circus', 'clown'], ['trapeze', 'artist']])
print(nested_lists[0][0]) # circus
```

#### Practice together!

```python
pets = ['dog', 'cat', 'guinea pig', 'ferret', 'bird', 'lizard']

# Print index 1:


# Print ['guinea pig', 'ferret']:


# Print the 5th element:


# Print all elements up to and INCLUDING 'ferret':


# Print 'dog':


# Print all elements from 'ferret' onwards:


```



## Built-In Operations for Manipulating Lists

### Add Items to a List
If you want to extend the content of a single list, you can use `.append()`, `.extend()` `.insert()` to add elements of any data type.

#### `.append()` vs. `.extend()`
These methods both add items to the end of the list. The difference here is that `.append()` will add whatever value or group of values you pass it *in one chunk*. In contrast, if you pass a group of values into `.extend()`, it will add each element of the group *individually*. Here are a few examples to show you the difference in outcomes.

```python
""" Passing direct argument """
# Append..
x = ['a', 'b', 'c', 'd']
x.append(['e', 'f', 'g'])
print(x)
# ['a', 'b', 'c', 'd', ['e', 'f', 'g']]

# ... vs. extend
x = ['a', 'b', 'c', 'd']
x.extend(['e', 'f', 'g'])
print(x)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
```

Notice in this next example how `.extend()` only considers individual values of the parent list. It still adds the tuple and list - `('f', 'g')` and `['h', 'i']` - to our list `x` as their own items.

```python
""" Passing argument within a var"""
# Append..
x = ['a', 'b', 'c', 'd']
y = ['e', ('f', 'g'), ['h', 'i'], 'j']
x.append(y)
print(y)
# ['a', 'b', 'c', 'd', ['e', ('f', 'g'), ['h', 'i'], 'j']]

# ... vs. extend
x = ['a', 'b', 'c', 'd']
y = ['e', ('f', 'g'), ['h', 'i'], 'j']
x.extend(y)
print(x)
# ['a', 'b', 'c', 'd', 'e', ('f', 'g'), ['h', 'i'], 'j']
```

#### `.insert(index, value)`
If you want to add an item to a specific point in your list, you can pass the desired index and value into `.insert()` as follows.

```python
"""your_list.insert(index, item)"""

my_class = ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha', 'Sonyl']
my_class.insert(1, 'Sanju')
print(my_class)
# ['Brandi', 'Sanju', 'Zoe', 'Steve', 'Aleksander', 'Dasha', 'Sonyl']
```

### Remove Items from a List
Likewise, you can use `.pop()` or `.pop(index)` to remove any type of element from a list.

#### `.pop()`
- Removes an item from the end of the list.

```python
"""your_list.pop()"""

my_class = ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha', 'Sonyl']
student_that_left = my_class.pop()
print("The student", student_that_left, "has left the class.")
# Sonyl
print(my_class)
# ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha']
```

#### `.pop(index)`

- Removes an item from the list.
- Can take an index.

```python
"""your_list.pop(index)"""

my_class = ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha']
student_that_left = my_class.pop(2) # Remember to count from 0!
print('The student', student_that_left, 'has left the class.')
# 'Steve'
print(my_class)
# => ['Brandi', 'Zoe', 'Aleksander', 'Dasha']
```

### Edit Items in a List

#### Update/Replace Items

To replace items in a list, you reference them by their index value and simply declare a new value for that element.

```python
x = ['Brandi', 'Sanju', 'Zoe', 'Steve', 'Aleksander', 'Dasha', 'Sonyl']

x[1] = 'Raju'
x[4:] = ['Chloe', 'Phoebe']
print(x)
```

#### Join Items

If you need to, you can compile your list items into a single string using `.join()`. You CANNOT do this with lists of numbers, booleans, or a list containing a mix of strings and other data types though.

```python
letters = ['j', 'u', 'l', 'i', 'a', 'n', 'n', 'a']
name = ''.join(letters)
print(name) # 'julianna'

words = ['this', 'is', 'fun']
sentence = ' '.join(words)
print(f'{sentence}.') # 'this is fun.'
```

#### Split Items

Conversely, you can separate a string using `.split('by_char')`, which will parse values out of a string and turn each value into a list item. This one doesn't work for single words you might want to split into individual characters. That said, you *can* specify what character should convey to the method when to split out a new item. By default, `.split('by_char')` will use a space character to split the string.

```python
x = 'this is fun'
sentence = x.split() # note - using default split char at space
print(sentence) # ['this', 'is', 'fun']

y = 'Sandra,hi@email.com,646-212-1234,8 Cherry Lane,Splitsville,FL,58028'
data = y.split(',')
print(data) # ['Sandra', 'hi@email.com', '646-212-1234', '8 Cherry Lane', 'Splitsville', 'FL', '58028']
```

## Built-in Operators for Analyzing Lists

Python has some built-in operations that allow you to analyze the content of a list. Some basic ones include:

#### `len()`

This counts the numbers of elements in the list, or its *length*, regardless of data type.

```python
# length_variable = len(your_list)

my_class = ['Brandi', 'Zoe', 'Aleksander', 'Dasha']
num_students = len(my_class)
print(f'There are {num_students} students in the class')
# => 5
```

Aside from merely finding the length, `len()` comes in handy during a number of other use cases. For example, you can use `len()` to dynamically select the last element of a list. If you find the list's length then subtract 1, you will have the index of the last list element. Watch this:

```python
my_class = ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha']
num_students = len(my_class)
last_student_index = num_students - 1
print(my_class[last_student_index]) # Dasha

# You can do this all in one line if you want!
# print(my_class[(len(my_class)-1)])
```

Here it is with a nested list:

```python
nested_lists = [['circus', 'clown'], ['trapeze', 'artist']]
last_index_nested_lists = len(nested_lists) - 1
print(last_index_nested_lists)

last_index_last_nested_list = len(nested_lists[last_index_nested_lists]) - 1
print(last_index_last_nested_list)

last_element_last_nested_list = nested_lists[last_index_nested_lists][last_index_last_nested_list]

print(last_element_last_nested_list) # artist
```

#### `sum()`

This returns the sum of all items in *numerical lists*.

```python
"""sum_variable = sum(your_numeric_list)"""

team_batting_avgs = [.328, .299, .208, .301, .275, .226, .253, .232, .287]
sum_avgs = sum(team_batting_avgs)
print(f'The total of all the batting averages is {sum_avgs}.')
```

#### `min()` & `max()`

Return the smallest or largest number *in a numerical list*.

```python
"""
max(your_numeric_list)
min(your_numeric_list)
"""

team_batting_avgs = [.328, .299, .208, .301, .275, .226, .253, .232, .287]
print(f'The highest batting average is {max(team_batting_avgs}')
# ... 0.328
print(f'The lowest batting average is {min(team_batting_avgs)}')
# ... 0.208
```

#### `.index()`

Given a list element's value, return its index.

```python
sentence = ['a', 'purple', 'pig', 'and', 'a', 'green', 'donkey', 'flew', 'a', 'kite', 'in', 'the', 'middle','of', 'the', 'night', 'and', 'ended', 'up', 'sunburnt']

pig_index = sentence.index('pig')
print(pig_index)
```

If the element occurs multiple times in the list, `.index()` will only return the index of its *first* occurrence!

```
sentence = ['a', 'purple', 'pig', 'AND', 'a', 'green', 'donkey', 'flew', 'a', 'kite', 'in', 'the', 'middle','of', 'the', 'night', 'AND', 'ended', 'up', 'sunburnt']

and_index = sentence.index('AND')
print(and_index) # 3
```

#### `.count()`

This returns the number of occurrences of a *single, distinct element* within a list. That means for example, if you're searching a list of words (i.e. strings) for the occurrences of a single letter, only instances where that single letter appears as its own list item will be counted.

```python
nums = [84, 8, 18, 8, 28, 6, 10, 8, 78, 9]
print(nums.count(8)) # 3


sentence = ['a', 'purple', 'pig', 'and', 'a', 'green', 'donkey', 'flew', 'a', 'kite', 'in', 'the', 'middle','of', 'the', 'night', 'and', 'ended', 'up', 'sunburnt']
print(sentence.count('a')) # 3
```

If you want to count the occurrences of a single character within a larger value, you can still use `.count()`...

```python
word = 'sunburnt'
print(word.count('u')) # 2
```

*...BUT only on **strings**.* Notice how `.count()` throws an error if you try to count the number of times the digit "2" appears in the number below. And remember, you CANNOT use the `.split()` method as a workaround because `.split()` only works on strings!

```python
num = 22384232348
print(num.count(2))
```

#### Practice Together!

Now, take a look at how these list operations work together in this contextual example. Let's say we're conducting a probability experiment with coin tosses. We conduct some number of trials (i.e. the coin tosses) and record the outcomes. Based on the sample below, here's one way to find the probabilities of a "Heads" or "Tails" outcome.

```python
coin_toss = [True, False, False, False, True, False, True, True, False, False, True, True, False, True]

num_tosses = len(coin_toss)

heads = coin_toss.count(True)
tails = coin_toss.count(False)
print(f'# Heads: {heads} vs. # Tails: {tails}\n')

P_heads = heads / num_tosses
P_tails = tails / num_tosses

print(f'P(Heads) = {P_heads} vs. P(Tails) = {P_tails}')
```

## Sorting Lists

If you want to organize your lists better, you can sort them with the `.sort()` or `sorted()` functions. You can sort:

* Numbers: ascending and descending order
* Strings: alphabetically and reverse alphabetically
* You **cannot** sort a list that includes different data types. 

It's important to remember that the `.sort()` function modifies the list *in place*, while the `sorted()` function requires you to assign its result back to the variable.

#### `.sort()`

The first two examples below illustrate how to sort lists in ascending order/alphabetically using `.sort()`.

```python
numbers = [1, 3, 7, 5, 2, 4, 6]
numbers.sort()
print(numbers) # [1, 2, 3, 4, 5, 6, 7]


letters = ['b', 'e', 'c', 'a', 'd']
letters.sort()
print(letters) # ['a', 'b', 'c', 'd', 'e']
```

To do this in descending order, simply add `reverse=True` as an argument in `.sort()` like this:

```python
numbers = [1, 3, 7, 5, 2, 4, 6]
numbers.sort(reverse = True)
print(numbers) # [7, 6, 5, 4, 3, 2, 1]

letters = ['b', 'e', 'c', 'a', 'd']
letters.sort(reverse = True)
print(letters) # ['e', 'd', 'c', 'b', 'a']
```

#### `sorted()`

The first two examples below illustrate how to sort lists in **ascending order**/alphabetically using `sorted()`.

```python
numbers = [1, 3, 7, 5, 2, 4, 6]
ascending = sorted(numbers)
print(ascending) # [1, 2, 3, 4, 5, 6, 7]


letters = ['b', 'e', 'c', 'a', 'd']
ascending = sorted(letters)
print(ascending) # ['a', 'b', 'c', 'd', 'e']
```

To do this in **descending order**, simply add `reverse=True` as an argument in `.sorted()` like this:

```python
numbers = [1, 3, 7, 5, 2, 4, 6]
descending = sorted(numbers, reverse=True)
print(descending) # [7, 6, 5, 4, 3, 2, 1]


letters = ['b', 'e', 'c', 'a', 'd']
descending = sorted(letters, reverse=True)
print(descending) # ['e', 'd', 'c', 'b', 'a']
```

## Tuples

Tuples are a special subset of lists - they are *immutable* - in that they cannot be changed after creation. Tuples are denoted with `()` as opposed to `[]`.

You can declare sets in two ways:

```python
score1 = ('Taq', 100)
print(score1) # ('Taq', 100)

# OR

score2 = 'Sue', 101 # ('Sue', 101)
print(score2)
```

We read tuples just like we would read a list:

```python
dna = ('A', 'T'), ('G', 'C')
print(dna) # (('A', 'T'), ('G', 'C'))


print(dna[0]) # ('A', 'T')
print(dna[1][0]) # G
```

You can do SOME of the same operations on tuples despite their immutability. For example:

```python
tuple1 = (1, 3, 7, 5, 2, 4, 6)

len_tuple1 = len(tuple1) # 7
sum_tuple1 = sum(tuple1) # 28
min_tuple1 = min(tuple1) # 1
max_tuple1 = max(tuple1) # 7

count_val4 = tuple1.count(4) # 1
index_val2 = tuple1.index(2) # 4

print(f'''
Length: {len_tuple1}
Sum: {sum_tuple1}
Min: {min_tuple1}
Max: {max_tuple1}
Occurrences of "4": {count_val4}
Index of "2": {index_val2}
''')
```

You *can sort, join, or split* a tuple the same as a list, **BUT** because you can't edit a tuple:
* You can't use `.sort()` because that edits the object in place
* Each of these will return a *new list object*

```python
tuple2 = ('b', 'e', 'c', 'a', 'd')

sort_asc = sorted(tuple2)
print(sort_asc, type(sort_asc)) # ['a', 'b', 'c', 'd', 'e'] <class 'list'>

sort_desc = sorted(tuple2, reverse = True)
print(sort_desc, type(sort_desc)) # ['e', 'd', 'c', 'b', 'a'] <class 'list'>

print('\n')

joined = ', '.join(tuple2) # Joined: b, e, c, a, d <class 'str'>
print('Joined:', joined, type(joined))

split_up = joined.split(',') # Split: ['b', ' e', ' c', ' a', ' d'] <class 'list'>
print('Split:', split_up, type(split_up))
```

## Sets

Sets are special lists in that they can only have **unique** elements. They are denoted with `{}`.

```python
set_1 = {1,2,3,4,5} # this is a set, notice the {}
set_2 = {1,1,1,2,2,3,4,5,5,5} # this is still a set
print(set_2) # {1,2,3,4,5}

print(set_1 == set_2) # True
```

Sets are also not indexed, so you cannot access, say, the 3rd element in a set. Instead, you can use *boolean membership operators* to check for a value's existence in the set. Remember those?

```python
set_1 = {1,2,3,4,5}

print(2 in set_1) # True
print(8 in set_1) # False

print(2 and 8 in set_1) # False
print(2 and 3 in set_1) # True
```

That said, you can still perform mathmetical operations on sets. These are the same examples we used for tuples, and they have the same results. Notice how you can't find the index of an element for the reasons we just discussed!

```python
set1 = (1, 3, 7, 5, 2, 4, 6)

len_set1 = len(set1) # 7
sum_set1 = sum(set1) # 28
min_set1 = min(set1) # 1
max_set1 = max(set1) # 7

count_val4 = set1.count(4) # 1

print(f'''
Length: {len_set1}
Sum: {sum_set1}
Min: {min_set1}
Max: {max_set1}
Occurrences of "4": {count_val4}
''')
```

You *can also sort, join, or split* a set, **BUT** you have the same limitations as you do with a tuple:
* You can't use `.sort()` because that edits the object in place
* Each of these will return a *new list object*

```python
set2 = {'b', 'e', 'c', 'a', 'd'}

sort_asc = sorted(set2)
print(sort_asc, type(sort_asc)) # ['a', 'b', 'c', 'd', 'e'] <class 'list'>

sort_desc = sorted(set2, reverse = True)
print(sort_desc, type(sort_desc)) # ['e', 'd', 'c', 'b', 'a'] <class 'list'>

print('\n')

joined = ', '.join(set2) # Joined: b, e, c, a, d <class 'str'>
print('Joined:', joined, type(joined))

split_up = joined.split(',') # Split: ['b', ' e', ' c', ' a', ' d'] <class 'list'>
print('Split:', split_up, type(split_up))
```

**Pro Tip**: Sets give a great way to remove duplicates from a list!

```python
my_list = [1,2,4,5,2,3,1,4,5,1,5,3]

uniques_in_my_list = set(my_list)
print(uniques_in_my_list) # {1, 2, 3, 4, 5}

my_list = list(uniques_in_my_list)
print(my_list) # [1, 2, 3, 4, 5]
```

Here's a **[helpful list](https://snakify.org/en/lessons/sets/#section_4)** of other set operations.

## Summary

<img src="https://github.com/mottaquikarim/PYTH2/blob/master/assets/Lists_Summary.png?raw=true" width="100%" align="left"/>

### Class Practice PSETs

[Lists](https://github.com/mottaquikarim/PYTH2/blob/master/src/PSETS/nb/lists_inclass_psets.ipynb)


## Additional Resources

- [Python Lists - Khan Academy Video](https://www.youtube.com/watch?v=zEyEC34MY1A)
- [Google For Education: Python Lists](https://developers.google.com/edu/python/lists)
- [Python-Lists](https://www.tutorialspoint.com/python/python_lists.htm)
- [Python List Methods](https://www.programiz.com/python-programming/methods/list/)
- [Python Data Structures: Lists, Tuples, Sets, and Dictionaries Video](https://www.youtube.com/watch?v=R-HLU9Fl5ug)
