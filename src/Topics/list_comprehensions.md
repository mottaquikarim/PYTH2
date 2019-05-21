<!---
{"next":"Topics/classes.md","title":"List Comprehensions"}
-->

# List Comprehensions

At their core, **list comprehensions** are a short-cut for transforming lists into other lists. Essentially, you can iterate through my_list using a condensed for-loop syntax. Till now, we've been fine using for loops to transform lists, but as your code gets more complicated, you'll be thankful for any short-cut!

Here's a one-to-one comparison of the general syntax for creating a list with a `for loop` versus a `list comprehension`. We'll use pseudo-code here for better initial context. These are the key elements to note in the list comprehension:

* The square brackets, a signature of Python lists;
* The `for` keyword, followed by an arbitrary variable to represent the list items
* The `in` keyword, followed by a list variable

```python
# for loop
<variable_for_values> = []
for <item> in <iterable>:
    <variable_for_values>.append(<expression>)

# list comprehension
<variable_for_values> = [<expression> for <item> in <iterable>]
```

The examples below also achieve the same outcome, but with actual code...

```python
# for loop
squares = []
for x in range(8):
	squares.append(x*x)
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49]

# list comprehension
squares = [x*x for x in range(8)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49]
```

## Incorporating Conditionals

Just like iterating through list items with a for loop, you might want to access only items adhering to one or more specific conditions. Let's walk through these use cases.

**Modify a List's Existing Items**

```python
grades = [100, 33, 98, 76, 54, 98, 89, 49]
curved_grades = []

# for loop
for grade in grades:
  curved_grades.append(grade + 10)

print(curved_grades) # [110, 43, 108, 86, 64, 108, 99, 59]

# list comprehension
curved_grades2 = [(grade + 10) for grade in grades]

print(curved_grades2) # [110, 43, 108, 86, 64, 108, 99, 59]
```

**Create a New List w. a Specific Subset of the Original List Items**

```python
grades = [100, 33, 98, 76, 54, 98, 89, 49]
failing_grades = []

# for loop
failing_grades = []
for grade in grades:
  if grade < 65:
    failing_grades.append(grade)
  
print(failing_grades) # [33, 54, 49]

# list comprehension
failing_grades = [grade for grade in grades if grade < 65]

print(failing_grades) # [33, 54, 49]
```


