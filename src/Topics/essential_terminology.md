<!---
{"next": "Topics/basic_data_types.md","title": "Essential Terminology"}
-->

# Essential Terminology

Here are some words and concepts that will hopefully give you a more holistic view of the more technical aspects of the industry. 

## What Is a Computer Program?

It's a set of discrete, highly logical, and explicit instructions that are parsed and executed by a computer. We call this set of human-readable instructions **source code**, or colloquially, a **computer program**. A **programming language** is a series of grammar and rules that we can define towards writing this source code. Languages are effectively different approaches towards communicating the same ideas when writing source code.

**Compilers** then take this source code and transform it into **machine code**, a representation of the source that can be executed by the computer's **central processing unit** or **CPU**. 

Not all programs are compiled though, some are **interpreted**. This is dependent on which programming language you are using! The difference is that compiled languages need a step where the source code is physically transformed into machine code. However, with an interpreted language, this additional step is **excluded** in favor of **parsing** and **executing** the source code directly when the program is run.

### How programs are written

Programming languages *all build on the same fundamental concepts.* When you combine these concepts in any language, you can dictate a wide variety of tasks you might want your computer program to perform. The main difference lies in **how** each language runs the program (compiled vs interpreted) and also **how** each language is used. 

There are many programming languages. Way too many. But here are some of the most popular ones...

1. **JavaScript**: this language is interpreted.
2. **Python**: this language is interpreted.
3. **Java**: this language is compiled
4. **Ruby**: this language is interpreted.
5. **C/C++**: this language is compiled.

In general, anything programmable can be programmed in each of the languages defined above. However, some languages are better suited for certain tasks above others. For example, to perform web programming on the front-end, you'll want to write JavaScript. This is because all browsers collectively support running javascript within it's environment.

### Universal Code Fundamentals

Here are a collection of these most important concepts:

#### Declarations
Typically, we can store and retrieve data in our programs by associating them with intermediary values that we call **variables**.

#### Expressions
We use expressions to evaluate stuff. For example, **`2 + 2`** is an example of an expression that will **evaluate** a value, namely 4.

* **NOTE**: Typically we can use expressions and declarations in tandem to perform complex tasks. For instance, we can reference a variable we declared in an expression to help us evaluate new values which can then be stored.

#### Statements & Control Flow
Statements will use expressions and declarations to alternate a program's **control flow**, which is essentially the order in which declarations, expressions, and other statements are executed.

Aside from these fundamental concepts, we also talk a lot about this idea of **algorithms**. An **algorithm** is simple a series of declarations, expressions, and statements that can be used over and over again to solve well defined problems of a certain type.

Algorithms can be as **simple** as converting temperatures from Fahrenheit to Celsius or as **complex** as processing payment for a purchase using facial recognition software. Others example include...

* Managing what content to display based on search parameters
* Calculating the interest total interest paid on a mortgage based on the interest rate and # of payments since the mortgage was issued.
* Collecting user behavior data to analyze their interests and make better recommendations

## Thinking Programmatically w. Pseudocode

The beauty of programming lies in the universal set of fundamental concepts outlined above. For this reason, we do not need to specify any particular programming language when discussing the functional aspects of a program. This allows us to have initial, high-level discussions about a program's intended functionality using **pseudocode**, a mix of spoken language and coding syntax.

For example, we can write a program that converts temperature from **fahrenheit** to **celsius**. It would look something like this:

1. **Declare** F = 32;
2. **Expression** ( **F** - 32 ) / 1.8;
3. **Declare** C = **Evaluated** expression from **[2]**

^^ This is a form of pseudocode where we define the steps a computer program &mdash; **any** &mdash; computer program can take to convert **fahrenheit** to **celsius**.

#### **EXAMPLE 1**: Write the logic for the functionality of a smart thermostat.
- **When room temp is lower than some temp pre-set by the user, turn on heat. Call this value "cold".**
- **When room temp is higher than some temp pre-set by the user, turn on the A/C. Call this value "hot".**
- **When room temp is between the above two temps, turn off the thermostat.**

```python
# Example 1 Answer...

```

#### **PRACTICE 1**: Based on user input, deposit money into a bank account with some existing balance.

```python
# Practice 1 Answer...

```

#### **PRACTICE 2**: You have a recipe and want to convert the ingredient amounts into metric units.

```python
# Practice 2 Answer...

```

#### **PRACTICE 3**: You have a group of numbers. You want to square the evens and double the odds, display each result as you go.

```python
# Practice 3 Answer...

```

#### **PRACTICE 4**: Pseduocode Rock, Paper, Scissors! Given two player inputs (rock, paper, or scissors) - write a program that outputs the winner (e.g. p1 or p2).

```python
# Practice 4 Answer...

```

#### **PRACTICE 5**: You are a doctor and you store health information about each of your patients. Let’s talk about three patients in particular (p1, p2, & p3). As we do this, we’re concerned about various components of each patient’s medical records (e.g. height, blood pressure, cholesterol, etc.).

**p1** got married and changed her name.
**p2** lost 15 pounds since her last visit 2 years ago.
**p3** has hypothyroidism, so you’ve been tracking his TSH (Thyroid-Stimulating Hormone) levels every month for the past year. You want to show him how his TSH levels have fluctuated.

```python
# Practice 5 Answer...

```

#### **EXAMPLE 2**: You work for an ecommerce platform. After a customer buys one or more products, you need to update the remaining inventory of each product as well as record the profit you just made from this sale.

```python
# Example 2 Answer...

```
