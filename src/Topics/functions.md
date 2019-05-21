<!---
{"next":"Topics/list_comprehensions.md","title":"Functions"}
-->

# Functions

In Python, `functions` are your best friends! Let's say you need to perform some action or calculation multiple times for multiple values. For example, you might want to convert temperatures in Celsius to Fahrenheit like you did in the last chapter's exercises. It would be inefficient and messy to copy that code every time you need it. Instead, you can define a `function` to contain that code. Every time you call that function, it runs the whole block of code inside and saves you lots of time. Sweet!

Python includes lots of built-in functions in its main library. We've seen lots of these already like `len()`, `sum()`, `.append()`, `.popitem`, etc. You can extend the range of built-in functions available to you by importing `modules`. We'll talk about those next!

## Elements of a Function

For now, let's start with the basics. Here's the skeleton of a function and a breakdown of each part.

```python
def function_name(parameters):
	"""docstring"""
	# statement(s)
```

* `def` shows you are "defining" a new function
* A unique function name; same naming rules as  variables)
* *Optional* parameters, or arguments, to be passed into the function when it is called.
* `:` ends the function header
* An *optional* `docstring`, i.e. a comment with documentation describing the function.
* At least one statement make up the "function body"; this code achieves the purpose for calling the function.
* An *optional* return statement, which exits the function and passes out some value from the body code.

**NOTE!** *It is a best practice to always create notes and documentation. Other potential users of your functions - and maybe future YOU - will thank you for the extra info.*

## Input/Output: Function Arguments & The `return` Statement

When you create a function, you might need to feed it some input and have it give back some output. We call function input `arguments` and function output `return` values. Remember - both `arguments` and `return` values are *optional* depending on the purpose of your function.

Let's say we want to create a function to get the square of a number. At the most basic level, there are three parts:
1. Input the number we want to square
2. Calculate the square of that number
3. Output the square of that number

Let's implement this in a function called `NumSquared()`.

```python
def num_squared(num):
	"""Find the square of some number passed in"""
	square = num*num # code to find the square
	return square
```

1. Input the number we want to square 
	We create an *parameter* called `num` to represent the number we will past into our function as an argument. (p.s. Parameters are the names used when defining a function.) Remember that arguments should always be passed in the correct format and positional order, or the function will not be able to recognize them.
2. Calculate the square of that number
	Using the value of `num`, we write the formula for calculating a square and assign it to the variable `square`.
3. Output the square of that number
	We return `square` to pass out the numeric value we calculated. The return statement exits the function so the program can move on to the next block of code you've written. If you don't need to specify a value to return, the function will default to `return None` in order to exit the function.

Once we've written this logic, we can call `NumSquared()` every time we want to use it. Let's say we want to find the value of 12 squared...

```python
sq12 = num_squared(12)
print(sq12) # 144
```

**NOTE!** You should store the function call within a var so that the return value gets stored in the var. If you don't, how will you access the output you wanted??

One last thing - you should know that the `return` statement can return multiple values *by using tuples*. Once you return the tuple from the function, you can *unpack* its values by simultaneously assigning each one to a new var as follows...

```python
	# some function...
	return 3,'a',True

x, y, z = (3,'a',True)
print(x, type(x)) # 3 <class 'int'>
print(y, type(y)) # a  <class 'str'>
print(z, type(z)) # True <class 'bool'>
```

## Argument Types

#### Required Arguments
If your function won't work without specific arguments, you can define the function with **required arguments**. In order for anyone to call the function, that user *must* always pass values for the required arguments in the correct positional order with the correct syntax you defined in advance. For example...

```python
def plus(a,b):
  return a + b

c = plus(8,12)
print(c) # 20
```

#### Keyword Arguments
Now switch perspectives. You're using a function that your colleague defined. If you want to make sure that you call all the required arguments in the right order, you can use the **keyword arguments** in your function call. Essentially, this means that you mention each argument's parameter name when you assign it a value during the function call. It works like this...

```python
def plus(a,b):
  return a + b

c = plus(a=8,b=12)
print(c) # 20
```

#### Default Arguments
Back to writing our own functions! If you want, you can give your function a **default argument**. Functions with default arguments take some pre-defined default value if no argument value is passed when you call the function. When defining your own function, you can assign this default value like this:

```python
def plus(a,b = 12):
  return a + b
  
# Only passing a value for `a`...
c = plus(a=8)
print(c) # 20

# ...vs. passing values for `a` and `b`
c = plus(8, 17)
print(c) # 25
```

#### Variable number of Arguments
Even if you're not sure how many arguments you will need to pass to your function, you can still define it. To do this, you use the parameter `*args` as a stand-in. This signals to the function that it should expect any variety of arguments. Let's take a look at a few different ways to implement this.

**Using integers** (as we did in the earlier examples)

```python
def plus(*args):
  return sum(args)

c = plus(8,12,17)
print(c) # 37
```

**Using different data types**

```python
def length(*args):
  list1 = [*args]
  return len(list1)

c = length(8,'a',True)
print(c) # 3
```

**Using a variable**

```python
var1 = 'h' + 'i'
def print_all(*args):
  list1 = [*args]
  return list1

c = print_all(8,'a',True,var1)
print(c) # [8, 'a', True, 'hi']
```

**NOTE!** If you use `*args`, your function will be more flexible, *but only if you write it that way*. If you expect different types of arguments, you will have to write the function such that it can handle every use case you expect could occur.

## Variable Scope Recap

* `global variable`: a variable declared outside a function; any function in your script can access this
* `local variable`: a variable declared within a function's code block; you can only access this variable within the function where it is declard, otherwise you will get a `NameError` telling you that variable is not defined.


```python
x = 'I\'m a global variable.'

def foo():
	x = 'I\'m a local variable.'
    print(x) # I'm a local variable.
    return x

y = foo()

print(x) # I'm a global variable.
print(y) # I'm a local variable.
```

Notice that even though the function `foo()` above says `return x`, it **only returns the value of the local variable `x`**. We assign this *value* to the variable `y` when we call foo().

Look at the nuanced difference in this example though:

```python
def foo():
    x = 'I\'m a local variable.'
    print(x) # I'm a local variable.
    return x

foo()

print(x) # NameError: name 'x' is not defined
```

Even though we called the function `foo()`, we did not assign its return value to a variable outside the function. Therefore, trying to print `x` will output `NameError: name 'x' is not defined`. This is because `x` only exists within the function.

## Practice Problems
