#!/usr/bin/env python
# coding: utf-8

# # PA 3 - PYTHON DATA ANALYSIS (PANDAS)
# ------

# ##### NO. 2 `PROBLEM 2`
# ------

# In[17]:


import pandas as pd


# In[18]:


#READ CSV FILE AND SHOW DATA
CARS = pd.read_csv('cars-PA3.csv')
CARS


# In[19]:


#DO THE CONDITION FOR .ILOC
CARS.iloc[:5, 1::2]


# In[20]:


#WILL USE BOOLEAN INDEXING TO FILTER ROWS
CARS[CARS['Model'] == 'Mazda RX4']


# In[21]:


#LOCATE SPECIFIC MODEL AND SPECIFIC CYL
CARS.loc[CARS['Model'] == 'Camaro Z28',
        ['Model','cyl']]


# In[22]:


#USE .ISIN TO FILTER MULTIPLE MODELS, THEN SELECT SPECIFIC COLUMNS TO SHOW
CARS.loc[CARS['Model'].isin(['Mazda RX4', 'Ford Pantera L', 'Honda Civic']), ['cyl', 'gear']]

