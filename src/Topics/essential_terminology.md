<!---
{"next": "Topics/basic_data_types.md","title": "Essential Terminology"}
-->

# Essential Terminology

Here are some words and concepts that will hopefully give you a more holistic view of the more technical aspects of the industry. 

## Define: Program

Discrete, highly logical and explicit instructions that are parsed and executed by a computer.

We call this set of human-readable instructions **source code**, or colloquially, a **computer program**.

**Compilers** can take this source code and transform it into **machine code**, a representation of the source that can be executed by the computer's **central processing unit** or **CPU**. 

Not all programs are compiled though, some are **interpreted**. The difference is that compiled languages need a step where the source code is physically transformed into machine code. However, with an interpreted language, this additional step is **excluded** in favor of **parsing** and **executing** the source code directly when the program is run.

## How programs are written

All programs are composed with a collection of **fundamental** concepts that, when combined, can essentially dictate a wide variety of tasks a computer can perform.

Here are a collection of these most important concepts:

#### Declarations
Typically, we can store and retrieve data in our programs by associating them with intermediary values that we call **variables**
#### Expressions
We use expressions to evaluate stuff. For example, **`2 + 2`** is an example of an expression that will **evaluate** a value, namely 4. 
* **NOTE**: typically we can use expressions and declarations in tandem to perform complex tasks. For instance, we can reference a variable we declared in an expression to help us evaluate new values which can then be stored.
#### Statements & Control Flow
Statements will use expressions and declarations to alternate a program's **control flow**, which is essentially the order in which declarations, expressions, and other statements are executed.

Aside from these fundamental concepts, we also talk a lot about this idea of **algorithms**. An **algorithm** is simple a series of declarations, expressions, and statements that can be used over and over again to solve well defined problems of a certain type.

For example, we can implement an algorithm that converts temperature from **fahrenheit** to **celsius**. It would look something like this:

1. **Declare** F = 32;
2. **Expression** ( **F** - 32 ) / 1.8;
3. **Declare** C = **Evaluated** expression from **[2]**

This is a form of **pseudo** code where we define the steps a computer program &mdash; **any** &mdash; computer program can take to convert **fahrenheit** to **celsius**.

The beauty of programming is that all of it revolves around the same key set of concepts and ideas. For this reason, we do not need to specify any **particular programming language** when discussing the functional aspects of a program.

## Define: Programming languages

A programming language is a series of **grammar** and **rules** that we can define towards writing source code.

Languages are effectively different approaches towards communicating the same ideas in programming. Essentially, we can communicate in say both **French** and **English**, what mainly differs is the structure of our sentences and the actual words and sounds themselves.

The **same analogy** can be made with programming languages.

## Examples of programming languages

There are many. Way too many. 

Here are some of the most popular ones, though.

1. **JavaScript**: this language is interpreted.
2. **Python**: this language is interpreted.
3. **Java**: this language is compiled
4. **Ruby**: this language is interpreted.
5. **C/C++**: this language is compiled.

These languages all build on the same concepts defined above; the main difference lies in **how** they are run (compiled vs interpreted) and also **how** they are used. 

In general, anything programmable can be programmed in each of the languages defined above. However, some languages are better suited for certain tasks above others. 

For example, to perform web programming on the front-end, you'll want to write JavaScript. This is because all browsers collectively support running javascript within it's environment.

## Why Learn Python

Here's a blog post from Dan Bader that outlines some data-driven reasons learning python right now can pay off -- https://dbader.org/blog/why-learn-python

## 🚗 Practice: WE DO

Let's pseudocode a thermostat. User is able to:

* Set a temperature
* When room temp is greater than set temp, turn on heat
* Otherwise, turn off heat

## 🚗 Practice: YOU DO

Pseduocode Rock, Paper, Scissors!

Given two player inputs, `p1` and `p2` - where each selection can be one of: `{"r", "p", "s"}` - write a program that outputs the `winner` as: 

* `p1`, meaning player 1 has won
* `p2`, meaning player 2 has won

