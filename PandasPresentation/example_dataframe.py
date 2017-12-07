import pandas as pd

from random import randint

"""
NOTE: Examples are in Python 3
"""

#####################################################################################
# DataFrame - 2D tabular
#####################################################################################

# Define a dictionary with data for example
dct = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Gender': ['Male', 'Female', 'Male', 'Male', 'Female'],
    'DOB': [pd.Timestamp(val).date() for val in
            ['1-Jan-80', '10-Mar-83', '31-Mar-85', '11-Jun-80', '10-Jan-80']],
    'Pet': ['Dog', 'Cat', 'Dog', 'Dog', None],
    'Drivers_License': [True, False, False, False, True],
    'Height_cm': [174, 157, 189, 168, 192]
}

# Initialize data from dictionary (keys - column names, values - columns)
df_dct = pd.DataFrame(dct)

# Set column order
df_dct2 = pd.DataFrame(dct,  columns=['Name', 'DOB', 'Gender', 'Height_cm',
                                      'Pet', 'Drivers_License'])

# Assign index
df_dct_index = pd.DataFrame(dct, index=['I1', 'I2', 'I3', 'I4', 'I5'])

# Use one of the dictionary keys as index
df_dct_index2 = pd.DataFrame(dct, index=dct['Pet'])

# Initialize data from array-like data (each array is a ROW!)
person1 = ['Jane', 'Smith', 24]
person2 = ['Maria', 'Jones', 47]
columns = ['FirstName', 'LastName', 'Age']
index = ['ID1', 'ID2']

df_arr = pd.DataFrame(data=[person1, person2], columns=columns, index=index)

# Initializing from missing values (Note NaN in index 'd', column 'col1')
col1 = [1, 2, 3]
index1 = ['a', 'b', 'c']

col2 = [1, 2, 3, 4]
index2 = ['a', 'b', 'c', 'd']

# pair each column with it's relevant indices in Series, then create DataFrame
df_missing = pd.DataFrame(data={'col1': pd.Series(col1, index=index1),
                                'col2': pd.Series(col2, index=index2)})


#####################################################################################
# Accessing information
#####################################################################################
big_dct = {
    'col1': range(0, 100),
    'col2': pd.date_range(start='10/12/2017', periods=100),
    'col3': [chr(randint(65, 90)) * 3 for ix in range(100)]
}
index = range(100, 0, -1)

df_big = pd.DataFrame(big_dct, index=index)

# See first \ last records ( = rows)
head = df_big.head()
tail = df_big.tail()

# access column
col3 = df_big['col3']

# access record \ row
row0_loc = df_big.loc[1]  # reminder - loc accesses indices
row0_iloc = df_big.iloc[0]  # reminder - iloc accesses by order in DataFrame
# df_big[0] - will NOT work!

# creating a new column
df_big['new_column'] = df_big['col1'] * 2


# creating a new column with a function
def my_func(row):
    """
    :param row: single DataFrame row, with all the columns
    """
    if row['col3'][0] in 'AEIOU':
        return row['col3'] * row['col1']
    return row['col3']


df_big['another_column'] = df_big.apply(my_func, axis=1)

# removing rows with missing data

# TODO: delete values and fill missing values


a = 5
