#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
nabil = pd.read_csv('nabil.csv')


# In[15]:


nabil = pd.read_csv('nabil.csv', header= 0, index_col= 'Date', parse_dates=True)


# In[18]:


nabil.head(n=15)


# In[21]:


nabil.tail(n=15)

