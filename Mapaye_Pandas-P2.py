#!/usr/bin/env python
# coding: utf-8

# # EXPERIMENT 3: PYTHON DATA ANALYSIS (PANDAS)
# #### MAPAYE, SHERWIN MIGUEL C.

# ### PROBLEM 2: Save your file as Surname_Pandas-P2.py
# #### Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.

# In[1]:


import pandas as pd


# In[3]:


# Read cars data from CSV file into dataframe
cars=pd.read_csv("cars.csv")


# ###### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

# In[15]:


# Selects every second row starting from index 1 and displays the first five rows
cars.iloc[1::2].head()


# ###### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

# In[16]:


# Selects rows where the 'Model' is 'Mazda RX4'
cars.loc[cars['Model'] == 'Mazda RX4']


# ###### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

# In[17]:


# Selects row where the 'Model' is 'Camaro Z28' and display only the 'Model' and 'cyl' column
cars.loc[cars['Model'] == 'Camaro Z28',['Model','cyl']]


# ###### d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# In[14]:


# Selects the 'Model', 'cyl', and 'gear' for the specific car model
cars.loc[(cars['Model'] == 'Mazda RX4 Wag') | 
         (cars['Model'] == 'Ford Pantera L') | 
         (cars['Model'] == 'Honda Civic'), ['Model', 'cyl', 'gear']]

