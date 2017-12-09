
# coding: utf-8

# In[1]:

pth = r"C:\Users\anat.shkolyar\PycharmProjects\pandas_workshop\data\taxi.csv.bz2"  # slice of NY taxi DB (full avilable on Google, Amazon)


# In[2]:

get_ipython().magic('matplotlib inline')
import pandas as pd


# In[8]:

# see file size
from os.path import getsize

print('size = {:.2f}mb'.format(getsize(pth)/ (1<<20)))


# In[11]:

# jupyter extension (magic commands)
get_ipython().system('dir $pth')


# In[17]:

# load file (note that it takes time. * appears near to [In] and top right circle fills)
df = pd.read_csv(pth)
len(df)


# In[18]:

# look at data - the csv is problematic, see VendorId, Name values (etc)
df.iloc[0]


# In[22]:

# look at file content
import bz2

with bz2.BZ2File(pth) as fp:
    header = fp.readline()
    data = fp.readline()
    
# Python 3 only:
header = header.decode('utf-8')
data = data.decode('utf-8')
    
print(header)

print(data)


# In[26]:

# number of columns and values do not match
columns = header.split(',')
values = data.split(',')

len(columns), len(values)


# In[28]:

# only use first 21 columns - the values make more sense
import numpy as np

df = pd.read_csv(pth, usecols=np.arange(21))
df.iloc[0]


# In[29]:

df.dtypes  # check column types


# In[36]:

# parse times
df = pd.read_csv(pth, usecols=np.arange(21), parse_dates=['lpep_pickup_datetime', 'Lpep_dropoff_datetime'])
df.columns = [col.strip() for col in df.columns]  # remove spaces
df.dtypes


# # Header of Markdown cell
# 
# * item 1
# * item 2
# 
# [google](https://google.com)
# 
# $ sinc = \frac{sin(x)}{x} $
# 
# supports latex, free text, use jupyter to create a report in html and send the file
# 

# # Question: How many rides per VendorID?

# In[38]:

# numpy and pandas do not copy variables, but provide views on same variable
df.groupby('VendorID').count()['Trip_type']  # select a single column because the count returns sae value in all columns


# In[39]:

df.groupby('VendorID')['Trip_type'].count()  # colunm selection before or after count


# In[40]:

df['VendorID'].value_counts()  # pandas method to calculate the same without groupby - works on Series


# In[41]:

# pd.cut - for binning 
pd.cut(df['Total_amount'], 10)  # for each row shows the bin it belongs to. note bin list at the end of output.


# In[42]:

# histogram
df.groupby(pd.cut(df['Total_amount'], 10))['Trip_type'].count()  # select any column for counting


# In[43]:

pd.cut(df['Total_amount'], 10).value_counts()  # using value counts


# esc + p shows jupyter command pallette
# esc + any letter from pallette perform that action
# 

# 
# # Median Number of Rides in Hour of Day
# 

# In[44]:

df.head()


# In[50]:

# assume pickup time is the ride time

# divide info into days
# in each day, count rides per hour
# median on days

# create new columns of day and hour
df['weekday'] = df['lpep_pickup_datetime'].dt.weekday
df['hour'] = df['lpep_pickup_datetime'].dt.hour

df[['weekday', 'hour']].head()


# In[61]:

# group by day and hour

rides_per_day_hour = df.groupby(['weekday', 'hour'])['VendorID'].count()
rides_per_day_hour.head()


# In[63]:

rides_per_day_hour = rides_per_day_hour.unstack()
rides_per_day_hour


# In[67]:

medians_per_hour = rides_per_day_hour.apply(np.median)
medians_per_hour.head()


# In[72]:

# groupby on more than one column creates a multi-index DataFrame
# unstack - separates the multi index into rows and columns (but it is complicated for more than 2 groupby column and thus not recommended)
# then median on days in the resulting data frame gives us the required result.

# a better way to solve this:
count = df.groupby(['weekday', 'hour'], as_index=False).count()  # as_index=False - does not stack the columns into multi index
count.head()


# In[74]:

# group the result of first groupby, the counts, by hour, then select a single column and perform median
hourly = count.groupby('hour').median()['VendorID']  # select one column
hourly.head()


# In[81]:

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (10, 6)  # in inches
ax = hourly.plot.bar(rot=45)
ax.set_xlabel('Hour')
ax.set_title('Median Hourly Rides');
ax.set_ylabel('# rides')

# in solutions there is also a breakdown by vendors


# ## Box Plot per VendorID of Daily Earnings
# 
# 2 boxplots, one per vendor, present daily earnings

# In[84]:

# we can do this by 2 group by steps, but also through PIVOT

edf = df[['VendorID', 'Total_amount', 'weekday']]
pivot_edf = edf.pivot_table(index='weekday', columns='VendorID', values='Total_amount', aggfunc=np.sum)
# create a new dataframe pivot from edf, define index as the day, columns as vendor, values as the total amount, and aggregation function indicates what to do for values that fall into same bin of column and index
pivot_edf.plot.box();


# In[ ]:



