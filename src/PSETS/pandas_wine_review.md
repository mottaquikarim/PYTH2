#  PANDAS1 WINE REVIEWS

## [DATA](https://raw.githubusercontent.com/mottaquikarim/pydev-psets/master/pset_pandas1_wine_reviews/winemag-data-130k.csv)

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


## SORTING

### P1.PY



```python
"""
Data Organization I - Sorting a Series
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')

# Using this Series, sort the elements alphabetically.

countries = wine_reviews['country']



# Using this Series, sort the elements from highest to lowest.

prices = wine_reviews['price']
```


### P2.PY



```python
"""
Data Organization II - Sorting a DataFrame
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')

# Using this DataFrame, sort the rows reverse alphabetically based on the 'country' column.

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]




# Now sort the DataFrame's rows based on price from highest to lowest.


```


### P3.PY



```python
"""
Data Organization III - Sorting a DataFrame by Multiple Columns
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')

# Using this DataFrame, sort the rows first, alphabetically by 'country', and second, by 'rating' from highest to lowest.

ratings_by_location = wine_reviews[['country', 'province', 'rating']]



# Take a look at the result by printing out the rows from indeces 0 to 10 as well as the rows from indeces 52065 to 52075.

```


## EDA

### P1.PY



```python
"""
Exploratory Data Analysis I - Core Stats Summary
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')
wine_reviews.rename(columns={'points': 'rating'}, inplace=True)

# With one function call, return the core statistics for the wine_ratings DataFrame below.

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]


# Drop the null values in the latter three columns and drop duplicates based on the 'title' column. Then return the core statistics again.


```


### P2.PY



```python
"""
Exploratory Data Analysis II - Unique Values
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')

# Print a list of all the unique countries in the wine_reviews DataFrame in alphabetical order. Also print the number of unique countries that exist in the dataset. Hint: Don't just find the length of your first result.


```


## DATA_CLEANING

### P1.PY



```python
"""
Cleaning Data I - Drop Columns
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')


# Drop the 'region_2' and 'taster_twitter_handle' columns.

```


### P10.PY



```python
"""
Cleaning Data X - Fill Null Values
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')
wine_reviews.rename(columns={'points': 'rating'}, inplace=True)

# Use the below df for these problems:

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]



# Replace all the null 'price' values with the mean of the existing 


# Return a count of the null values in wine_ratings.


# Print out the number of rows in wine_ratings.


# Replace all the missing values in the 'country' column with 'Unknown'. Hint: Remember this should be the only column left with null values.


# Return a count of the null values in wine_ratings.


# Print out the number of rows in wine_ratings.



```


### P11.PY



```python
"""
Cleaning Data XI - Removing Duplicates
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')
wine_reviews.rename(columns={'points': 'rating'}, inplace=True)

# Using this DataFrame, drop the null values in the 'price' and 'country' columns. Then find the number of duplicates values in the 'title' column.

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]




# Now, drop the duplicate rows in the 'title' column.




# Print out these statements with the correct values for the blanks.


# _____ rows w. null values removed
# _____ duplicate rows removed
# _____ total rows removed
```


### P2.PY



```python
"""
Data Cleaning II - Rename Columns
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')

# Rename the 'designation' column to 'vineyard' and the 'points' column to 'rating'.

```


### P3.PY



```python
"""
Data Cleaning III - Bulk Replace in a Series
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')

# Using this Series, replace all instances of 'US' with 'DEMOCRATIC REPUBLIC OF CONGO'.

countries = wine_reviews['country']



# Again using the original Series, replace all instances of 'US' with 'FRENCH POLYNESIA' and all instances of 'Italy' with 'MADAGASCAR'.
```


### P4.PY



```python
"""
Data Cleaning IV - Bulk Replace in a Single DataFrame Column (Like a Series)
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')

# (Obviously, these changes are geographically incorrect and just for the sake of example.)

# Using this DataFrame, replace all instances of 'US' in the 'country' column with 'UNITED ARAB EMIRATES'.

wine_geography = wine_reviews.copy()[['variety', 'country', 'province']]



# Again using the original DataFrame, replace all instances of 'US' in the 'country' column with 'COSTA RICA' and all instances of 'Italy' in the 'country' column with 'UNITED ARAB EMIRATES'.




```


### P5.PY



```python
"""
Data Cleaning V - Bulk Replace in a Single DataFrame Column (Like a Dict)
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')

# (Obviously, these changes are geographically incorrect and just for the sake of example.)

# Using this DataFrame, replace all instances of 'US' in the 'country' column with 'CZECH REPUBLIC'.

wine_geography = wine_reviews.copy()[['variety', 'country', 'province']]



# Again using the original DataFrame, replace all instances of 'US' in the 'country' column with 'COSTA RICA' and all instances of 'Italy' with 'CZECH REPUBLIC'.
```


### P6.PY



```python
"""
Data Cleaning VI - Bulk Replace Across Multiple DataFrame Columns
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')

# (Obviously, these changes are geographically incorrect and just for the sake of example.)

# Using this DataFrame, replace all instances in the following columns according to the directions below. HINT: You should be able to do this in one function call!
## 'country' column
#### 'US' should become 'Morocco'
#### 'France' should become 'Mexico'
## 'province' column
#### 'Oregon' should become 'Ouezzane'
#### 'Michigan' should become 'Fahs-Anjra'
#### 'Sicily & Sardinia' should become 'Tuscany'

wine_geography = wine_reviews.copy()[['variety', 'country', 'province']]


```


### P7.PY



```python
"""
Cleaning Data VII - View Null Values
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')
wine_reviews.rename(columns={'points': 'rating'}, inplace=True)

# Use the below df for these problems:

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]



# Return a dataframe of booleans that show True for null values.



# Return a dataframe of booleans that show True for values that exist.

```


### P8.PY



```python
"""
Cleaning Data VIII - Find Null Values
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')
wine_reviews.rename(columns={'points': 'rating'}, inplace=True)

# Use the below df for these problems:

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]


# Return a count of the null values in wine_ratings.


# Print out the number of rows in wine_ratings.


```


### P9.PY



```python
"""
Cleaning Data IX - Drop Null Values
"""

import numpy as np
import pandas as pd
wine_reviews = pd.read_csv('../winemag-data-130k.csv')
wine_reviews.rename(columns={'points': 'rating'}, inplace=True)

# Use the below df for these problems:

wine_ratings = wine_reviews[['title', 'country', 'rating', 'price']]


# Drop the rows containing null values in any column.



# Return a count of the null values in wine_ratings.



# Print out the number of rows in wine_ratings.



```

