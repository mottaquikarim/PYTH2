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

#### When to Use Python

*Python is simple, versatile, always improving, and popular among many reputable companies!*

Python is particularly well-suited for dynamically processing large amounts of data and analyzing it. That’s what makes it so great for data science.

- Putting up websites.
- Analyzing data.
- Constructing machine learning algorithms
- Building robots.

#### When NOT to Use Python

Python isn't great for everything!

- Mobile apps
- Huge programs
  - Python is interpreted - the computer reads it as it goes.
  - Other programming languages are read in advance!
- Sometimes too easy
  - Easy to expect things to work that don't!

### Universal Code Fundamentals

**Declarations**
Typically, we can store and retrieve data in our programs by associating them with intermediary values that we call **variables**.

**Expressions**
We use expressions to evaluate stuff. For example, **`2 + 2`** is an example of an expression that will **evaluate** a value, namely 4.

* **NOTE**: Typically we can use expressions and declarations in tandem to perform complex tasks. For instance, we can reference a variable we declared in an expression to help us evaluate new values which can then be stored.

**Statements & Control Flow**
Statements will use expressions and declarations to alternate a program's **control flow**, which is essentially the order in which declarations, expressions, and other statements are executed.

--

Aside from these fundamental concepts, we also talk a lot about this idea of **algorithms**. An **algorithm** is simple a series of declarations, expressions, and statements that can be used over and over again to solve well defined problems of a certain type.

Algorithms can be as **simple** as converting temperatures from Fahrenheit to Celsius or as **complex** as processing payment for a purchase using facial recognition software. Others example include...

* Managing what content to display based on search parameters
* Calculating the total interest paid on a mortgage based on the interest rate and # of payments since the mortgage was issued.
* Collecting user behavior data to analyze their interests and make better recommendations

## Thinking Programmatically w. Pseudocode

The beauty of programming lies in the universal set of fundamental concepts outlined above. For this reason, we do not need to specify any particular programming language when discussing the functional aspects of a program. This allows us to have initial, high-level discussions about a program's intended functionality using **pseudocode**, a mix of spoken language and coding syntax.

For example, we can write a program that converts temperature from **fahrenheit** to **celsius**. It would look something like this:

1. **Declare** F = 32;
2. **Expression** ( **F** - 32 ) / 1.8;
3. **Declare** C = **Evaluated** expression from **[2]**

^^ This is a form of pseudocode where we define the steps a computer program &mdash; **any** &mdash; computer program can take to convert **fahrenheit** to **celsius**.

```python
# PRACTICE SECTION!
```

#### **EXAMPLE 1**: Write the logic for the functionality of a smart thermostat.
- **When room temp is lower than some temp pre-set by the user, turn on heat. Call this value "cold".**
- **When room temp is higher than some temp pre-set by the user, turn on the A/C. Call this value "hot".**
- **When room temp is between the above two temps, turn off the thermostat.**

```python
# Example 1 Answer...

"""
1. Grab pre-set "hot" and "cold" temperature values.
2. Is current temp > "cold" AND < "hot"?
3. If yes, keep system off or turn it off.
4. If no, is current temp <= "cold"?
5. If yes, turn on heat.
6. If no, is current temp >= "hot"?
7. If yes, turn on A/C.
"""

# OR

"""
hot = 76
cold = 66

if cold < current_temp < hot then...
  if system A/C == True or heat == True, turn system off

if current_temp <= cold then...
  turn on heat
  
if current_temp >= heat then...
  turn on A/C
"""
```

#### **PRACTICE 1**: Based on user input, deposit money into a bank account with some existing balance.


```python
# Practice 1 Answer...

"""
1. Is user input a #?
2. If not, show error message.
3. If yes, add this # to existing balance # and save this new value.
"""

# OR

"""
acc1_balance = 100
deposit_input = 50

if deposit_input is NOT a number then...
  show message to enter a valid number

otherwise...
  acc1_balance = deposit_input + acc1_balance
"""
```

#### **PRACTICE 2**: You have a recipe and want to convert the ingredient amounts into metric units. The first 3 ingredients are 0.5 tbsp butter, 1.5 cups flour, and 2 ounces milk. Hint: Metric conversions for these are: tbsp become grams, ounces become grams, & cups become mL.

**NOTE!** There are MANY units to consider here, as well as solid vs. liquid units. To simplify this example, we'll only look at the 3 above!

```python
# Practice 2 Answer...

"""
1. Look at first ingredient
2. Do math to convert to metric units
3. Update and save the new metric value for that ingredient.
4. Look at second ingredient
5. Repeat steps 2 and 3.
6. Look at third ingredient
7. Repeat steps 2 and 3.
8. etc...
"""

# OR

"""
ingredients is a collection of ingredient names, numerical amounts, and units like so:

ingredients =
  'butter', 0.5, 'tbsp'
  'flour', 1.5, 'cups'
  'milk', 2, 'ounces'


for each ingredient...
if unit for ingredient == 'tbsp' then...
  convert numerical amount of 'tbsp' to 'grams'
  if not, continue to next use case

if unit for ingredient == 'cups' then...
  convert numerical amount of 'ounces' to 'mL'
  if not, continue to next use case

if unit for ingredient == 'ounces' then...
  convert numerical amount of 'cups' to 'grams'

repeat above use cases for 'sugar'
repeat above use cases for 'flour'
"""
```

#### **PRACTICE 3**: You have a group of numbers. You want to square the evens and double the odds, display each result as you go.

```python
# Practice 3 Answer...

"""
1. Look at first number
2. Is # even? (expand on this)
3. If yes, display result of #^2 (sq’d)
4. If not, it must be odd. Thus, display result of # x 2.
Repeat steps 2-4 for each of rest of numbers in the group
"""

# OR

"""
numbers = 1, 2, 3, 4, 5

if 1 is even then...
  print 1^2
otherwise...
  print 1*2

repeat above code for 2, 3, 4, and 5


resultant numbers = 2, 4, 6, 16, 10
"""
```

#### **PRACTICE 4**: Pseduocode Rock, Paper, Scissors! Given two player inputs (rock, paper, or scissors) - write a program that outputs the winner (e.g. p1 or p2).

```python
# Practice 4 Answer...

"""
- If p1 plays rock and p2 plays rock, display tie
- If p1 plays rock and p2 plays paper, display p2 as winner
- If p1 plays rock and p2 plays scissor, display p2 as winner
- If p1 plays scissor and p2 plays scissor, display tie
- If p1 plays scissor and p2 plays rock, display p2 as winner
- If p1 plays scissor and p2 plays paper, display p1 as winner
- If p1 plays paper and p2 plays paper, display tie
- If p1 plays paper and p2 plays rock, display p1 as winner
- If p1 plays paper and p2 plays scissor, display p2 as winner
"""

# OR

"""
if p1 == p2 then tie
if p1 == r and p2 == p then p2
if p1 == r and p2 == s then p1
if p1 == p and p2 == r then p1
if p1 == p and p2 == s then p2
if p1 == s and p2 == r then p2
if p1 == s and p2 == p then p1
"""
```

#### **PRACTICE 5**: You are a doctor and you store health information about each of your patients. Let’s talk about three patients in particular (p1, p2, & p3). As we do this, we’re concerned about various components of each patient’s medical records (e.g. height, blood pressure, cholesterol, etc.).

**p1** got married and changed her name.

**p2** lost 15 pounds since her last visit 2 years ago.

**p3** has hypothyroidism, so you’ve been tracking his TSH (Thyroid-Stimulating Hormone) levels every month for the past year. You want to show him how his TSH levels have fluctuated.

```python
# Practice 5 Answer...*
```

**p1 got married and changed her name.**
1. Locate p1 in patient database.
2. Grab name of p1 and update with new value

OR...

```python
"""
p1 got married and changed her name.

search p1 metadata for name info

# existing record is...
name = 'Suzie Harrison' # existing record

# update the record...
name = 'Suzie Bradley' # updated record
"""
```

**p2 lost 15 pounds since her last visit 2 years ago.**

1. Locate p2 in patient database.
2. Grab weight of p2
3. Add the date and p2’s new weight to p2’s weight history
4. Grab age of p2
5. Add age + 2 and update p2’s age

OR...

```python
"""
p2 lost 15 pounds since her last visit 2 years ago.

search p1 metadata for weight info

# existing record is... 
weight = 
  date1, weight1
  date2, weight2
  date3, weight3

# update the record...
weight = 
  date1, weight1
  date2, weight2
  date3, weight3
  date4, weight4
"""
```

**p3 has hypothyroidism, so you’ve been tracking his TSH (Thyroid-Stimulating Hormone) levels every month for the past year. You want to show him how his TSH levels have fluctuated.**
1. Locate p3 in patient database.
2. Grab TSH levels of p3
3. Graph the TSH levels for all measurements within the last 12 months.

OR...

```python
"""
p3 has hypothyroidism, so you’ve tracked his TSH (Thyroid-Stimulating Hormone)
levels every month for the past year. You want to show him how his TSH levels
have fluctuated.


search p3 metadata for TSH_level info

# existing record is...
TSH_level = 
  month1, tsh1
  month2, ths2
  ... etc ...
  month 15, tsh15

last_years_TSH = subset of TSH_level w. last 12 months (month4 through month15)

graph_values(last_years_TSH)
    months on x-axis
    TSH_level on y-axis

    display graph    
"""
```

#### **EXAMPLE 2**: You work for an ecommerce platform. After a customer buys one or more products, you need to update the remaining inventory of each product as well as record the profit you just made from this sale.

```python
# Example 2 Answer...

"""
1. Look at first product and its metadata (e.g. inventory amount, quantity purchased, retail price, and wholesale price).
2. How many of this product were in the inventory before this purchase?
Subtract quantity purchased from that number and save
3. the new inventory amount.
Look up the retail price and wholesale price of that product
4. Multiply retail price * quantity purchased (result is gross profit)
Subtract wholesale price from result of step 5 (result it net profit)
5. Add the profit from this sale to your accounting database
Repeat for rest of products purchased
"""

# OR

"""

products_purchased is a collection of items from the user's purchase, containing each product's name and quantity_purchased

products_purchased = 
	jeans, 2
	shirt, 3
	shoes, 1


products is a representation of the inventory metadata, containing each product's name, remaining_inventory (i.e. how much of product is in stock), retail_price, wholesale_price, unit_profit_margin, quantity_purchased_to_date, and profits_to_date

products = 
	jeans, 24, 10.25, 16.00, 5.75, 8, 46.00
	shirt, 56, 7.75, 12.50, 4.75, 10, 47.50
	shoes, 15, 12.00, 19.99, 7.99, 5, 39.95

search products for jeans metadata

remaining_inventory = remaining_inventory - quantity_purchased # 24 - 2 = 22

purchase_gross_revenue = retail_price * quantity_purchased # 16.00 * 2 = 32.00
cost = wholesale_price * quantity_purchased # 10.25 * 2 = 20.50
purchase_profit = purchase_gross_revenue - cost # 32.00 - 20.50 = 11.50

profits_to_date = profits_to_date + purchase_profit # 46.00 + 11.50 = 57.50


repeat steps for user's purchases of shirt and shoes products
"""

```
