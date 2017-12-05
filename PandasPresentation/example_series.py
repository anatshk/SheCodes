import pandas as pd

#####################################################################################
# Series - 1D array
#####################################################################################

numbers = [5, 4, 3, 2, 1]
animals = ['Cat', 'Dog', 'Bird', 'Iguana', 'Ferret']

# define Series
s_numbers = pd.Series(numbers)
s_animals = pd.Series(animals)

# Change index in Series (anything can be an index)
s_animals_set_index = pd.Series(data=animals, index=numbers)
s_numbers_set_index = pd.Series(data=numbers, index=animals)

# Create a timestamp and use as index
time_range = pd.date_range(start='10/12/2017', end='31/12/2017', freq='2D')
time_axis = time_range[:len(animals)]
s_animals_time_index = pd.Series(data=animals, index=time_axis)

# Series methods
# (https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html)

# numeric
min_num = s_numbers.min()
cum_sum = s_numbers.cumsum()

# sorting
sort_vals_1 = s_animals.sort_values()
sort_vals_2 = s_animals.sort_values(ascending=False)
sort_index = s_animals_set_index.sort_index()

# categorical
with_dup = pd.Series(['one', 'two', 'three', 'three', 'two', 'one', 'zero'])
no_dup = with_dup.drop_duplicates()  # NOTE: Index does not change per item!

# accessing by index
no_dup.loc[2]  # 'three'
no_dup.loc[3]  # crash - no such index
no_dup.loc[6]  # 'zero'

# accessing by location
no_dup.iloc[2]  # 'three'
no_dup.iloc[3]  # 'zero'
no_dup.iloc[6]  # crash - series only has 4 items
