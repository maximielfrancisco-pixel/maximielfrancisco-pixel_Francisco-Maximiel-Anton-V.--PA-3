#!/usr/bin/env python
# coding: utf-8

# # PA 3 - PYTHON DATA ANALYSIS (PANDAS)
# ------

# ##### NO. 2 `PROBLEM 2`
# ------

# In[14]:


import pandas as pd


# In[15]:


CARS = pd.read_csv('cars-PA3.csv')
CARS


# In[6]:


CARS.iloc[:5, 1::2]


# In[7]:


CARS[0:1]


# In[13]:


CARS.loc[CARS['Model']
        =='Camaro Z28',
        ['Model','cyl']]


# In[10]:


CARS.loc[[1,28,18],['Model','cyl','gear']]

