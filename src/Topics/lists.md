<!---
{"next":"Topics/dicts.md","title":"Lists"}
-->

# Lists

In order to begin to truly write dynamic programs, we need to be able to work with *dynamic* data where we do not know how much of a certain type of variable we have.

The problem, essentially is, **variables hold only one item**.

```python
my_color = "red"
my_peer = "Brandi"
```
Lists hold multiple items - and lists can hold any datatype.

## Creating lists

Here are some different ways to declare a list variable:

```python
colors = ['red', 'yellow', 'green'] #strings
grades = [100, 99, 65, 54, 19] #numbers
bools = [True, False, True, True] #booleans
```

To create a new **blank** list, simply use ```python blank_list = list()```.

## Accessing Elements in the List

The **list index** means the location of something (an *element*) in the list.

List indexes start counting at 0!

|  List | "Brandi" | "Zoe" | "Steve" | "Aleksander" | "Dasha" |
|:-----:|:--------:|:-----:|:-------:|:------:|:------:|
| Index |     0    |   1   |    2    |    3   |    4   |

```python
my_class = ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha']
print(my_class[0]) # Prints "Brandi"
print(my_class[1]) # Prints "Zoe"
print(my_class[4]) # Prints "Dasha"
```

## Built-In Operations for Manipulating Lists

#### Add or Edit Items to a List
If you want to extend the content of a single list, you can use `.append()`, `.extend()` `.insert()` to add elements of any data type.

`.append()` & `.extend()`:
These methods both add items to the end of the list. The difference here is that `.append()` will add whatever value or group of values you pass it *in one chunk*. In contrast, if you pass a group of values into `.extend()`, it will add each element of the group *individually*. Here are a few examples to show you the difference in outcomes.

```python
# passing direct argument
x = ['a', 'b', 'c', 'd']
x.append(['e', 'f', 'g'])
print(x) # ['a', 'b', 'c', 'd', ['e', 'f', 'g']]

x = ['a', 'b', 'c', 'd']
x.extend(['e', 'f', 'g'])
print(x) # ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# passing argument within a var
x = ['a', 'b', 'c', 'd']
y = ['e', ('f', 'g'), ['h', 'i'], 'j']
x.append(y)
print(y) # ['a', 'b', 'c', 'd', ['e', ('f', 'g'), ['h', 'i'], 'j']]

x = ['a', 'b', 'c', 'd']
y = ['e', ('f', 'g'), ['h', 'i'], 'j']
x.extend(y)
print(x) # ['a', 'b', 'c', 'd', 'e', ('f', 'g'), ['h', 'i'], 'j']
```

Notice that `.extend()` only considers individual values of the parent list. It still added the tuple and list - `('f', 'g')` and `['h', 'i']` - to our list `x` as their own items.

`.insert(index, value)`:
If you want to add an item to a specific point in your list, you can pass the desired index and value into `.insert()` as follows.

```python
# your_list.insert(index, item)

my_class = ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha', 'Sonyl']
my_class.insert(1, 'Sanju')
print(my_class)
# => ['Brandi', 'Sanju', 'Zoe', 'Steve', 'Aleksander', 'Dasha', 'Sonyl']
```

`l[index:index]=`:
To *replace* items in a list by their index position, you can use the same syntax for adding a single new value. You simply reference which indeces you want to replace and specify the new values.

```python
x = ['Brandi', 'Sanju', 'Zoe', 'Steve', 'Aleksander', 'Dasha', 'Sonyl']
x[1] = 'Raju'
x[6:] = ['Chloe', 'Phoebe']
print(x) # ['Brandi', 'Raju', 'Zoe', 'Steve', 'Aleksander', 'Dasha', 'Chloe', 'Phoebe']
```

`.join()`:
If you need to, you can compile your list items into a single string.

```python
letters = ['j', 'u', 'l', 'i', 'a', 'n', 'n', 'a']
name = ''.join(letters)
print(name) # 'julianna'

words = ['this', 'is', 'fun']
sentence = ' '.join(words)
print(f'{sentence}.') # 'this is fun.'
```

`.split('by_char')`:
You can also do the opposite - split values out of a string and turn each value into a list item. This one doesn't work for single words you might want to split into individual characters. That said, you *can* specify what character should convey to the method when to split out a new item. By default, `.split()` will use a space character to split the string.

```python
x = 'this is fun'
sentence = x.split() # note - using default split char at space
print(sentence) # ['this', 'is', 'fun']

y = 'Sandra,hi@email.com,646-212-1234,8 Cherry Lane,Splitsville,FL,58028'
data = y.split(',')
print(data) # ['Sandra', 'hi@email.com', '646-212-1234', '8 Cherry Lane', 'Splitsville', 'FL', '58028']
```

#### Remove Items from a List
Likewise, you can use `.pop()` or `.pop(index)` to remove any type of element from a list.

`.pop()`:
- Removes an item from the end of the list.

```python
# your_list.pop()

my_class = ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha', 'Sonyl']
student_that_left = my_class.pop()
print("The student", student_that_left, "has left the class.")
# Sonyl
print(my_class)
# => ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha']
```

`.pop(index)`:
- Removes an item from the list.
- Can take an index.

```python
# your_list.pop(index)

my_class = ['Brandi', 'Zoe', 'Steve', 'Aleksander', 'Dasha']
student_that_left = my_class.pop(2) # Remember to count from 0!
print("The student", student_that_left, "has left the class.")
# => "Steve"
print(my_class)
# => ['Brandi', 'Zoe', 'Aleksander', 'Dasha']
```

## Built-in Operators for Analyzing Lists

Python has some built-in operations that allow you to analyze the content of a list. Some basic ones include:

#### `len()`

This tells you how many items are in the list; can be used for lists composed of any data type (i.e. strings, numbers, booleans)

```python
# length_variable = len(your_list)

my_class = ['Brandi', 'Zoe', 'Aleksander', 'Dasha']
num_students = len(my_class)
print("There are", num_students, "students in the class")
# => 5
```

#### `sum()`

This returns the sum of all items in *numerical lists*.

```python

# sum_variable = sum(your_numeric_list)

team_batting_avgs = [.328, .299, .208, .301, .275, .226, .253, .232, .287]
sum_avgs = sum(team_batting_avgs)
print(f"The total of all the batting averages is {sum_avgs}")
# => 2.409
```

#### `min()` & `max()`

These return the smallest and largest numbers *in a numerical list* respectively.

```python
# max(your_numeric_list)
# min(your_numeric_list)

team_batting_avgs = [.328, .299, .208, .301, .275, .226, .253, .232, .287]
print(f"The highest batting average is {max(team_batting_avgs}")
# => 0.328
print("The lowest batting average is", min(team_batting_avgs))
# => 0.208
```

## Sorting Lists

If you want to organize your lists better, you can sort them with the `sorted()` operator. At the some basic level, you can sort both numerically and alphabetically. **NOTE!** You cannot sort a list that includes different data types. 

#### **Numbers** - Ascending & Descending

```python
numbers = [1, 3, 7, 5, 6, 4, 2]

ascending = sorted(numbers)
print(ascending) # [1, 2, 3, 4, 5, 6, 7]
```
To do this in descending order, simply add `reverse=True` as an argument in `sorted()` like this:

```python
descending = sorted(numbers, reverse=True)
print(descending) # [7, 6, 5, 4, 3, 2, 1]
```

#### **Letters** - Alphabetically & Reverse

```python
letters = ['b', 'e', 'c', 'a', 'd']

ascending = sorted(letters)
print(ascending) # ['a', 'b', 'c', 'd', 'e']

descending = sorted(letters, reverse=True)
print(descending) # ['e', 'd', 'c', 'b', 'a']
```

## Tuples

Tuples are a special subset of lists - they are *immutable* - in that they cannot be changed after creation.

We write tuples as:

```python
score_1 = ('Taq', 100)

# OR

score_2 = 'Sue', 101
```

Tuples are denoted with the `()`.

We read tuples just like we would read a list:

```python
print(score_1[0]) # 'Taq'
```

## Sets

Sets are special lists in that they can only have **unique** elements

```python
set_1 = {1,2,3,4,5} # this is a set, notice the {}
set_2 = {1,1,1,2,2,3,4,5,5,5} # this is still a set
print(set_2) # {1,2,3,4,5}

print(set_1 == set_2) # True
```

Sets are not indexed, so you cannot access say the 3rd element in a set. Instead, you can:

```python
print(2 in set_1) # True
print(9 in set_1) # False
```
Here's a **[helpful list](https://snakify.org/en/lessons/sets/#section_4)** of set operations.


## 1. Simple List operations

1. Create a **list** with the names `"Holly"`, `"Juan"`, and `"Ming"`.
2. Print the third name.
3. Create a **list** with the numbers `2`,`4`, `6`, and `8`.
4. Print the first number.

## 2. Editing & Manipulating Lists

1. Declare a list with the names of your classmates
2. Print out the length of that list
3. Print the 3rd name on the list
4. Delete the first name on the list
5. Re-add the name you deleted to the end of the list
6. You work for Spotify and are creating a feature for users to alphabetize their playlists by song title. Below are is a list of titles from one user's playlist. Alphabetize these songs.
`playlist_titles = ["Rollin' Stone", "At Last", "Tiny Dancer", "Hey Jude", "Movin' Out"]`
7. Create a list with 6 numbers and sort it in descending order.

```python
# 1.

# 2.

# 3.

# 4.

# 5. 

# 6.

# 7.
  
```

## 3. Math Operations

1. Save a list with the numbers `2`, `4`, `6`, and `8` into a variable called `numbers`.
2. Print the max of `numbers`.
3. Pop the last element in `numbers` off; re-insert it at index `2`.
4. Pop the second number in `numbers` off.
5. Append `3` to `numbers`.
6. Print out the average number.
7. Print `numbers`.

```python
# 1.

# 2.

# 3.

# 4.

# 5. 

# 6.

# 7.

  
```

## Additional Resources

- [Python Lists - Khan Academy Video](https://www.youtube.com/watch?v=zEyEC34MY1A)
- [Google For Education: Python Lists](https://developers.google.com/edu/python/lists)
- [Python-Lists](https://www.tutorialspoint.com/python/python_lists.htm)
- [Python List Methods](https://www.programiz.com/python-programming/methods/list/)
- [Python Data Structures: Lists, Tuples, Sets, and Dictionaries Video](https://www.youtube.com/watch?v=R-HLU9Fl5ug)
