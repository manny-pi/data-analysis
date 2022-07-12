import sys

import pandas as pd 
import numpy as np

delim = '\n- - - - - - - - -\n\n'

def series():
    """ 
    A Series is a one-dimensional, indexed array of data 
    """

    ser1 = pd.Series([-4, 7, -5, 3])
    ser2 = pd.Series([1, 5, 11, 2] , index=['a', 'b', 'd', 'c'])

    print(ser1, delim)
    print(ser2, delim)

    # access elements in the series 
    print(f'Series 1 ex: {ser1[0]}', delim)
    print(f"Series 2 ex: {ser2['b']}", delim)

    # access the elements in the series 
    print(ser1.values, delim)
    print(ser1.index, delim)

    # access the indexes in the series
    print(ser1.index, delim)
    print(ser2.index, delim)

    # accessing multiple values simulatenously; pass a list of the 
    # indexes you want to retrieve
    print(ser1[[0, 2, 3]], delim)
    print(ser2[['a', 'b', 'c']], delim)


    # common numpy operations used on Series objects 
    # - - filtering using boolean expressions
    indexes = ser2 > 0
    print(indexes)
    print(ser2[indexes], delim)

    # - - algebraic expressions
    print(ser2 * 2, delim)
    print(np.exp(ser2), delim) # raise e to the n power, where n in ser2


    # creating series from existing datasets
    sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
    ser3 = pd.Series(sdata)
    print(ser3, delim)

    states=['California', 'Ohio', 'Florida', 'Utah']
    ser4 = pd.Series(sdata, states) # original keys in sdata get deleted; new keys are given NaN values
    print(ser4, delim)
    print(f"California: {ser4['California']}", delim)

    # detecting values
    print(pd.isnull(ser4), delim) # detecting null/missing values
    print(pd.notnull(ser4), delim) # detecting non-null values

    # pandas.Series automatically aligns differently indexed data in arithmetic operations
    print(ser3 + ser4, delim)

    # Fields in the pandas.Series object have names that increase functionality
    ser4.name = 'population' # the name of the Series 
    ser4.index.name = 'state' # the name of the index
    print(ser4, delim) # prints the Series object, but gives the index a name: 'state'

    # Reassigning a Series index 
    ser4.index = ['Los Angeles', 'New York', 'Washington', 'District of Columbia']
    print(ser4, delim)

def dataframe(): 
    """
    A DataFrame represents tabular, spreadsheet-like data structure containing an ordered
    collection of columns, each with a differen value type

    Each column in a DataFrame is a series
    """

    # creating a pandas.DataFrame from an existing collection
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 
    'year': [2000, 2001, 2002, 2001, 2001], 
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    df = pd.DataFrame(data)
    print(df, delim)

    # if a column doesn't have data, pandas fill it with NaN
    df2 = pd.DataFrame(data, columns=['state', 'year', 'pop', 'debt'], index=[1, 2, 3, 4, 5])
    print(df2, delim)

    # accessing columns in a DataFrame 
    print(df2['state'], delim) # using dictionary notation
    print(df2.year, delim) # using attributes

    # accessing rows 
    print(df2.iloc[2], delim) # returns row 2 of the DataFrame

    # assigning values to columns 
    df2['debt'] = 100
    print(df2, delim)

    df2['debt'] = np.arange(5.)
    print(df2, delim)
    

# series()
dataframe()