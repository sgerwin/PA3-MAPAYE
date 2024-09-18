#!/usr/bin/env python
# coding: utf-8

# # EXPERIMENT 3: PYTHON DATA ANALYSIS (PANDAS)
# #### MAPAYE, SHERWIN MIGUEL C.

# ### PROBLEM 1: Save your file as Surname_Pandas-P1.py
# #### Using knowledge obtained from the experiment and demonstrations:
# ###### a. Load the corresponding .csv file into a data frame named cars using pandas

# In[2]:


import pandas as pd


# In[3]:


# Read cars data from CSV file into dataframe
cars=pd.read_csv("cars.csv")
# Output of dataframe
cars


# ###### b. Display the first five and last five rows of the resulting cars.

# In[4]:


# Display the first five rows of the cars dataframe
cars.head()


# In[5]:


# Display the last five rows of the cars dataframe
cars.tail()

