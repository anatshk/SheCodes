import pandas as pd
import folium  # http://folium.readthedocs.io/en/latest/quickstart.html
import matplotlib.pyplot as plt
import numpy as np

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

# GroupBy object - groups the DataFrame by a column and allows to perform actions
count_vendors = df.groupby('vendor_id').count()
# in each column, we'll see the number each vendor_ids appears
# note that 'vendor_id' is now the index!

# select (any) one column to avoid duplicated columns
count_vendors_series = df.groupby('vendor_id').count()['trip_type']

# we can also group by several columns to create multi-index.
# this complicates the data and not recommended.
multi_groupby = df.groupby(['vendor_id', 'passenger_count', 'payment_type']).count()['trip_type']

# there is a similar Series method that avoids the redundant counts
vendor_count = df['vendor_id'].value_counts()

# divide the data into bins using pd.cut (Series method)
binned_distance = pd.cut(df['trip_distance'], bins=10)
# returns for each row the bin it belongs to.
# Note the list of bins printed at the end of Series.
# Notice that leftmost bin is (-0.379, 37.891] even though no trip_distance < 0.

# create a histogram - group by the bins, count each bin
hist = binned_distance.value_counts()
# we see that most of the rides were < 37 miles and out bin selection was not ideal

# select different bins (can be non-uniform)
bins = list(range(15)) + [15, 20, 25, 30, 35, 40]
hist_2 = pd.cut(df['trip_distance'], bins=bins).value_counts()
hist_2.sort_index(inplace=True)  # sort by index

# lets plot the histogram (Series method)
plt.figure()  # indication to open a new figure
hist_plot = hist_2.plot(kind='bar')
for tick in hist_plot.get_xticklabels():
    tick.set_rotation(45)
hist_plot.set_xlabel('Ride Distance in miles')
hist_plot.set_ylabel('Number of Rides')
hist_plot.set_title('Histogram of Ride Distances')

# Different plots - pie, line, etc.
plt.figure()  # indication to open a new figure
pie = vendor_count.plot(kind='pie')

# Calculate median number of rides per hour, perform the median on weekdays (Sun-Sat)
# 1. create new columns, weekday and hour
df['weekday'] = df['pickup_time'].dt.weekday
df['hour'] = df['pickup_time'].dt.hour
# each Timestamp Series (parse_dates read these columns as Timestamps),
# has 'dt' property that allows to access its datetime properties

# 2. count how many rides per weekday, per hour
ride_count = df.groupby(['weekday', 'hour'], as_index=False).count()
# as_index=False - avoids replacing the index with the groupby columns
# see weekday and hour columns + trip_type column for ride counts
ride_count[['weekday', 'hour', 'trip_type']].head()

# 3. now, take the result of the first groupby
#    and perform groupby on the hour to calculate the median on the weekdays
#    (groupby - creates groups of 7 counts per day for each hour)
ride_count_hourly = ride_count.groupby('hour').median()['trip_type']

ax = ride_count_hourly.plot.bar(rot=45)
ax.set_xlabel('Hour')
ax.set_title('Median Hourly Rides')
ax.set_ylabel('# rides')

# Pivot Table - summarizes data in another table using aggregation function and grouping
# Example - create 2 boxplots, one per vendor, present daily earnings
# 1. Select data for pivot -
df_for_pivot = df[['vendor_id', 'total_amount', 'weekday']]
# 2. select index, columns, values and aggregation function
pivot_df = df_for_pivot.pivot_table(index='weekday',
                                    columns='vendor_id',
                                    values='total_amount',
                                    aggfunc=np.sum)
# pivot_df is a DataFrame where weekdays are index and vendors are columns
# the value in each column is sum of earnings per weekday
plt.figure()  # indication to open a new figure
piv_fig_bar = pivot_df.plot.bar()
piv_fig_bar.set_xlabel('Weekday')
piv_fig_bar.set_title('Weekday Earnings per Vendor')
piv_fig_bar.set_ylabel('Earnings in USD')


# 3. plot the pivot table
plt.figure()  # indication to open a new figure
piv_fig = pivot_df.plot.box()
piv_fig.set_xlabel('Vendor')
piv_fig.set_title('Weekday Earnings per Vendor')
piv_fig.set_ylabel('Earnings in USD')


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
