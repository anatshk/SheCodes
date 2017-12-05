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

min_num = s_numbers.min()
cum_sum = s_numbers.cumsum()

sort_vals_1 = s_animals.sort_values()
sort_vals_2 = s_animals.sort_values(ascending=False)
sort_index = s_animals_set_index.sort_values()


# Define a dictionary with data for example
dct = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Gender': ['Male', 'Female', 'Male', 'Male', 'Female'],
    'DOB': [pd.Timestamp(val).date() for val in ['1-Jan-80', '10-Mar-83', '31-Mar-85', '11-Jun-80', '10-Jan-80']],
    'Pet': ['Dog', 'Cat', 'Dog', 'Dog', None],
    'Drivers_License': [True, False, False, False, True],
    'Height_cm': [174, 157, 189, 168, 192]
}




df = pd.DataFrame.from_dict(dct)

a = 5
