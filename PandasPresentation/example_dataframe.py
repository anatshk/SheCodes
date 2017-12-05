import pandas as pd

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

# Initialize data from dictionary
df = pd.DataFrame.from_dict(dct)

# TODO: show how to replace index
# TODO: show how to access columns \ rows
# TODO: mention immutability (copies are created unless using 'inplace')
# TODO: create new columns
# TODO: delete values and fill missing values


a = 5
