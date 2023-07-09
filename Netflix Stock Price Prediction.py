#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


# In[2]:


data = pd.read_csv("D:\\Bharat intern\\Stock price prediction\\NFLX.csv")


# In[3]:


#INSPECTION~
print(data.head(10))
print(data.shape)

#convert string to pandas datetime, filtering only the date using '.dt.date'
pd.to_datetime(data['Date']).dt.date


# In[4]:


print(data.describe())
print(data.info())
print(data.isnull().sum())
#no missing values


# In[5]:


data['Datetime'] = pd.to_datetime(data['Date'])
data = data.set_index('Datetime')


# In[6]:


plt.figure(figsize=(15, 5))
plt.xticks(rotation = 45)
plt.plot(data['Adj Close'])
plt.title('Netflix stock price for 5 years')
plt.ylabel('Price', fontsize=18)
plt.xlabel('Year', fontsize=18)


# In[7]:


#subplots for different variables against datetime
data.plot(subplots=True)


# # Project Objective: To find out whether buying on Friday and selling on Monday is profitable.

# for each of the fri-mon pair 
# * Take (mon - fri) / fri to get % change
# * Each of this is 1 data point
# * Plot histo of all data points to get overall distribution

# In[8]:


data['Day'] = pd.to_datetime(data['Date']).dt.weekday
data
#0: Monday, 1: Tues, 2: Wed, 3: Thurs, 4: Fri


# In[9]:


#filtering mondays and fridays
filter_df = data[(data['Day'] == 0) | (data['Day'] == 4)]
filter_df = filter_df.sort_values('Date').reset_index(drop=True)
filter_df['DateTime'] = pd.to_datetime(filter_df['Date'])
filter_df['diff_days'] = filter_df['DateTime'].diff()
filter_df.head(10)
info_df = pd.DataFrame(columns=['buy_date', 'sell_date', 'buy_px', 'sell_px'])
for i in range(len(filter_df)):
    if filter_df.loc[i, 'diff_days'].days == 3:
        info_df = info_df.append(
        {
            'buy_date': filter_df.loc[i-1, 'Date'], 
            'sell_date':filter_df.loc[i, 'Date'], 
            'buy_px':filter_df.loc[i-1, 'Adj Close'], 
            'sell_px':filter_df.loc[i, 'Adj Close']
            
        },ignore_index=True
        )


# In[10]:


info_df['pct'] =  ((info_df['sell_px'] - info_df['buy_px']) / info_df['buy_px']) *100


# In[11]:


info_df['pct'].plot.hist()


# In[12]:


info_df['pct'].describe(percentiles = np.arange(0,1,0.1))


# **On average we will make 0.210645% profit if we buy on Friday close and sell on the subsequent Monday close. This is unlikely to be a profitable strategy after transaction cost.**
# 
# *But the distribution of % difference is positively skewed.*

# In[ ]:





# In[ ]:





# In[ ]:




