
# Data Pre-Processing with Pandas

In this section, our core focus will be using a dataset developed by Microsoft for training purposes in SQL server, known the Adventureworks Cycles 2014OLTP Database.

* It is based on a fictitious company called Adventure Works Cycles (AWC), a multinational manufacturer and seller of bicycles and accessories.
* The company is based in Bothell, Washington, USA and has regional sales offices in several countries.
* We will be looking at a single table from this database, the Production.Product table, which outlines some of the products this company sells.


We will examine this table to earn how to wrangle and clean Pandas data structures. At a high-level, this lesson will cover:

<!--
* **[Adventure Works Cycles Data Dictionary](preprocessing.md#wine-review-data-dictionary)**
* **[Wrangling Data](preprocessing.md#wrangling-data)**
* **[Selecting Data](preprocessing.md#selecting-data)**
	* **[Single Values](preprocessing.md#single-values)**
	* **[Subsetting & Slicing](preprocessing.md#subsetting--slicing)**
* **[Cleaning & Organizing Data](preprocessing.md#cleaning--organizing-data)**
	* **[Editing](preprocessing.md#editing)**
	* **[Null Values](preprocessing.md#null-values)**
	* **[Duplicates](preprocessing.md#duplicates)**
	* **[Sorting](preprocessing.md#sorting)**
-->

## Data Dictionary




```
import pandas as pd
import numpy as np

from google.colab import drive
drive.mount('/content/gdrive')
```

    Drive already mounted at /content/gdrive; to attempt to forcibly remount, call drive.mount("/content/gdrive", force_remount=True).



```
ad_cycle = pd.read_csv('/content/gdrive/My Drive/PyDev/raw_data/production.product.tsv', sep='\t')
```


Every good dataset has a **data dictionary**. Essentially, it lists each field in the data and provides a contextual description. It serves as a good frame of reference for anyone not diving directly into the data.


```
cols = ad_cycle.columns
for idx, col in enumerate(cols):
  print(idx+1, col)
```

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


## Wrangling Data

After your initial import of some dataset, you'll want to do a gut check to make sure everything is in place. Here are the kind of very basic properties you might want to check:

### `df.info()` -- returns index, datatype and memory information


```
ad_cycle.info() # this will simply output whatever is returned by calling the `info` method on ad_cycle
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 504 entries, 0 to 503
    Data columns (total 25 columns):
    ProductID                504 non-null int64
    Name                     504 non-null object
    ProductNumber            504 non-null object
    MakeFlag                 504 non-null int64
    FinishedGoodsFlag        504 non-null int64
    Color                    256 non-null object
    SafetyStockLevel         504 non-null int64
    ReorderPoint             504 non-null int64
    StandardCost             504 non-null float64
    ListPrice                504 non-null float64
    Size                     211 non-null object
    SizeUnitMeasureCode      176 non-null object
    WeightUnitMeasureCode    205 non-null object
    Weight                   205 non-null float64
    DaysToManufacture        504 non-null int64
    ProductLine              278 non-null object
    Class                    247 non-null object
    Style                    211 non-null object
    ProductSubcategoryID     295 non-null float64
    ProductModelID           295 non-null float64
    SellStartDate            504 non-null object
    SellEndDate              98 non-null object
    DiscontinuedDate         0 non-null float64
    rowguid                  504 non-null object
    ModifiedDate             504 non-null object
    dtypes: float64(6), int64(6), object(13)
    memory usage: 98.5+ KB


### `df.shape` -- returns the number of rows and columns in a data frame



```
ad_cycle.shape
```




    (504, 25)



### `len(obj)` -- returns # of rows in the object data (*S & df)



```
len(ad_cycle)
```




    504



### `obj.size` -- returns # of elements in the object (*S & df)



```
ad_cycle.size
```




    12600



### `df.index` -- returns index of the rows specifically (*S & df)



```
ad_cycle.index
```




    RangeIndex(start=0, stop=504, step=1)



### `df.columns` -- returns the column labels of the DataFrame.



```
ad_cycle.columns
```




    Index(['ProductID', 'Name', 'ProductNumber', 'MakeFlag', 'FinishedGoodsFlag',
           'Color', 'SafetyStockLevel', 'ReorderPoint', 'StandardCost',
           'ListPrice', 'Size', 'SizeUnitMeasureCode', 'WeightUnitMeasureCode',
           'Weight', 'DaysToManufacture', 'ProductLine', 'Class', 'Style',
           'ProductSubcategoryID', 'ProductModelID', 'SellStartDate',
           'SellEndDate', 'DiscontinuedDate', 'rowguid', 'ModifiedDate'],
          dtype='object')



### `df.head(n)` -- returns last n rows of a data frame



```
ad_cycle.head() # n is 5 by default
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ProductID</th>
      <th>Name</th>
      <th>ProductNumber</th>
      <th>MakeFlag</th>
      <th>FinishedGoodsFlag</th>
      <th>Color</th>
      <th>SafetyStockLevel</th>
      <th>ReorderPoint</th>
      <th>StandardCost</th>
      <th>ListPrice</th>
      <th>...</th>
      <th>ProductLine</th>
      <th>Class</th>
      <th>Style</th>
      <th>ProductSubcategoryID</th>
      <th>ProductModelID</th>
      <th>SellStartDate</th>
      <th>SellEndDate</th>
      <th>DiscontinuedDate</th>
      <th>rowguid</th>
      <th>ModifiedDate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Adjustable Race</td>
      <td>AR-5381</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{694215B7-08F7-4C0D-ACB1-D734BA44C0C8}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Bearing Ball</td>
      <td>BA-8327</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{58AE3C20-4F3A-4749-A7D4-D568806CC537}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>BB Ball Bearing</td>
      <td>BE-2349</td>
      <td>1</td>
      <td>0</td>
      <td>NaN</td>
      <td>800</td>
      <td>600</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{9C21AED2-5BFA-4F18-BCB8-F11638DC2E4E}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Headset Ball Bearings</td>
      <td>BE-2908</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>800</td>
      <td>600</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{ECFED6CB-51FF-49B5-B06C-7D8AC834DB8B}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>316</td>
      <td>Blade</td>
      <td>BL-2036</td>
      <td>1</td>
      <td>0</td>
      <td>NaN</td>
      <td>800</td>
      <td>600</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{E73E9750-603B-4131-89F5-3DD15ED5FF80}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 25 columns</p>
</div>



### `df.tail(n)` -- returns last n rows of a data frame


```
ad_cycle.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ProductID</th>
      <th>Name</th>
      <th>ProductNumber</th>
      <th>MakeFlag</th>
      <th>FinishedGoodsFlag</th>
      <th>Color</th>
      <th>SafetyStockLevel</th>
      <th>ReorderPoint</th>
      <th>StandardCost</th>
      <th>ListPrice</th>
      <th>...</th>
      <th>ProductLine</th>
      <th>Class</th>
      <th>Style</th>
      <th>ProductSubcategoryID</th>
      <th>ProductModelID</th>
      <th>SellStartDate</th>
      <th>SellEndDate</th>
      <th>DiscontinuedDate</th>
      <th>rowguid</th>
      <th>ModifiedDate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>499</th>
      <td>995</td>
      <td>ML Bottom Bracket</td>
      <td>BB-8107</td>
      <td>1</td>
      <td>1</td>
      <td>NaN</td>
      <td>500</td>
      <td>375</td>
      <td>44.9506</td>
      <td>101.24</td>
      <td>...</td>
      <td>NaN</td>
      <td>M</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>96.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{71AB847F-D091-42D6-B735-7B0C2D82FC84}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>500</th>
      <td>996</td>
      <td>HL Bottom Bracket</td>
      <td>BB-9108</td>
      <td>1</td>
      <td>1</td>
      <td>NaN</td>
      <td>500</td>
      <td>375</td>
      <td>53.9416</td>
      <td>121.49</td>
      <td>...</td>
      <td>NaN</td>
      <td>H</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>97.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{230C47C5-08B2-4CE3-B706-69C0BDD62965}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>501</th>
      <td>997</td>
      <td>Road-750 Black, 44</td>
      <td>BK-R19B-44</td>
      <td>1</td>
      <td>1</td>
      <td>Black</td>
      <td>100</td>
      <td>75</td>
      <td>343.6496</td>
      <td>539.99</td>
      <td>...</td>
      <td>R</td>
      <td>L</td>
      <td>U</td>
      <td>2.0</td>
      <td>31.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{44CE4802-409F-43AB-9B27-CA53421805BE}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>502</th>
      <td>998</td>
      <td>Road-750 Black, 48</td>
      <td>BK-R19B-48</td>
      <td>1</td>
      <td>1</td>
      <td>Black</td>
      <td>100</td>
      <td>75</td>
      <td>343.6496</td>
      <td>539.99</td>
      <td>...</td>
      <td>R</td>
      <td>L</td>
      <td>U</td>
      <td>2.0</td>
      <td>31.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{3DE9A212-1D49-40B6-B10A-F564D981DBDE}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>503</th>
      <td>999</td>
      <td>Road-750 Black, 52</td>
      <td>BK-R19B-52</td>
      <td>1</td>
      <td>1</td>
      <td>Black</td>
      <td>100</td>
      <td>75</td>
      <td>343.6496</td>
      <td>539.99</td>
      <td>...</td>
      <td>R</td>
      <td>L</td>
      <td>U</td>
      <td>2.0</td>
      <td>31.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{AE638923-2B67-4679-B90E-ABBAB17DCA31}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 25 columns</p>
</div>



### `df.copy()` -- create a deep copy of the object (*S & df)



```
ad_cycle.copy()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ProductID</th>
      <th>Name</th>
      <th>ProductNumber</th>
      <th>MakeFlag</th>
      <th>FinishedGoodsFlag</th>
      <th>Color</th>
      <th>SafetyStockLevel</th>
      <th>ReorderPoint</th>
      <th>StandardCost</th>
      <th>ListPrice</th>
      <th>...</th>
      <th>ProductLine</th>
      <th>Class</th>
      <th>Style</th>
      <th>ProductSubcategoryID</th>
      <th>ProductModelID</th>
      <th>SellStartDate</th>
      <th>SellEndDate</th>
      <th>DiscontinuedDate</th>
      <th>rowguid</th>
      <th>ModifiedDate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Adjustable Race</td>
      <td>AR-5381</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{694215B7-08F7-4C0D-ACB1-D734BA44C0C8}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Bearing Ball</td>
      <td>BA-8327</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{58AE3C20-4F3A-4749-A7D4-D568806CC537}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>BB Ball Bearing</td>
      <td>BE-2349</td>
      <td>1</td>
      <td>0</td>
      <td>NaN</td>
      <td>800</td>
      <td>600</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{9C21AED2-5BFA-4F18-BCB8-F11638DC2E4E}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Headset Ball Bearings</td>
      <td>BE-2908</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>800</td>
      <td>600</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{ECFED6CB-51FF-49B5-B06C-7D8AC834DB8B}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>316</td>
      <td>Blade</td>
      <td>BL-2036</td>
      <td>1</td>
      <td>0</td>
      <td>NaN</td>
      <td>800</td>
      <td>600</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{E73E9750-603B-4131-89F5-3DD15ED5FF80}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>317</td>
      <td>LL Crankarm</td>
      <td>CA-5965</td>
      <td>0</td>
      <td>0</td>
      <td>Black</td>
      <td>500</td>
      <td>375</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>L</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{3C9D10B7-A6B2-4774-9963-C19DCEE72FEA}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>318</td>
      <td>ML Crankarm</td>
      <td>CA-6738</td>
      <td>0</td>
      <td>0</td>
      <td>Black</td>
      <td>500</td>
      <td>375</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>M</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{EABB9A92-FA07-4EAB-8955-F0517B4A4CA7}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>319</td>
      <td>HL Crankarm</td>
      <td>CA-7457</td>
      <td>0</td>
      <td>0</td>
      <td>Black</td>
      <td>500</td>
      <td>375</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{7D3FD384-4F29-484B-86FA-4206E276FE58}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>320</td>
      <td>Chainring Bolts</td>
      <td>CB-2903</td>
      <td>0</td>
      <td>0</td>
      <td>Silver</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{7BE38E48-B7D6-4486-888E-F53C26735101}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>321</td>
      <td>Chainring Nut</td>
      <td>CN-6137</td>
      <td>0</td>
      <td>0</td>
      <td>Silver</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{3314B1D7-EF69-4431-B6DD-DC75268BD5DF}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>322</td>
      <td>Chainring</td>
      <td>CR-7833</td>
      <td>0</td>
      <td>0</td>
      <td>Black</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{F0AC2C4D-1A1F-4E3C-B4D9-68AEA0EC1CE4}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>11</th>
      <td>323</td>
      <td>Crown Race</td>
      <td>CR-9981</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{51A32CA6-65A1-4C31-AF2B-D9E4F5D631D4}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>324</td>
      <td>Chain Stays</td>
      <td>CS-2812</td>
      <td>1</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{FE0678ED-AEF2-4C58-A450-8151CC24DDD8}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>325</td>
      <td>Decal 1</td>
      <td>DC-8732</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{05CE123C-A402-478E-AE9B-75D7727AEAAD}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>326</td>
      <td>Decal 2</td>
      <td>DC-9824</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{A56851F9-1CD7-4E2F-8779-2E773E1B5209}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>327</td>
      <td>Down Tube</td>
      <td>DT-2377</td>
      <td>1</td>
      <td>0</td>
      <td>NaN</td>
      <td>800</td>
      <td>600</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{1DAD47DD-E259-42B8-B8B4-15A0B7D21B2F}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>16</th>
      <td>328</td>
      <td>Mountain End Caps</td>
      <td>EC-M092</td>
      <td>1</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{6070B1EA-59B7-4F8B-950F-2BE07D00449D}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>17</th>
      <td>329</td>
      <td>Road End Caps</td>
      <td>EC-R098</td>
      <td>1</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{88399D13-719E-4545-81D6-F0650F372FA2}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>18</th>
      <td>330</td>
      <td>Touring End Caps</td>
      <td>EC-T209</td>
      <td>1</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{6903CE24-D0CE-4191-9198-4231DE37A929}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>19</th>
      <td>331</td>
      <td>Fork End</td>
      <td>FE-3760</td>
      <td>1</td>
      <td>0</td>
      <td>NaN</td>
      <td>800</td>
      <td>600</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{C91D602E-DA52-43D2-BD7E-EB110A9392B9}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>332</td>
      <td>Freewheel</td>
      <td>FH-2981</td>
      <td>0</td>
      <td>0</td>
      <td>Silver</td>
      <td>500</td>
      <td>375</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{D864879A-E8B1-4F7B-BAFA-1F136089C2C8}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>21</th>
      <td>341</td>
      <td>Flat Washer 1</td>
      <td>FW-1000</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{A3F2FA3A-22E1-43D8-A131-A9B89C32D8EA}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>22</th>
      <td>342</td>
      <td>Flat Washer 6</td>
      <td>FW-1200</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{331ADDEC-E9B9-4A7E-9324-42069C2DCDC4}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>23</th>
      <td>343</td>
      <td>Flat Washer 2</td>
      <td>FW-1400</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{84A3473E-AE26-4A21-81B9-60BB418A79B2}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>24</th>
      <td>344</td>
      <td>Flat Washer 9</td>
      <td>FW-3400</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{0AE4CE60-5242-48F5-ADA1-3013FF45F969}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>25</th>
      <td>345</td>
      <td>Flat Washer 4</td>
      <td>FW-3800</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{2C1C58B4-234C-4B3A-8C8E-84524AC05EEA}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>26</th>
      <td>346</td>
      <td>Flat Washer 3</td>
      <td>FW-5160</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{590C2C3F-A8B6-42B5-9412-D655E37F0EAE}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>27</th>
      <td>347</td>
      <td>Flat Washer 8</td>
      <td>FW-5800</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{1B73F5FE-AB85-49FC-99AD-0500CEBDA91D}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>28</th>
      <td>348</td>
      <td>Flat Washer 5</td>
      <td>FW-7160</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{D182CF18-4DDF-429B-A0DF-DE1CFC92622D}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>29</th>
      <td>349</td>
      <td>Flat Washer 7</td>
      <td>FW-9160</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>1000</td>
      <td>750</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{7E55F64D-EA3C-45FF-BE72-F7F7B9D61A79}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>474</th>
      <td>970</td>
      <td>Touring-2000 Blue, 46</td>
      <td>BK-T44U-46</td>
      <td>1</td>
      <td>1</td>
      <td>Blue</td>
      <td>100</td>
      <td>75</td>
      <td>755.1508</td>
      <td>1214.85</td>
      <td>...</td>
      <td>T</td>
      <td>M</td>
      <td>U</td>
      <td>3.0</td>
      <td>35.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{C0009006-715F-4B76-A05A-1A0D3ADFB49A}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>475</th>
      <td>971</td>
      <td>Touring-2000 Blue, 50</td>
      <td>BK-T44U-50</td>
      <td>1</td>
      <td>1</td>
      <td>Blue</td>
      <td>100</td>
      <td>75</td>
      <td>755.1508</td>
      <td>1214.85</td>
      <td>...</td>
      <td>T</td>
      <td>M</td>
      <td>U</td>
      <td>3.0</td>
      <td>35.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{84ABDA8F-0007-4BCA-9A61-B2DEA58866C3}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>476</th>
      <td>972</td>
      <td>Touring-2000 Blue, 54</td>
      <td>BK-T44U-54</td>
      <td>1</td>
      <td>1</td>
      <td>Blue</td>
      <td>100</td>
      <td>75</td>
      <td>755.1508</td>
      <td>1214.85</td>
      <td>...</td>
      <td>T</td>
      <td>M</td>
      <td>U</td>
      <td>3.0</td>
      <td>35.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{6DCFE2A3-3555-44E4-9116-6F6DBE448B8B}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>477</th>
      <td>973</td>
      <td>Road-350-W Yellow, 40</td>
      <td>BK-R79Y-40</td>
      <td>1</td>
      <td>1</td>
      <td>Yellow</td>
      <td>100</td>
      <td>75</td>
      <td>1082.5100</td>
      <td>1700.99</td>
      <td>...</td>
      <td>R</td>
      <td>M</td>
      <td>W</td>
      <td>2.0</td>
      <td>27.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{237B16D9-53F2-4FD4-BEFE-48209E57AEC3}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>478</th>
      <td>974</td>
      <td>Road-350-W Yellow, 42</td>
      <td>BK-R79Y-42</td>
      <td>1</td>
      <td>1</td>
      <td>Yellow</td>
      <td>100</td>
      <td>75</td>
      <td>1082.5100</td>
      <td>1700.99</td>
      <td>...</td>
      <td>R</td>
      <td>M</td>
      <td>W</td>
      <td>2.0</td>
      <td>27.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{80BD3F8B-42C7-43D8-91F5-9FB6175287AF}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>479</th>
      <td>975</td>
      <td>Road-350-W Yellow, 44</td>
      <td>BK-R79Y-44</td>
      <td>1</td>
      <td>1</td>
      <td>Yellow</td>
      <td>100</td>
      <td>75</td>
      <td>1082.5100</td>
      <td>1700.99</td>
      <td>...</td>
      <td>R</td>
      <td>M</td>
      <td>W</td>
      <td>2.0</td>
      <td>27.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{0C61E8AF-003D-4E4B-B5B7-02F01A26BE26}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>480</th>
      <td>976</td>
      <td>Road-350-W Yellow, 48</td>
      <td>BK-R79Y-48</td>
      <td>1</td>
      <td>1</td>
      <td>Yellow</td>
      <td>100</td>
      <td>75</td>
      <td>1082.5100</td>
      <td>1700.99</td>
      <td>...</td>
      <td>R</td>
      <td>M</td>
      <td>W</td>
      <td>2.0</td>
      <td>27.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{EC4284DC-85FA-44A8-89EC-77FC9B71720A}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>481</th>
      <td>977</td>
      <td>Road-750 Black, 58</td>
      <td>BK-R19B-58</td>
      <td>1</td>
      <td>1</td>
      <td>Black</td>
      <td>100</td>
      <td>75</td>
      <td>343.6496</td>
      <td>539.99</td>
      <td>...</td>
      <td>R</td>
      <td>L</td>
      <td>U</td>
      <td>2.0</td>
      <td>31.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{87B81A1A-A5B5-43D2-A20D-0230800490B9}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>482</th>
      <td>978</td>
      <td>Touring-3000 Blue, 44</td>
      <td>BK-T18U-44</td>
      <td>1</td>
      <td>1</td>
      <td>Blue</td>
      <td>100</td>
      <td>75</td>
      <td>461.4448</td>
      <td>742.35</td>
      <td>...</td>
      <td>T</td>
      <td>L</td>
      <td>U</td>
      <td>3.0</td>
      <td>36.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{4F638E15-2ED0-4193-90CE-47DA580E01DD}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>483</th>
      <td>979</td>
      <td>Touring-3000 Blue, 50</td>
      <td>BK-T18U-50</td>
      <td>1</td>
      <td>1</td>
      <td>Blue</td>
      <td>100</td>
      <td>75</td>
      <td>461.4448</td>
      <td>742.35</td>
      <td>...</td>
      <td>T</td>
      <td>L</td>
      <td>U</td>
      <td>3.0</td>
      <td>36.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{DE305B62-88FC-465B-B23D-D8C0F7E6D361}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>484</th>
      <td>980</td>
      <td>Mountain-400-W Silver, 38</td>
      <td>BK-M38S-38</td>
      <td>1</td>
      <td>1</td>
      <td>Silver</td>
      <td>100</td>
      <td>75</td>
      <td>419.7784</td>
      <td>769.49</td>
      <td>...</td>
      <td>M</td>
      <td>M</td>
      <td>W</td>
      <td>1.0</td>
      <td>22.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{7A927632-99A4-4F24-ADCE-0062D2D113D9}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>485</th>
      <td>981</td>
      <td>Mountain-400-W Silver, 40</td>
      <td>BK-M38S-40</td>
      <td>1</td>
      <td>1</td>
      <td>Silver</td>
      <td>100</td>
      <td>75</td>
      <td>419.7784</td>
      <td>769.49</td>
      <td>...</td>
      <td>M</td>
      <td>M</td>
      <td>W</td>
      <td>1.0</td>
      <td>22.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{0A72791C-A984-4733-AE4E-2B4373CFD7CD}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>486</th>
      <td>982</td>
      <td>Mountain-400-W Silver, 42</td>
      <td>BK-M38S-42</td>
      <td>1</td>
      <td>1</td>
      <td>Silver</td>
      <td>100</td>
      <td>75</td>
      <td>419.7784</td>
      <td>769.49</td>
      <td>...</td>
      <td>M</td>
      <td>M</td>
      <td>W</td>
      <td>1.0</td>
      <td>22.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{4EA4FE06-AAEA-42D4-A9D9-69F6A9A4A042}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>487</th>
      <td>983</td>
      <td>Mountain-400-W Silver, 46</td>
      <td>BK-M38S-46</td>
      <td>1</td>
      <td>1</td>
      <td>Silver</td>
      <td>100</td>
      <td>75</td>
      <td>419.7784</td>
      <td>769.49</td>
      <td>...</td>
      <td>M</td>
      <td>M</td>
      <td>W</td>
      <td>1.0</td>
      <td>22.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{0B0C8EE4-FF2D-438E-9CAC-464783B86191}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>488</th>
      <td>984</td>
      <td>Mountain-500 Silver, 40</td>
      <td>BK-M18S-40</td>
      <td>1</td>
      <td>1</td>
      <td>Silver</td>
      <td>100</td>
      <td>75</td>
      <td>308.2179</td>
      <td>564.99</td>
      <td>...</td>
      <td>M</td>
      <td>L</td>
      <td>U</td>
      <td>1.0</td>
      <td>23.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{B96C057B-6416-4851-8D59-BCB37C8E6E51}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>489</th>
      <td>985</td>
      <td>Mountain-500 Silver, 42</td>
      <td>BK-M18S-42</td>
      <td>1</td>
      <td>1</td>
      <td>Silver</td>
      <td>100</td>
      <td>75</td>
      <td>308.2179</td>
      <td>564.99</td>
      <td>...</td>
      <td>M</td>
      <td>L</td>
      <td>U</td>
      <td>1.0</td>
      <td>23.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{B8D1B5D9-8A39-4097-A04A-56E95559B534}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>490</th>
      <td>986</td>
      <td>Mountain-500 Silver, 44</td>
      <td>BK-M18S-44</td>
      <td>1</td>
      <td>1</td>
      <td>Silver</td>
      <td>100</td>
      <td>75</td>
      <td>308.2179</td>
      <td>564.99</td>
      <td>...</td>
      <td>M</td>
      <td>L</td>
      <td>U</td>
      <td>1.0</td>
      <td>23.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{E8CEC794-E8E2-4312-96A7-4832E573D3FC}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>491</th>
      <td>987</td>
      <td>Mountain-500 Silver, 48</td>
      <td>BK-M18S-48</td>
      <td>1</td>
      <td>1</td>
      <td>Silver</td>
      <td>100</td>
      <td>75</td>
      <td>308.2179</td>
      <td>564.99</td>
      <td>...</td>
      <td>M</td>
      <td>L</td>
      <td>U</td>
      <td>1.0</td>
      <td>23.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{77EF419F-481F-40B9-BDB9-7E6678E550E3}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>492</th>
      <td>988</td>
      <td>Mountain-500 Silver, 52</td>
      <td>BK-M18S-52</td>
      <td>1</td>
      <td>1</td>
      <td>Silver</td>
      <td>100</td>
      <td>75</td>
      <td>308.2179</td>
      <td>564.99</td>
      <td>...</td>
      <td>M</td>
      <td>L</td>
      <td>U</td>
      <td>1.0</td>
      <td>23.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{CAD60945-183E-4AB3-A70C-3F5BAC6BF134}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>493</th>
      <td>989</td>
      <td>Mountain-500 Black, 40</td>
      <td>BK-M18B-40</td>
      <td>1</td>
      <td>1</td>
      <td>Black</td>
      <td>100</td>
      <td>75</td>
      <td>294.5797</td>
      <td>539.99</td>
      <td>...</td>
      <td>M</td>
      <td>L</td>
      <td>U</td>
      <td>1.0</td>
      <td>23.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{28287157-3F06-487B-8531-BEE8A37329E4}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>494</th>
      <td>990</td>
      <td>Mountain-500 Black, 42</td>
      <td>BK-M18B-42</td>
      <td>1</td>
      <td>1</td>
      <td>Black</td>
      <td>100</td>
      <td>75</td>
      <td>294.5797</td>
      <td>539.99</td>
      <td>...</td>
      <td>M</td>
      <td>L</td>
      <td>U</td>
      <td>1.0</td>
      <td>23.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{F5752C9C-56BA-41A7-83FD-139DA28C15FA}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>495</th>
      <td>991</td>
      <td>Mountain-500 Black, 44</td>
      <td>BK-M18B-44</td>
      <td>1</td>
      <td>1</td>
      <td>Black</td>
      <td>100</td>
      <td>75</td>
      <td>294.5797</td>
      <td>539.99</td>
      <td>...</td>
      <td>M</td>
      <td>L</td>
      <td>U</td>
      <td>1.0</td>
      <td>23.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{C7852127-2FB8-4959-B5A3-DE5A8D6445E4}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>496</th>
      <td>992</td>
      <td>Mountain-500 Black, 48</td>
      <td>BK-M18B-48</td>
      <td>1</td>
      <td>1</td>
      <td>Black</td>
      <td>100</td>
      <td>75</td>
      <td>294.5797</td>
      <td>539.99</td>
      <td>...</td>
      <td>M</td>
      <td>L</td>
      <td>U</td>
      <td>1.0</td>
      <td>23.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{75752E26-A3B6-4264-9B06-F23A4FBDC5A7}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>497</th>
      <td>993</td>
      <td>Mountain-500 Black, 52</td>
      <td>BK-M18B-52</td>
      <td>1</td>
      <td>1</td>
      <td>Black</td>
      <td>100</td>
      <td>75</td>
      <td>294.5797</td>
      <td>539.99</td>
      <td>...</td>
      <td>M</td>
      <td>L</td>
      <td>U</td>
      <td>1.0</td>
      <td>23.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{69EE3B55-E142-4E4F-AED8-AF02978FBE87}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>498</th>
      <td>994</td>
      <td>LL Bottom Bracket</td>
      <td>BB-7421</td>
      <td>1</td>
      <td>1</td>
      <td>NaN</td>
      <td>500</td>
      <td>375</td>
      <td>23.9716</td>
      <td>53.99</td>
      <td>...</td>
      <td>NaN</td>
      <td>L</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>95.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{FA3C65CD-0A22-47E3-BDF6-53F1DC138C43}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>499</th>
      <td>995</td>
      <td>ML Bottom Bracket</td>
      <td>BB-8107</td>
      <td>1</td>
      <td>1</td>
      <td>NaN</td>
      <td>500</td>
      <td>375</td>
      <td>44.9506</td>
      <td>101.24</td>
      <td>...</td>
      <td>NaN</td>
      <td>M</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>96.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{71AB847F-D091-42D6-B735-7B0C2D82FC84}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>500</th>
      <td>996</td>
      <td>HL Bottom Bracket</td>
      <td>BB-9108</td>
      <td>1</td>
      <td>1</td>
      <td>NaN</td>
      <td>500</td>
      <td>375</td>
      <td>53.9416</td>
      <td>121.49</td>
      <td>...</td>
      <td>NaN</td>
      <td>H</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>97.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{230C47C5-08B2-4CE3-B706-69C0BDD62965}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>501</th>
      <td>997</td>
      <td>Road-750 Black, 44</td>
      <td>BK-R19B-44</td>
      <td>1</td>
      <td>1</td>
      <td>Black</td>
      <td>100</td>
      <td>75</td>
      <td>343.6496</td>
      <td>539.99</td>
      <td>...</td>
      <td>R</td>
      <td>L</td>
      <td>U</td>
      <td>2.0</td>
      <td>31.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{44CE4802-409F-43AB-9B27-CA53421805BE}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>502</th>
      <td>998</td>
      <td>Road-750 Black, 48</td>
      <td>BK-R19B-48</td>
      <td>1</td>
      <td>1</td>
      <td>Black</td>
      <td>100</td>
      <td>75</td>
      <td>343.6496</td>
      <td>539.99</td>
      <td>...</td>
      <td>R</td>
      <td>L</td>
      <td>U</td>
      <td>2.0</td>
      <td>31.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{3DE9A212-1D49-40B6-B10A-F564D981DBDE}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>503</th>
      <td>999</td>
      <td>Road-750 Black, 52</td>
      <td>BK-R19B-52</td>
      <td>1</td>
      <td>1</td>
      <td>Black</td>
      <td>100</td>
      <td>75</td>
      <td>343.6496</td>
      <td>539.99</td>
      <td>...</td>
      <td>R</td>
      <td>L</td>
      <td>U</td>
      <td>2.0</td>
      <td>31.0</td>
      <td>2013-05-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{AE638923-2B67-4679-B90E-ABBAB17DCA31}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
  </tbody>
</table>
<p>504 rows × 25 columns</p>
</div>



### `obj.empty` -- returns booleans for whether object is empty or not


```
ad_cycle.empty
```




    False



## Selecting Data

We can select data as either single values or we can slice the data in subsets.


#### Single Values

### `df.loc[row_label, col_label]` -- select a single item in a DataFrame by its row and column labels


```
print("ProductID:", ad_cycle.loc[0,'ProductID'])

print("Name", ad_cycle.loc[0,'Name'])

print("ProductNumber", ad_cycle.loc[0,'ProductNumber'])

```

    ProductID: 1
    Name Adjustable Race
    ProductNumber AR-5381



### `df.loc[start_row_label : end_row_label, start_col_label : end_col_label]` 

-- select a slice of a DataFrame by starting and ending row/column labels


```
ad_cycle.loc[0:3, "ProductID":"ProductNumber"]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ProductID</th>
      <th>Name</th>
      <th>ProductNumber</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Adjustable Race</td>
      <td>AR-5381</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Bearing Ball</td>
      <td>BA-8327</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>BB Ball Bearing</td>
      <td>BE-2349</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Headset Ball Bearings</td>
      <td>BE-2908</td>
    </tr>
  </tbody>
</table>
</div>




### `df.iloc[row_index,:]` -- select a row in a DataFrame by index position



```
ad_cycle.iloc[6:8]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ProductID</th>
      <th>Name</th>
      <th>ProductNumber</th>
      <th>MakeFlag</th>
      <th>FinishedGoodsFlag</th>
      <th>Color</th>
      <th>SafetyStockLevel</th>
      <th>ReorderPoint</th>
      <th>StandardCost</th>
      <th>ListPrice</th>
      <th>...</th>
      <th>ProductLine</th>
      <th>Class</th>
      <th>Style</th>
      <th>ProductSubcategoryID</th>
      <th>ProductModelID</th>
      <th>SellStartDate</th>
      <th>SellEndDate</th>
      <th>DiscontinuedDate</th>
      <th>rowguid</th>
      <th>ModifiedDate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>318</td>
      <td>ML Crankarm</td>
      <td>CA-6738</td>
      <td>0</td>
      <td>0</td>
      <td>Black</td>
      <td>500</td>
      <td>375</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>M</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{EABB9A92-FA07-4EAB-8955-F0517B4A4CA7}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>319</td>
      <td>HL Crankarm</td>
      <td>CA-7457</td>
      <td>0</td>
      <td>0</td>
      <td>Black</td>
      <td>500</td>
      <td>375</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008-04-30 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{7D3FD384-4F29-484B-86FA-4206E276FE58}</td>
      <td>2014-02-08 10:01:36.827000000</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 25 columns</p>
</div>



### `s.iloc[index]` -- select a single item by its position




```
ad_cycle.iloc[0]
```




    ProductID                                                     1
    Name                                            Adjustable Race
    ProductNumber                                           AR-5381
    MakeFlag                                                      0
    FinishedGoodsFlag                                             0
    Color                                                       NaN
    SafetyStockLevel                                           1000
    ReorderPoint                                                750
    StandardCost                                                  0
    ListPrice                                                     0
    Size                                                        NaN
    SizeUnitMeasureCode                                         NaN
    WeightUnitMeasureCode                                       NaN
    Weight                                                      NaN
    DaysToManufacture                                             0
    ProductLine                                                 NaN
    Class                                                       NaN
    Style                                                       NaN
    ProductSubcategoryID                                        NaN
    ProductModelID                                              NaN
    SellStartDate                               2008-04-30 00:00:00
    SellEndDate                                                 NaN
    DiscontinuedDate                                            NaN
    rowguid                  {694215B7-08F7-4C0D-ACB1-D734BA44C0C8}
    ModifiedDate                      2014-02-08 10:01:36.827000000
    Name: 0, dtype: object



### `s.loc[index]` -- select a slice of items from a Series


```
ad_cycle.loc[1]
```




    ProductID                                                     2
    Name                                               Bearing Ball
    ProductNumber                                           BA-8327
    MakeFlag                                                      0
    FinishedGoodsFlag                                             0
    Color                                                       NaN
    SafetyStockLevel                                           1000
    ReorderPoint                                                750
    StandardCost                                                  0
    ListPrice                                                     0
    Size                                                        NaN
    SizeUnitMeasureCode                                         NaN
    WeightUnitMeasureCode                                       NaN
    Weight                                                      NaN
    DaysToManufacture                                             0
    ProductLine                                                 NaN
    Class                                                       NaN
    Style                                                       NaN
    ProductSubcategoryID                                        NaN
    ProductModelID                                              NaN
    SellStartDate                               2008-04-30 00:00:00
    SellEndDate                                                 NaN
    DiscontinuedDate                                            NaN
    rowguid                  {58AE3C20-4F3A-4749-A7D4-D568806CC537}
    ModifiedDate                      2014-02-08 10:01:36.827000000
    Name: 1, dtype: object



### Difference between loc and iloc

loc gets rows (or columns) with particular labels from the index. iloc gets rows (or columns) at particular positions in the index (so it only takes integers). [SO](https://stackoverflow.com/questions/31593201/how-are-iloc-ix-and-loc-different)


```
s2 = pd.Series(np.nan, index=[49,48,47,46,45, 1, 2, 3, 4, 5])
print(s2.iloc[:3])
print('---------------')
print(s2.loc[:3])
```

    49   NaN
    48   NaN
    47   NaN
    dtype: float64
    ---------------
    49   NaN
    48   NaN
    47   NaN
    46   NaN
    45   NaN
    1    NaN
    2    NaN
    3    NaN
    dtype: float64

