#!/usr/bin/env python
# coding: utf-8

# # PA 3 - PYTHON DATA ANALYSIS (PANDAS)
# ------

# ##### NO. 1 `PROBLEM 1`
# ------

# In[11]:


import pandas as pd


# In[12]:


#READ THE CSV FILE
CARS = pd.read_csv('cars-PA3.csv')
CARS


# In[13]:


#BY THE FUNCTION .HEAD AUTOMATICALLY DISLAY THE FIRST 5 ROWS OF DATA
CARS.head()


# In[7]:


#BY THE FUNCTION .HEAD AUTOMATICALLY DISLAY THE LAST 5 ROWS OF DATA
CARS.tail()

