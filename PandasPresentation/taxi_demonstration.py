import pandas as pd
import folium  # http://folium.readthedocs.io/en/latest/quickstart.html

from os.path import getsize

from bz2 import BZ2File

"""
NOTE: Examples are in Python 3
Full data can be found here: 
http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml
"""

# path to data - csv.bz2: a csv file that was compressed on a linux system
taxi_path = r'C:\Users\Anat\Downloads\pandas_data\taxi.csv.bz2'

# see size of file before loading.
# getsize returns size in bits, << performs bitwise shift left to get mb
print('size = {:.2f}mb'.format(getsize(taxi_path) / (1 << 20)))

# load the file (takes a few moments)
df = pd.read_csv(taxi_path)  # create DataFrame from CSV

# check data size
len(df)

# lets look at the data
first_row = df.iloc[0]
# Note: seems that the data is corrupted -
# VendorID is a date, pickup time is a letter, etc.

# access the file directly
with BZ2File(taxi_path) as fp:
    header = fp.readline()  # read 1st line, data headers
    data = fp.readline()  # read 2nd line, 1st row of data

# for Python 3 only - decode
header = header.decode('utf-8')
data = data.decode('utf-8')

# split column names from header and values from 1st row
columns = header.split(',')
values = data.split(',')

len(columns)  # 21
len(values)  # 23
# the number of columns and values does not match

# add 2 placeholders to the end of column names and compare columns to values
tmp_list = [(col, val) for col, val in zip(columns + ['fake1', 'fake2'], values)]
# last pairs -  ('fake1', ''), ('fake2', '\r\n') do not have valid values
# usually - randomly check a few more rows, not just the 1st
# in this case - we will just use the first 21 columns that have headers

# re-load the data, usecols limits us to 21 columns, parse_dates indicates which columns contain dates
df = pd.read_csv(taxi_path, usecols=range(21), parse_dates=['lpep_pickup_datetime', 'Lpep_dropoff_datetime'])

# check number and names of columns
len(df.columns)
col_names = df.columns

# Note:
# 'Trip_type ' column has a trailing space
# Column titles are camelCase or capitalized or lower case

# renaming columns, notice the use of inplace=True instead of assignment
# https://pandas.pydata.org/pandas-docs/version/0.21/generated/pandas.DataFrame.rename.html
col_renaming = {
    'VendorID': 'vendor_id',
    'lpep_pickup_datetime': 'pickup_time',
    'Lpep_dropoff_datetime': 'dropoff_time',
    'RateCodeID': 'rate_code_id',
    'Pickup_longitude': 'pickup_lon',
    'Pickup_latitude': 'pickup_lat',
    'Dropoff_longitude': 'dropoff_lon',
    'Dropoff_latitude': 'dropoff_lat',
    'Trip_type ': 'trip_type',
}
df.rename(columns=col_renaming, inplace=True)
# df = df.rename(columns=col_renaming)

# one more step - make all column names lowercase
df.rename(str.lower, axis='columns', inplace=True)
new_col_names = df.columns

# look at the column types
df.dtypes
# ints and floats - floats are actual values, ints probably map to strings (except passenger #)
# (trip_type - one-way\return, payment_type - cash\credit\app)

#######################################################################
# Data Visualization - on a map (folium package - best used in Jupyter)
#######################################################################

# find median center of pickup locations
map_center = [df['pickup_lat'].median(), df['pickup_lon'].median()]

# display map with center \ pickup\dropoff locations

# commented out because it takes a while 
"""
m = folium.Map(location=map_center, zoom_start=15)
marker = folium.Marker(map_center)
marker.add_to(m)
m.save('C:\\Users\\Anat\\Documents\\GitRepos\\SheCodes\\PandasPresentation\\map.html')

# write a function for placing markers per row
def add_marker(row):
    pickup = folium.Marker([row['pickup_lat'], row['pickup_lon']],
                           icon=folium.Icon(color='green'))
    pickup.add_to(m)
    dropoff = folium.Marker([row['dropoff_lat'], row['dropoff_lon']],
                            icon=folium.Icon(color='red'))
    dropoff.add_to(m)

# take a smaller DataFrame to see all pickup \ dropoff locations
df_small = df.iloc[1::1000]
m = folium.Map(location=map_center, zoom_start=15)
df_small.apply(add_marker, axis=1)
m.save(r'C:\\Users\\Anat\\Documents\\GitRepos\\SheCodes\\PandasPresentation\\map_with_locs.html')
"""

# GroupBy
df.groupby('vendor_id')


a = 5

# TODO: see taxi jupyter notebook for ideas.
# TODO: go over tutorials for things to demonstrate:
"""
https://pandas.pydata.org/pandas-docs/stable/dsintro.html#dsintro
https://pandas.pydata.org/pandas-docs/stable/tutorials.html
https://pandas.pydata.org/pandas-docs/stable/10min.html
https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python
"""
# TODO: think of ways to use function in previous example
# TODO: write a demonstration with plots, pivot table, sample,
# TODO: show how to write to Excel

# TODO: instead of final slide, create a df with x and y of points when plotted will show 'Questions?'
# TODO: (write in paint, read as matrix and pixellate?)

# TODO: add a basic linear regression model? on this data or  http://pbpython.com/amortization-model-revised.html
