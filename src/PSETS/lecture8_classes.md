#  CLASSES

## CLASS_BASICS

### P1.PY



```python
"""
RGB to HEX
"""

# Remember our function "rgb_hex" from the functions pset? That function took a color in rgb format and returned it in hex format as well as vice versa. Wouldn't it be so much easier to do that with a class called Color?

# Define a class called "Color" to store each color's rgb and hex values. Define a method called "convert_codes()" to retrieve one value given the other. Create at least one instance of Color and try the convert_codes() method.


```


### P2.PY



```python
"""
Phone Contacts
""" 

# Create a class called "Contact" that will store the below items for each contact in your phone. The starred items should be required.
    ### name*
    ### mobile_num
    ### work_num
    ### email

```


### P3.PY



```python
"""
Rectangle
"""

# Write a Python class named "Rectangle" constructed by values for length and width. It should include two methods to calculate the "area" and the "perimeter" of a rectangle. Instantiate a Rectangle and call both methods.
```


### P4.PY



```python
"""
Circle
"""

# Write a Python class named "Circle" constructed by a radius value and a class attribute for pi. You can use 3.14159 for the value of pi for simplicity. It should include two methods to calculate the "area" and the "perimeter" of a circle. Instantiate a Circle and call both methods.




```


### P5.PY



```python
"""
Vehicles I 
"""

# Create a "Vehicle" class with a class attribute for category ('transportion') and a method called "start_engine()" that prints "Vroom!". Add "name" as an instance method and instantiate a Vehicle called "submarine". Access all its attributes and methods for practice.

# Note: See Vehicles II in p6 for an explanation of why we chose "submarine" as a vehicle instance!


```


### P6.PY



```python
"""
Vehicles II
"""

# Define 3 unique child classes for Vehicle - Car, Plane, and Boat. Each of these should have its own class attributes for "motion" and "terrain". (For Car, these would be something like "drive" and "land".)

## For Car, define a method called "honk_horn()" that prints "HONK!"
## For Plane, define a method called "take_off()" that prints "Fasten your seatbelts!"
## For Boat, define a method called "drop_achor()" that prints "Anchors away!"

# Create an instance of each child class. Access all their attributes and methods, including those inherited from their parent class Vehicle.

# TAKEAWAY! - Vehicle is the baseline class for other more specific types of vehicles. Typically, you wouldn't instantiate a Vehicle because the child classes are more useful for storing information about vehicles. The Vehicle class serves to create a relationship between its children. However, "submarine" might be created as a Vehicle because it's so rare that you might not need a full Submarine class!
```


### P7.PY



```python
"""
Vehicles III
"""

# Let's expand the Car class to be more comprehensive. Include attributes for brand name, plates, owner, fuel, fuel_level (a numerical amount that defaults to 50, and max speed in MPH that defaults to None. 

# Next, define new method called "check_fuel_level()". If the fuel_level attribute is < 15, the method should reset fuel_level to 50 and print out how many units it refueled the car, e.g. 'Refueled 38 units.' Otherwise, it should simply print 'No need to refuel right now.'

# Create at least TWO instances of Car, one of which has a fuel level below 15. Access the new attributes and call the check_fuel_level() method for each instance. 
```


### P8.PY



```python
"""
Dogs I - Breeds
""" 

# A) Create a class called "Dog". It should include: 
### A class attribute "domesticated" w. value True
### An instance method called "bark()" that prints "Woof!"

# B) Create child class for 3 dog breeds - Collie, Siberian Husky, and Pekingese. Each should have:
### 2 class attributes for "breed" and "temperament". The latter should be a list.
### 3 instance attributes for "name", "age", and "gender".

# C) Add an instance method to Collie called "herd_the_kids()" that prints "Here are your children!"

# D) Add an instance method called "bark()" to Pekingese. This should override the parent method "bark()" such that when you call bark() on an instance of Pekingese, it prints "Yap!" instead.

# E) Instantiate one of each breed. Access the attributes, methods, and parent methods of each one. BONUS: Aside from herd_the_kids(), you should be able to do this in a loop.



```


### P9.PY



```python
"""
Dogs II - Tricks (CHALLENGE!)
"""

# Many dogs know how to do common tricks or follow common commands. You could create methods for each trick/command in the Dog parent class, but the problem is that not all dogs know all tricks/commands. 

# However, it would be inefficient to define a custom set of instance methods for tricks/commands every time you instantiate a unique Collie (or SiberianHuskey or Pekingese etc.).

# Find an efficient way to specify which tricks each unique dog knows and to call them. You can use "roll_over", "fetch", "shake_hands", and "spin". Secondly, find a way to teach a dog new trick from this set.



```


## CLASS_BASICS_2

### P1.PY



```python
"""
Dog Class
"""

# Implement a class called "Dog" with the following properties:
# name
# breed
# age

```


### P2.PY



```python
"""
Cat class
"""

# Implement a class called "Cat" with the following properties:
# name
# breed
# age

# also, implement a method called "speak" that should print out "purr"

```


### P3.PY



```python
"""
Student class
"""

# Create a Student class and initialize it with name and roll number. Make methods to :
# 1. Display - It should display all informations of the student.
# 2. setAge - It should assign age to student
# 3. setMarks - It should assign marks to the student.

```


### P4.PY



```python
"""
Person class
"""

# Create a Person class with the following properties
# 1. name
# 2. age
# 3. social security number

```


### P5.PY



```python
"""
Vehicle class
"""

# Create a Vehicle class with the following properties

# * name
# * kind
# * color
# * value

# It should also have a description method that returns something like:
# "{name} is a {color} {kind} worth {value}."

```


## WEDDING_GUESTS

### P1.PY



```python
"""
Weddings I - Guest List
"""

# Imagine for this problem set that you are planning a wedding. 


# A) Define a class called "Guest" to help you manage all the information about each invitee. This should initially include instance attributes for the guests's name, phone, and an optional "invite_sent" that defaults to False. Guest should also include an instance method called "send_invite()", which changes the value of invite_sent to True once you send an invitation to that guest.



# B) Next, define a child class called "Bridesmaid", which includes the same initial attributes and inherits Guest's instance method.



# C) Finally, create at least one instance of each class and do the following:
### Call send_invite() on each instance.
### Check whether Bridesmaid is a child of Guest and vice versa.
```


### P2.PY



```python
"""
Weddings II - Record Bridesmaid RSVPs
"""

# Create a method in Guest to record a guests's rsvp to your invitation. It should record whether they have any dietary restrictions (e.g. vegetarian, kosher, halal, etc.) and whether they're bringing a plus one. If they are bringing a plus one, it should record the name of the plus one and his/her dietary restrictions if any. These values should be stored in instance attributes.

# Try out this method on at least one instance of Guest and at least one instance of Bridesmaid.
```


### P3.PY



```python
"""
Weddings III - Record Shower & Bachelorette RSVP
"""

# Create two methods in Bridesmaid to record a the bridesmaid's rsvp to the bridal shower and the bachelorette party. You can call them "record_shower_rsvp()" and "record_bachelorette_rsvp()". They will work just like the general "record_rsvp()" except there will be no plus ones or diet questions. Their rsvp answers should be stored in instance attributes with the same name (i.e. shower_rsvp & bachelorette_rsvp).
```

