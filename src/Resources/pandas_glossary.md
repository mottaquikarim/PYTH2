<!---
{"next":"Resources/genref.md","title":"Pandas Glossary"}
-->

# Pandas Glossary

<img src="https://news.nationalgeographic.com/content/dam/news/2015/12/15/pandas/01pandainsemination.ngsversion.1450209600474.adapt.1900.1.jpg" style="margin: 0 auto; width: 50%; display: block;"/>

## Reading & Writing Data

* `pd.read_csv(filename)` -- From a CSV file
* `pd.read_table(filename)` -- From a delimited text file (like TSV)
* `pd.read_excel(filename)` -- From an Excel file
* `pd.read_sql(query, connection_object)` -- Reads from a SQL table/database
* `pd.read_json(json_string)` -- Reads from a JSON formatted string, URL or file.
* `pd.read_html(url)` -- Parses an html URL, string or file and extracts tables to a list of dataframes
* `pd.read_clipboard()` -- Takes the contents of your clipboard and passes it to read_table()
* `pd.DataFrame(dict)` -- From a dict, keys for columns names, values for data as lists
* `df.to_csv(filename)` -- Writes to a CSV file
* `df.to_excel(filename)` -- Writes to an Excel file
* `df.to_sql(table_name, connection_object)` -- Writes to a SQL table
* `df.to_json(filename)` -- Writes to a file in JSON format
* `df.to_html(filename)` -- Saves as an HTML table
* `df.to_clipboard()` -- Writes to the clipboard

## Data Wrangling (Selecting)

* `obj.get(key)` -- returns an item from an object (e.g. a column from a DataFrame, a value from a Series, etc.)
* `df[col]` -- select and name a column and return it as a Series
* `df.loc[label1, label2, ...]` -- select one or more rows or columns in a DataFrame by its label
* `df.loc[row_label, col_label]` -- select a single item in a DataFrame by its row and column labels
* `df.loc[start_row_label : end_row_label, start_col_label : end_col_label]` -- select a slice of a DataFrame by starting and ending row/column labels
* `df.iloc[row_index,:]` -- select a row in a DataFrame by index position
* `df.iloc[row_index, col_index]` -- select a single item in a DataFrame by the index position of its row and col
* `df.iloc[start_index : end_index, start_index : end_index]` -- select a slice of a DataFrame by starting and ending index row/column positions; (ending index stop at index before it)
* `s.iloc[index]` -- select a single item by its position
* `s.loc[index]` -- select a slice of items from a Series
* `df[[col1, col2]]` -- select and name multiple columns and return them as a new data frame
* `df.nlargest(n, 'value')` -- Select and order top n entries.
* `df.nsmallest(n, 'value')` -- Select and order bottom n entries
* `obj.truncate([before, after, axis)` -- Truncate an object before and after some index value (*S & df)
* `obj.where(cond, other = NaN, inplace = False, axis = None)` -- replace values in the object where the condition is False


## Data Cleaning

* `pd.isnull()` -- checks for null values in the data and returns an array of booleans, where "True" means missing and "False" means present
* `pd.notnull()` -- returns all values that are NOT null
* `df.dropna()` -- remove all missing values
* `df.fillna(x)` —- replace all missing values with some value "x"
* `s.replace(1,'one')` -- replace all values equal to 1 with 'one'
* `s.replace([1,3],['one','three'])` -- replace all values equal to 1 with 'one' and all values equal to 3 with 'three'
* `df.rename(columns={'old_name': 'new_ name'})` -- rename specific columns
* `df.set_index('column_one')` -- change the index of the data frame
* `df.columns` = ['a','b','c'] -- Renames columns
* `pd.isnull()` -- Checks for null Values, Returns Boolean Array
* `pd.notnull()` -- Opposite of s.isnull()
* `df.dropna()` -- Drops all rows that contain null values
* `df.dropna(axis=1)` -- Drops all columns that contain null values
* `df.dropna(axis=1,thresh=n)` -- Drops all rows have have less than n non null values
* `df.fillna(x)` -- Replaces all null values with x
* `s.fillna(s.mean())` -- Replaces all null values with the mean (mean can be replaced with almost any function from the statistics section)
* `df.duplicated([subset, keep])` -- Rrturn boolean Series denoting duplicate rows; can choose to consider a subset of columns
* `drop_duplicates([subset, keep, inplace])` -- returns DataFrame with duplicate rows removed, optionally only considering certain columns.
* `s.replace(1,'one')` -- Replaces all values equal to 1 with 'one'
* `s.replace([1,3],['one','three'])` -- Replaces all 1 with 'one' and 3 with 'three'
* `df.rename(columns=lambda x: x + 1)` -- Mass renaming of columns
* `df.rename(columns={'old_name': 'new_ name'}) -- Selective renaming
* `df.set_index('column_one')` -- Changes the index
* `df.rename(index=lambda x: x + 1)` -- Mass renaming of index

## Exploring Data

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
* `describe()` -- returns basic summary statistics (e.g. count, mean, std, min, quartiles, & max)
* `df.count()` -- returns number of non-null values in each data frame column
* `value_counts()` -- returns count of each category in a categorical attributed series of values
* `df.mean()` -- returns mean of all columns
* `df.median()` -- returns median of each column
* `df.min()` -- returns lowest value in each column
* `df.max()` -- returns highest value in each column
* `quantile(x)` -- quantile
* `cumsum()` -- cummulative sum
* `comprod()` -- cumulative product
* `cummin()` -- cumulative minimum
* `var()` -- returns the variance among values in **each** column
* `df.std()` -- returns standard deviation of each column
* `cov()` -- covariance
* `mad()` -- mean absolute variation
* `skew()` -- skewness of distribution
* `sem()` -- unbiased standard error of the mean
* `kurt()` -- kurtosis
* `corr()` -- returns the Pearson correlation coefficent between columns in a data frame
* `autocorr()` -- auto-correlation
* `diff()` -- first discrete difference

## Organizating Data

* `df1.append(df2)` -- add the rows in df1 to the end of df2 (columns should be identical)
* `df.concat([df1, df2],axis=1)` —- add the columns in df1 to the end of df2 (rows should be identical)
* `df1.join(df2,on=col1,how='inner')` —- SQL-style join the columns in df1 with the columns on df2 where the rows for colhave identical values. how can be equal to one of: 'left', 'right', 'outer', 'inner'
* `df.sort_values(col1)` -- sort values in a certain column in *ascending* order
* `df.sort_values(col2,ascending=False)` -- sort values in a certain column in *descending* order
* `df.sort_values([col1,col2],ascending=[True,False])` -- sort values in a col1 in *asscending* order, then sort values in col2 in *descending* order
* `df[df[col] > 0.5]` # Rows where the col column is greater than 0.5
* `df[(df[col] > 0.5) & (df[col] < 0.7)]` # Rows where 0.5 < col < 0.7
* `df.groupby(col)` -- returns groupby object for values from a single, specific column
* `df.groupby([col1,col2])` -- returns a `groupby` object for values from multiple columns, which you can specify
* `df.groupby(col1)[col2].mean()` # Returns the mean of the values in col2, grouped by the values in col1 (mean can be replaced with almost any function from the statistics section)
* `df.pivot_table(index=col1, values= col2,col3], aggfunc=mean)` # Creates a pivot table that groups by col1 and calculates the mean of col2 and col3
* `df.groupby(col1).agg(np.mean)` # Finds the average across all columns for every unique column 1 group
* `df.apply(np.<function>)` # Applies a function across each column
* `df.apply(np.<function>, axis=1)` # Applies a function across each row



#### Sources
* [Pandas Docs](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
