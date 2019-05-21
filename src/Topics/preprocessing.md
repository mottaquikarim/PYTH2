<!---
{"next": "Topics/eda.md","title": "Exploratory Data Analysis w. 🐼"}
-->

# Exploratory Data Analysis w/🐼🐼

For today's lesson, we will leverage Pandas for exploratory data analysis (EDA).
We will use Pandas to investigate, wrangle, munge, and clean our data.

In particular, we will examine how Pandas can be used to:

* **Investigate a dataset's integrity**
* **Filter, sort, and manipulate a DataFrame's series**

Additionally, the end portion of this section contains a glossary of methods and attributes provided by Pandas to handle data wrangling, selection, cleaning and organizing.

* **[Wrangling Data](preprocessing.md#wrangling-data)**
* **[Selecting Data](preprocessing.md#selecting-data)**
	* **[Single Values](preprocessing.md#single-values)**
	* **[Subsetting & Slicing](preprocessing.md#subsetting--slicing)**
* **[Cleaning & Organizing Data](preprocessing.md#cleaning--organizing-data)**
	* **[Editing](preprocessing.md#editing)**
	* **[Null Values](preprocessing.md#null-values)**
	* **[Duplicates](preprocessing.md#duplicates)**
	* **[Sorting](preprocessing.md#sorting)**

## Data sets

* **[Wine Reviews | Kaggle](https://www.kaggle.com/zynicide/wine-reviews/)**
	* *130k wine reviews with variety, location, winery, price, and description* 
* **[Wine Reviews | Local](https://raw.githubusercontent.com/mottaquikarim/PythonProgramming/master/raw_data/winemag-data-130k-v2.csv)**
	* *You can download a version of the kaggle dataset directly from this Github Repo* 
* **[Adventureworks Cycles | Local](https://raw.githubusercontent.com/mottaquikarim/PythonProgramming/master/raw_data/production.product.tsv)**
	* *You can download a version of the Adventureworks Cycles dataset directly from this Github Repo* 


## Adventureworks Cycles

Our core focus will be using a dataset developed by Microsoft for training purposes in SQL server, known the Adventureworks Cycles 2014OLTP Database.

* It is based on a fictitious company called Adventure Works Cycles (AWC), a multinational manufacturer and seller of bicycles and accessories.
* The company is based in Bothell, Washington, USA and has regional sales offices in several countries.
* We will be looking at a single table from this database, the Production.Product table, which outlines some of the products this company sells.

### Loading the Data

We can load our data as follows:

```python
import pandas as pd
import numpy as np

prod = pd.read_csv('/raw_data/production.product.tsv', sep='\t')

```

Note the `sep='\t'`; this is because we are pulling in a `tsv` file, which is basically a csv file but with `tabs` as delimiters vs commas.

**YOU DO**: Download the `tsv` file into your local machine, create a python virtualenv and run the code above, but on your machine.



### Data dictionary

Every good dataset has a **data dictionary**. Essentially, it lists each field in the data and provides a contextual description. It serves as a good frame of reference for anyone not diving directly into the data.


```python
cols = prod.columns
for idx, col in enumerate(cols):
  print(idx+1, col)
```

```text
    1 ProductID
    2 Name
    3 ProductNumber
    4 MakeFlag
    5 FinishedGoodsFlag
    6 Color
    7 SafetyStockLevel
    8 ReorderPoint
    9 StandardCost
    10 ListPrice
    11 Size
    12 SizeUnitMeasureCode
    13 WeightUnitMeasureCode
    14 Weight
    15 DaysToManufacture
    16 ProductLine
    17 Class
    18 Style
    19 ProductSubcategoryID
    20 ProductModelID
    21 SellStartDate
    22 SellEndDate
    23 DiscontinuedDate
    24 rowguid
    25 ModifiedDate
```



### Reading data

```python
prod.head(1)
```

The `head` method lets us read in the **first n rows** of a dataset. Run this in your machine, you should expect to see:


```text
   ProductID             Name ProductNumber  MakeFlag  ...  SellEndDate DiscontinuedDate                                 rowguid                   ModifiedDate
0          1  Adjustable Race       AR-5381         0  ...          NaN              NaN  {694215B7-08F7-4C0D-ACB1-D734BA44C0C8}  2014-02-08 10:01:36.827000000

[1 rows x 25 columns]
```

* **YOU DO**: Run the above code in *your* machine, but with **n=5**. What do you see?
* **YOU DO**: What kind of object is `prod`? Run `type(prod)` and report back your findings.
* **YOU DO**: What is the shape of this dataframe? Run `prod.shape` to find out.

## DataFrame subsets

This dataset is comprehensive! Let's see how we might be able to select a *subset* of this data for easier analysis.

Let's start with only 3 rows for now:

```python
prod_subset = prod.head(3)
```

```text
   ProductID             Name ProductNumber  MakeFlag  ...  SellEndDate DiscontinuedDate                                 rowguid                   ModifiedDate
0          1  Adjustable Race       AR-5381         0  ...          NaN              NaN  {694215B7-08F7-4C0D-ACB1-D734BA44C0C8}  2014-02-08 10:01:36.827000000
1          2     Bearing Ball       BA-8327         0  ...          NaN              NaN  {58AE3C20-4F3A-4749-A7D4-D568806CC537}  2014-02-08 10:01:36.827000000
2          3  BB Ball Bearing       BE-2349         1  ...          NaN              NaN  {9C21AED2-5BFA-4F18-BCB8-F11638DC2E4E}  2014-02-08 10:01:36.827000000

[3 rows x 25 columns]
```

If we wanted to only pull in a few **columns**, we could do something like:

```python
two_cols = prod_subset[['ProductID', 'Name']]
print(two_cols)
```

```text
   ProductID             Name
0          1  Adjustable Race
1          2     Bearing Ball
2          3  BB Ball Bearing
```

* **YOU DO**: Grab the first **5** rows of the dataset and save a subset df with the following columns: **ProductID**, **Name**, **Color**, and **ListPrice**.

## Column headers and datatypes

We can leverage pandas to explore the column header names and associated datatypes of the headers as well.

```python
print(prod.columns)
```

```text
Index(['ProductID', 'Name', 'ProductNumber', 'MakeFlag', 'FinishedGoodsFlag',
       'Color', 'SafetyStockLevel', 'ReorderPoint', 'StandardCost',
       'ListPrice', 'Size', 'SizeUnitMeasureCode', 'WeightUnitMeasureCode',
       'Weight', 'DaysToManufacture', 'ProductLine', 'Class', 'Style',
       'ProductSubcategoryID', 'ProductModelID', 'SellStartDate',
       'SellEndDate', 'DiscontinuedDate', 'rowguid', 'ModifiedDate'],
      dtype='object')
```

If we wanted to view the columns and their types, we can do:

```python
prod.dtypes
```

```text
ProductID                  int64
Name                      object
ProductNumber             object
MakeFlag                   int64
FinishedGoodsFlag          int64
Color                     object
SafetyStockLevel           int64
ReorderPoint               int64
StandardCost             float64
ListPrice                float64
Size                      object
SizeUnitMeasureCode       object
WeightUnitMeasureCode     object
Weight                   float64
DaysToManufacture          int64
ProductLine               object
Class                     object
Style                     object
ProductSubcategoryID     float64
ProductModelID           float64
SellStartDate             object
SellEndDate               object
DiscontinuedDate         float64
rowguid                   object
ModifiedDate              object
```

* **YOU DO**: What kind of python object is the `prod.dtypes`? How do you know?
* **YOU DO**: How does pandas know the col datatypes? Don't code this, but how might you implement this feature in pure python?

## Column Selection

**IMPORTANT**: depending on number of square brackets used, selection of a column may return a **Series** object or a **DataFrame** object. Depending on your usecase, you may *want* one or the other!

Consider the following:

```python
prod['Name'].head(3)
type(prod['Name'].head(3))
```

```text
0    Adjustable Race
1       Bearing Ball
2    BB Ball Bearing
Name: Name, dtype: object
<class 'pandas.core.series.Series'>
```

vs 

```python
prod[["Name"]].head(3)
type(prod[['Name']].head(3))
```
```text
              Name
0  Adjustable Race
1     Bearing Ball
2  BB Ball Bearing
<class 'pandas.core.frame.DataFrame'>
```

* **YOU DO**: Select **Name** and **ProductID** columns from our Dataframe. Is this possible to do as a **Series**? Why or why not?

## Renaming Columns

We can rename columns as needed, like so:

```python
new_prod = prod.rename(columns={'Name': 'ProductName', 'ProductNumber':'Number'}, inplace=False).head(3)
```

A few things to note here:

* `inplace`: this is a boolean that will update the **original** dataframe OR create us a new one
* `{'Name': 'ProductName'}`: we may use this as a way to map a new col name to an existing one

**REMEMBER**: we can view all the columns of a dataframe with:

```python
prod.columns
```

What is the datatype of this attribute?

```python
type(prod.columns)
```
```text
<class 'pandas.core.indexes.base.Index'>
```

The **Index** is an immutable ndarray implementing an ordered, sliceable set. It is the basic object storing axis labels for all pandas objects. Think of it as a 'row address' for your data frame (table). We can cast this `Index` to be something like, like say...a list.

```python
list(prod.columns)
```

Now, we can do something like:

```python
cols_list = list(prod.columns)
cols_list[0] = 'New Col'
prod.columns = cols_list
```

* **YOU DO**: What will the code above do? Run it and report back.
* **YOU DO**: Select the first three rows under `New Col` and return it as a **dataframe**.
* **YOU DO**: First, copy `prod` to `prod_cpy` (look at references below to see how to copy a dataframe). Then, rename the columns above, but **inplace** meaning `prod_cpy` itself must be mutated.

## Basic Stats on Columns

Five Number Summary (all assumes numeric data):
- **Min:** The smallest value in the column
- **Max:** The largest value in the column
- **Quartile:** A quartile is one fourth of our data
    - **First quartile:** This is the bottom most 25 percent
    - **Median:** The middle value. (Line all values biggest to smallest - median is the middle!) Also the 50th percentile
    - **Third quartile:** This the the top 75 percentile of our data

![](https://www.mathsisfun.com/data/images/quartiles-a.svg)

The `describe` method allows us to achieve this with pandas:

```python
# note - describe *default* only checks numeric datatypes
prod[['MakeFlag', 'SafetyStockLevel', 'StandardCost']].describe()
```

If we were to select cols as series, we could run additional **Series** object methods:

```python
# show the most popular product colors (aggregated by count, descending by default)
prod['Color'].value_counts()
```

```text
Black           93
Silver          43
Red             38
Yellow          36
Blue            26
Multi            8
Silver/Black     7
White            4
Grey             1
Name: Color, dtype: int64
```

* **YOU DO**: Leveraging the `unique` **Series** method, print out the unique colors for this product.
* **YOU DO**: Leveraging the `nunique` **Series** method, print out how many distinct colors are available.
* **YOU DO**: Leveraging the `dropna` keyword arg of the `nunique` **Series** method, print out how many distinct colors are available *including* **NULL** values.

## Filtering

Filtering and sorting are key processes that allow us to drill into the 'nitty gritty' and cross sections of our dataset.

To filter, we use a process called **Boolean Filtering**, wherein we define a Boolean condition, and use that Boolean condition to filer on our DataFrame.

Recall: our given dataset has a column `Color`. Let's see if we can find all products that are `Black`. Let's take a look at the first 10 rows of the dataframe to see how it looks as-is:

```python
colors = prod['Color'].head(10)
```
```text
ProductID
1         NaN
2         NaN
3         NaN
4         NaN
316       NaN
317     Black
318     Black
319     Black
320    Silver
321    Silver
Name: Color, dtype: object
```

To find only the "Black" colored items, we can:

```python
prod['Color'].head(10) == 'Black'
```
```text
ProductID
1      False
2      False
3      False
4      False
316    False
317     True
318     True
319     True
320    False
321    False
Name: Color, dtype: bool
```

* **YOU DO**: Without using the `unique`/`nunique` methods from above, can you apply an additional filter to the series above to determine how many `Black` colored products exist?

We can apply this filtering to our Dataframes as well, in a more interesting manner:

```python
prod[prod['Color'] == 'Black'].head(3)
```
```text
   ProductID         Name ProductNumber  MakeFlag  ...  SellEndDate DiscontinuedDate                                 rowguid                   ModifiedDate
5        317  LL Crankarm       CA-5965         0  ...          NaN              NaN  {3C9D10B7-A6B2-4774-9963-C19DCEE72FEA}  2014-02-08 10:01:36.827000000
6        318  ML Crankarm       CA-6738         0  ...          NaN              NaN  {EABB9A92-FA07-4EAB-8955-F0517B4A4CA7}  2014-02-08 10:01:36.827000000
7        319  HL Crankarm       CA-7457         0  ...          NaN              NaN  {7D3FD384-4F29-484B-86FA-4206E276FE58}  2014-02-08 10:01:36.827000000

[3 rows x 25 columns]
```

* **YOU DO**: Slice the dataframe above and select only the `Color` column - is there any non `black` color items?
* **YOU DO**: calculate the average **ListPrice** for the salable products (**hint**: use the `FinishedGoodsFlag` column to determine "salability") using the **Series**.`mean()` method
* **YOU DO**: calculate the above again, but this time use `describe` and pull the `mean` from there.

## Compound Filtering

Let's filter on _multiple conditions_. Before, we filtered on rows where `Color` was `Black`. We also filtered where `FinishedGoodsFlag` was equal to `1`. Let's see what happens when we filter on *both* simultaneously. 

The format for multiple conditions is:

`df[ (df['col1'] == value1) & (df['col2'] == value2) ]`

Or, more simply:

`df[ (CONDITION 1) & (CONDITION 2) ]`

Which eventually may evaluate to something like:

`df[ True & False ]`

...on a row-by-row basis. If the end result is `False`, the row is omitted.

**Don't forget parentheses in your conditions!!** This is a common mistake.

```python
prod[ (prod['Color'] == 'Black') & (prod['FinishedGoodsFlag'] == 1) ].head(3)
```
```text
     ProductID                       Name ProductNumber  MakeFlag  ...  SellEndDate DiscontinuedDate                                 rowguid                   ModifiedDate
209        680  HL Road Frame - Black, 58    FR-R92B-58         1  ...          NaN              NaN  {43DD68D6-14A4-461F-9069-55309D90EA7E}  2014-02-08 10:01:36.827000000
212        708    Sport-100 Helmet, Black       HL-U509         0  ...          NaN              NaN  {A25A44FB-C2DE-4268-958F-110B8D7621E2}  2014-02-08 10:01:36.827000000
226        722  LL Road Frame - Black, 58    FR-R38B-58         1  ...          NaN              NaN  {2140F256-F705-4D67-975D-32DE03265838}  2014-02-08 10:01:36.827000000

[3 rows x 25 columns]
```

Another example:

```python
# Here we have an example of a list price of greater than 50, 
# OR a product size that is not equal to 'XL'

prod[ (prod['ListPrice'] > 50) | (prod['Size'] != 'XL') ].head(3)
```
```text
   ProductID             Name ProductNumber  MakeFlag  ...  SellEndDate DiscontinuedDate                                 rowguid                   ModifiedDate
0          1  Adjustable Race       AR-5381         0  ...          NaN              NaN  {694215B7-08F7-4C0D-ACB1-D734BA44C0C8}  2014-02-08 10:01:36.827000000
1          2     Bearing Ball       BA-8327         0  ...          NaN              NaN  {58AE3C20-4F3A-4749-A7D4-D568806CC537}  2014-02-08 10:01:36.827000000
2          3  BB Ball Bearing       BE-2349         1  ...          NaN              NaN  {9C21AED2-5BFA-4F18-BCB8-F11638DC2E4E}  2014-02-08 10:01:36.827000000

[3 rows x 25 columns]
```

* **YOU DO**: Find all rows that have a **NULL** dataframe and is **NOT** finished. **HINT**: use `pd.isna`

## Sorting

Here's how we can sort a dataframe

```python
prod.sort_values(by='StandardCost', ascending=False).head(3)
```

```text
     ProductID              Name ProductNumber  MakeFlag  ...          SellEndDate DiscontinuedDate                                 rowguid                   ModifiedDate
253        749  Road-150 Red, 62    BK-R93R-62         1  ...  2012-05-29 00:00:00              NaN  {BC621E1F-2553-4FDC-B22E-5E44A9003569}  2014-02-08 10:01:36.827000000
254        750  Road-150 Red, 44    BK-R93R-44         1  ...  2012-05-29 00:00:00              NaN  {C19E1136-5DA4-4B40-8758-54A85D7EA494}  2014-02-08 10:01:36.827000000
255        751  Road-150 Red, 48    BK-R93R-48         1  ...  2012-05-29 00:00:00              NaN  {D10B7CC1-455E-435B-A08F-EC5B1C5776E9}  2014-02-08 10:01:36.827000000

[3 rows x 25 columns]
```

This one is a little more advanced, but it demonstrates a few things:
- Conversion of a `numpy.ndarray` object (return type of `pd.Series.unique()`) into a `pd.Series` object
- `pd.Series.sort_values` with the `by=` kwarg omitted (if only one column is the operand, `by=` doesn't need specified
- Alphabetical sort of a string field, `ascending=True` means A->Z
- Inclusion of nulls, `NaN` in a string field (versus omission with a float/int as prior example)

```python
pd.Series(prod['Color'].unique()).sort_values(ascending=True)
```

```text
1           Black
5            Blue
8            Grey
6           Multi
3             Red
2          Silver
9    Silver/Black
4           White
7          Yellow
0             NaN
dtype: object
```

## A few final YOU DOs

* **YOU DO**: Create a variable called `rows` and a variable called `cols`. Store the num rows and cols in dataframe into these variables, respectively
* **YOU DO**: Print out the number of unique product lines that exist in this data set
* **YOU DO**: Print out the values of these product lines, **DROP NULLS**
* **YOU DO**: Using `shape` and a dataframe filter, print out how many `R` productlines exist.
* **Challenge**: What are the top 3 most expensive list price product that are either in the Women's Mountain category, OR Silver in Color? Return your answer as a DataFrame object, with NewName relabeled as Name, and ListPrice columns. Perform the statement in one execution, and do not mutate the source DataFrame.

## Recap

```python

# basic DataFrame operations
df.head()
df.tail()
df.shape
df.columns
df.Index

# selecting columns
df.column_name
df['column_name']

# renaming columns
df.rename({'old_name':'new_name'}, inplace=True)
df.columns = ['new_column_a', 'new_column_b']

# notable columns operations
df.describe() # five number summary
df['col1'].nunique() # number of unique values
df['col1'].value_counts() # number of occurrences of each value in column

# filtering
df[ df['col1'] < 50 ] # filter column to be less than 50
df[ (df['col1'] == value1) & (df['col2'] > value2) ] # filter column where col1 is equal to value1 AND col2 is greater to value 2

# sorting
df.sort_values(by='column_name', ascending = False) # sort biggest to smallest

```


🐼 🐼 🐼

## DataFrame Reference

Please find below a list of useful dataframe properties and methods for use in your exploratory data analysis practice.

## Wrangling Data

Given the following dataset:

```python
wine_reviews = pd.read_csv('raw_data/winemag-data-130k.csv')
```

After your initial import of some dataset, you'll want to do a gut check to make sure everything is in place. Here are the kind of very basic properties you might want to check:

* `df.info()` -- returns index, datatype and memory information
* `df.shape` -- returns the number of rows and columns in a data frame
* `len(obj)` -- returns # of rows in the object data (*S & df)
* `obj.size` -- returns # of elements in the object (*S & df)
* `df.index` -- returns index of the rows specifically (*S & df)
* `df.columns` -- returns the column labels of the DataFrame.
* `df.head(n)` -- returns last n rows of a data frame
* `df.tail(n)` -- returns last n rows of a data frame
* `copy(obj)` -- create a deep copy of the object (*S & df)
* `obj.empty` -- returns booleans for whether object is empty or not

## Selecting Data

#### Single Values

* `df.loc[row_label, col_label]` -- select a single item in a DataFrame by its row and column labels
* `df.loc[start_row_label : end_row_label, start_col_label : end_col_label]` -- select a slice of a DataFrame by starting and ending row/column labels
* `df.iloc[row_index,:]` -- select a row in a DataFrame by index position
* `s.iloc[index]` -- select a single item by its position
* `s.loc[index]` -- select a slice of items from a Series

#### Subsetting & Slicing

* `obj.get(key)` -- returns an item from an object (e.g. a column from a DataFrame, a value from a Series, etc.)
* `df[col]` -- select and name a column and return it as a Series
* `df.loc[label1, label2, ...]` -- select one or more rows or columns in a DataFrame by its label
* `df[[col1, col2]]` -- select and name multiple columns and return them as a new data frame
* `df.nlargest(n, key)` -- Select and order top n entries.
* `df.nsmallest(n, key)` -- Select and order bottom n entries
* `obj.where(cond, other = NaN, inplace = False, axis = None)` -- replace values in the object where the condition is False (*S or df*)
* `df.iloc[row_index, col_index]` -- select a single item in a DataFrame by the index position of its row and col
* `df.iloc[start_index : end_index, start_index : end_index]` -- select a slice of a DataFrame by starting and ending index row/column positions; (ending index stop at index before it)

## Cleaning & Organizing Data

#### Editing Existing Data

* `obj.truncate([before, after, axis)` -- truncate an object before and after some index value (*S & df*)
* `df.drop(columns=[col1, col2, ...])` -- drops specified columns from the dataframe
* `s.replace(1,'one')` -- replace all values equal to 1 with 'one'
* `s.replace([1,3],['one','three'])` -- replace all values equal to 1 with 'one' and all values equal to 3 with 'three'
* `df.rename(columns={'old_name': 'new_ name'})` -- rename specific columns
* `df.set_index(keys)` -- change the index of the data frame
* `df.reset_index(keys)` -- Reset index of DataFrame to row numbers, moving
index to columns.
* `shift([periods, freq, axis, fill_value])` -- Shift index by desired number of periods with an optional time freq.
* `df.set_axis(labels)`

#### Null Values

* `pd.isnull()` -- checks for null (NaN values in the data and returns an array of booleans, where "True" means missing and "False" means present
* `pd.notnull()` -- returns all values that are NOT null
* `pd.isnull().sum()` -- returns a count of null (NaN)
* `df.dropna()` -- Drops all rows that contain null values and returns a new df
* `df.dropna(axis=1)` -- Drops all columns that contain null values and returns a new df
* `df.dropna(subset=[col1])` -- Drops all rows that contain null values in one or more specific columns and returns a new df
* `df.fillna(value=x)` —- replace all missing values with some value `x` (*S & df*)
* `s.fillna(s.mean())` -- Replaces all null values with the mean (mean can be replaced with almost any function from the statistics section)

#### Duplicate Values

* `df.duplicated([subset, keep])` -- Rrturn boolean Series denoting duplicate rows; can choose to consider a subset of columns
* `drop_duplicates([subset, keep, inplace])` -- returns DataFrame with duplicate rows removed, optionally only considering certain columns.

#### Sorting

* `df.transform(func[, axis])` -- return DataFrame with transformed values
* `df.transpose(*args, **kwargs)` -- transpose rows and columns
* `df.sort_values(col1)` -- sort values in a certain column in *ascending* order
* `df.sort_index(axis=1)` -- sort axis values by index in *ascending* order
* `df.sort_values(col2,ascending=False)` -- sort values in a certain column in *descending* order
* `df.sort_index(axis=1, ascending=False)` -- sort axis values by index in *descending* order
* `df.sort_values([col1,col2],ascending=[True,False])` -- sort values in a col1 in *ascending* order, then sort values in col2 in *descending* order

