
# coding: utf-8

# In[1]:

2+5  # shift+enter runs cell


# In[2]:

import numpy as np


# In[3]:

help(np.any)


# In[7]:

# Jupyter only
get_ipython().magic('pinfo2 np.any')


# In[8]:

np.any  # tab for completion


# In[9]:

np.any([])  # shift + tab will show api


# In[10]:

# In Python everything is True except 
# - 0 values, (0, 0.0, (0+0j))
# - Empty collections ([], (), '', {})
# - False
# - None


# In[13]:

track_pth = r"C:\Users\anat.shkolyar\PycharmProjects\pandas_workshop\data\track.csv"


# In[14]:

import pandas as pd


# In[15]:

df = pd.read_csv(track_pth)  # 1st row assumed header


# In[16]:

df.head()  # shows N first lines + header, N=5 as default


# In[17]:

# lat, lng, time - columns
df.columns


# In[18]:

# columns are of 'Pandas Series' type, pd.Series
df['lat'].head()


# In[19]:

# leftmost 'col' - data frame index
df.index
# in this case - range index, but in pandas indices can be anything, not always numeric \ unique \ consistent


# In[20]:

df1 = pd.DataFrame(np.arange(12).reshape(4,3), columns=['c1', 'c2', 'c3'], index=['a', 'a', 'b', 'c'])


# In[21]:

df1


# In[22]:

df1.loc['a']  # accessing by index using 'loc' can return multiple rows if index is not unique. example - if intex is timestamp and several events occure at same time


# In[23]:

df1.iloc[0]  # access by location from top


# In[25]:

df.dtypes  # column types - we want 'time' to be a timestamp and not object 


# In[26]:

df = pd.read_csv(track_pth, parse_dates=['time'])  # force specific column to be time, setting explicit format may make csv reading much quicker (no explicit format meand pd is "guessing" format from data)
df.dtypes


# In[27]:

df.loc[10:15]  # slicing - unlike python, INCLUDES THE END INDEX


# In[28]:

df.iloc[10:15]  # iloc DOES NOT INCLUDE LAST


# In[29]:

# if index is not numeric - lexicographic sorting is applied ('a' < 'b')


# In[31]:

hdf = df.head()
hdf.loc[[True, False, True, True, False]]  # boolean indexing, boolean rows on index


# In[33]:

hdf.loc[[True, False, True, True, False], ['lat', 'lng']]  # slice on rows and columns


# In[34]:

hdf['time'].dt.second < 10  # checking conditions


# In[35]:

hdf[hdf['time'].dt.second < 10]  # Accessing by .dt or .str or .cat (where the type of the column matches) gives us more methods for time \ string \ categorical


# In[36]:

pd.Timestamp.now().weekday()


# In[37]:

# working with weekdays in a more readable way with calendar
import calendar
pd.Timestamp.now().weekday() == calendar.MONDAY


# In[38]:

# combining conditions - | OR, & AND, ~ NOT, parentheses are required!
(hdf['time'].dt.second < 10) | (hdf['time'].dt.second > 25)


# In[40]:

# query - can be faster than boolean indexing in specific cases (compare both when using)
df.query('time < "2015-08-20 03:48:30"')


# In[41]:

# query with variables (string formatting also works!)
df.query('time < @time', {'time': "2015-08-20 03:48:30"'})  # WRONG - GET CORRECT CODE FROM MIKI


# In[42]:

# Calculate run speed from data in track_pth
# show boxplot of speed in km\h


# In[43]:

get_ipython().magic('pwd')


# In[48]:

# copy dist.py next to notebook to get distance function
from dist import dist as earth_distance


# In[45]:

# dist uses numpy functions such as sin, which are universal (work on scalar \ array) and give results in rad
np.sin(90)
np.sin(np.linspace(-5, -5, 10))


# In[49]:

# to calculate dist between following points - shift df one step forward and calculate. shift(N) shifts left \ right
dist = earth_distance(df['lat'], df['lng'], df['lat'].shift(), df['lng'].shift())
dist.head()


# In[52]:

# do the same for time differences
dt = df['time'] - df['time'].shift()
dt.head()


# In[54]:

# diff function to do the same as above:
df['time'].diff().head()


# In[56]:

# calculate velocity - dist \ time
# speed = dist / dt  # won't work - dividing number by Timedelta variable - we need to convert to seconds before dividing
dt[1].total_seconds() / 3600  # (in Python 2 - 3600.0)


# In[57]:

import astropy.units  # adds units to numpy arrays and helps with conversions


# In[58]:

# another way to calculate time as scalar (divides the timedelta into sections of 1h. can be 5 min, or 3d - any time unit)
dt[1] / np.timedelta64(1, 'h')


# In[59]:

# final calculation of speed in km/h
dt = df['time'].diff() / np.timedelta64(1, 'h')
speed = dist / dt
speed.head()


# In[66]:

# the following line asks to show figures from matplotlib in this notebook
get_ipython().magic('matplotlib inline')
# %matplotlib notebook  # not stable yet, allows for zooming, etc,
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')  # change plot style globally


# In[67]:

speed.plot.box()  # speed is pandas Series and supports plots from matplotlib


# In[62]:

speed.plot.box();  # adding ; suppresses the axes printout


# In[65]:

ax = speed.plot.box(label='run')
ax.set_ylabel('speed (km/h)');


# In[68]:

with plt.style.context('ggplot'):  # change plot sytle only for this chart
    speed.plot.box()


# In[69]:

# jupyter notebook can be downloaded as python (file --> download as) and then converted into a module that can be used later


# In[73]:

# show variables
get_ipython().magic('who')
print('===')
get_ipython().magic('whos')


# In[74]:

# working with external files
"""
% run <path to file>
% run -n <path to file>
"""


# In[75]:

# conda install -c conda-forge folium


# In[76]:

import folium  # map package


# In[85]:

m = folium.Map(location=([df['lng'].mean(), df['lat'].mean()]), zoom_start=15)
marker = folium.CircleMarker([df['lng'].mean(), df['lat'].mean()])
marker.add_to(m)
m


# In[92]:

# NOTE: for columns where there is no space in the name: df['a'] == df.a
# tha main difference is in adding columns


# In[93]:

# use timestamp as index
df = pd.read_csv(track_pth, parse_dates=['time'], index_col='time')
df.head()


# In[96]:

df.loc["2015-08-20 03:48"]  # slicing on time range - using larger resolution on index (.loc can be removed, when its not provided, pd looks for column name and if there's no such column pd looks for the value in index column)


# In[97]:

# in this case, to calculate time difference we need to cast index as Series
pd.Series(df.index).diff().head()


# In[103]:

# resample data frame - you get resampler object
min_df = df.resample('1min')


# In[104]:

# what to do with all samples that were discarded to get from resampler to dataframe
min_df = min_df.mean()
min_df


# In[105]:

# write a function for placing markers per row
def add_marker(row):
    marker = folium.CircleMarker([row['lng'], row['lat']])
    marker.add_to(m)

m = folium.Map(location=([df['lng'].mean(), df['lat'].mean()]), zoom_start=15)
# apply per row
min_df.apply(add_marker, axis=1)
m


# In[106]:

# pandas allows conversion between timezones - see in solutions


# In[107]:

# extract row from df
df1.iloc[0]  # gives a Series where index is column names and values are column values


# In[108]:

df1.iloc[0:1]  # this returns the row as data frame by slicing the indices as reqested


# In[109]:

df1.iloc[[0, 2]]  # this slices the indices and returns dataframe


# In[110]:

df1.loc['a':'b']  # index slicing (loc)


# In[111]:

df1.loc['b':'b']  # requesting a single index


# In[ ]:



