#  PANDAS1 BASICS

## NDARRS

### P1.PY



```python
"""
ndarray properties
"""

import numpy as np

# Creating array object
arr = np.array([[1, 2, 3],
                [4, 2, 5]])

# Given the above:

# Printing type of arr object
print("Array is of type: ", None)  # how would you print type?

# Printing array dimensions (axes)
print("No. of dimensions: ", None)  # how would you print dimensions?

# Printing shape of array
print("Shape of array: ", None)  # how would you print "shape"

# Printing size (total number of elements) of array
print("Size of array: ", None)  # how would you print size?

# Printing type of elements in array
# how would you print element type?
print("Array stores elements of type: ", None)

```


### P2.PY



```python
"""
ndarrays operations 
"""

import numpy as np

# Create array from list with type float
a = None

# Create array from tuple
b = None

# Create a 3X4 array with all zeros
c = None

```


### P3.PY



```python
"""
ndarray indexing
"""

import numpy as np

# given this
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

# grab first two rows of arr
a = None

# grab second and third row of arr
b = None

# grab first two rows of arr and first two columns
c = None

# grab elements at indices (0, 3), (1, 2), (2, 1), (3, 0)
d = None

# grab elements > 0
e = None

```


### P4.PY



```python
"""
basic operations
"""

import numpy as np

a = np.array([1, 2, 5, 3])

# add 1 to every element
a = None
print("Adding 1 to every element:", a)

# subtract 3 from each element
b = None
print("Subtracting 3 from each element:", b)

# multiply each element by 10
c = None
print("Multiplying each element by 10:", c)

# square each element
d = None
print("Squaring each element:", d)

# Doubled each element of original array
print("Doubled each element of original array:", arr)

```


### P5.PY



```python
"""
basic operations II
"""

import numpy as np

arr = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])

# maximum element of array
print("Largest element is:", 0)

# minimum element of array
print("Smallest element is:", 0)

# maximum element per row
print("Row-wise maximum elements:",
      [])

# minimum element per col
print("Column-wise minimum elements:",
      [])

# sum of array elements
print("Sum of all array elements:",
      0)

# cumulative sum along each row
print("Cumulative sum along each row:\n",
      0)

c = np.array([[1, 2],
              [3, 4]])
d = np.array([[4, 3],
              [2, 1]])

# add arrays
print("Array sum:\n", None)

# multiply arrays (elementwise multiplication)
print("Array multiplication:\n", None)

```


## SERIES

### P1.PY



```python
"""
Simple Series
"""


# import pandas as pd
import pandas as pd

# import numpy as np
import numpy as np


# simple array
data = np.array(['l', 'a', 'y', 'l', 'a'])

# convert data to series
ser = None

# grab the first three items from ser
sub = None

# create series with custom label such that:
"""
a    l
b    a
c    y
d    l
e    a
dtype: object
"""
ser2 = None

# access "y" from series ser2
print("accessing 'y'", None)

```


### P2.PY



```python
"""
Indexing and Selecting Series
"""

# import pandas as pd
import pandas as pd

# import numpy as np
import numpy as np

# create a new series
s = pd.Series(np.nan, index=[49, 48, 47, 46, 45, 1, 2, 3, 4, 5])

# using iloc, get the first 3 items in series
t = None

# using loc, do the same
u = None

# using index operators, do the same
v = None

```


### P3.PY



```python
"""
Series operations
"""

# importing pandas module
import pandas as pd

# creating a series
data1 = pd.Series([5, 2, 3, 7], index=['a', 'b', 'c', 'd'])

# creating a series
data2 = pd.Series([1, 6, 4, 9], index=['a', 'b', 'd', 'e'])

# add data1 and data2


# subtract data1 and data2

```


#  PANDAS1 WINE REVIEWS

## CHECK_IMPORTED_DATA

### P1.PY



```python
"""
Checking Imported Data I - Data Dictionary
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')


# Access a summary of the core metadata of the DataFrame (i.e. the number and name of columns, the rows, etc.)
```


### P2.PY



```python
"""
Checking Imported Data II - How Big is the Data?
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')


# Print the number of rows and columns in wine_reviews.



# Print the number of elements in wine_reviews.


```


### P3.PY



```python
"""
Checking Imported Data III - DataFrame Labels
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')


# Access the labels on the rows of data.




# Access the labels on the columns of data.



# Return the labels for the rows and columns in wine_reviews in one command.



```


### P4.PY



```python
"""
Checking Imported Data IV - Preview Data
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')


# Print out the first and last 10 rows of data.
```


## SELECTING_DATA

### P1.PY



```python
"""
Selecting Data I - Access a Row
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')


# Return the 12th row in the wine_reviews dataframe.



```


### P2.PY



```python
"""
Selecting Data II - Access a Column
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')


# Return the winery column in a variable called "wineries".



# Run a command to return the type of wineries.


```


### P3.PY



```python
"""
Selecting Data III - Access Single Values
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')

# Print the value in the 5th column of the 7th row.


# Create a Series called "countries" from the 'country' column and print item at index 18.


# Print the 10th item in countries.

```


### P4.PY



```python
"""
Selecting Data IV - Access Slices
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')


# Print first 3 values in the 'province' column.



# Create a Series called "provinces" and print the first 3 values.


```


### P5.PY



```python
"""
Selecting Data V - Subsets
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')

# Create a new dataframe called "wine_ratings" that is a subset of wine_reviews. It should have these columns in this order:
### title
### country
### points
### price
```


### P6.PY



```python
"""
Selecting Data VI - Min & Max (CHALLENGE!)
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')


# Find the 5 rows with the highest-priced wine and the 5 rows with the lowest-priced wine. Assign them to variables called 'a' and 'b' respectively. Print 'a' and 'b'.



# Create a function to print out the variety and price of some number of the most and least expensive wines. Hints:
### It should contain loops
### The number function should take any number for finding the highest and lowest priced wines (e.g. top and bottom 5, top and bottom 10, etc.)
### If you're iterating through a 2 column dataframe item by item, remember the counting goes like this:
"""
[0,0], [0,1]
[1,0], [1,1]
[2,0], [2,1]
[3,0], [3,1]
[4,0], [4,1]
"""


```

