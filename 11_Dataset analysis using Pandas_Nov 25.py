#!/usr/bin/env python
# coding: utf-8

# # Pandas
# Pandas is a Python library used for working with data sets
# Pandas has functions for analyzing, Cleaning,exploring and manipulating the data.
# The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.
# Pandas used to analyze big data,Pandas can clean messy data sets and make them readable and relavent
# to find the missing values,Alignment,Group by,Slicing and Indexing on the given data frame.

# In[1]:


import pandas as pd


# In[3]:


data = pd.read_csv(r'/Users/aviswe/Desktop/FSDS/Old/01FSDS/Morning Batch/Sample Superstore Orders.csv')


# In[4]:


data


# In[5]:


data.shape #Returns the shape of the dataset


# In[6]:


len(data) #Returns the length of the entire dataset


# In[8]:


pd.__version__ #Pandas version on my machine


# In[9]:


data.columns #Returns the column names fromt the entire dataset


# In[10]:


len(data.columns) #Returns the length of the entire dataset columns


# In[11]:


type(data) # Returns the type of data


# In[13]:


id(data) # Returns the id of data


# In[15]:


data.info() # Returns the each column information from the entire dataset


# In[16]:


data.dtypes #Returns the each column data types from the dataset


# In[17]:


data.isnull() # Returns the null values from the dataset


# In[18]:


data.isnull().sum() #Returns the sum of the null values by column wise in the dataset.


# In[21]:


data.isna().sum() #Returns the sum of the null values by column wise in the dataset.


# In[22]:


data.head() #returns the top 5 rows from the dataset. 


# In[23]:


data.tail() # Returns the bottom 5 rows from the dataset


# In[24]:


data[10:21] # returns the rows from 10 to 20 from the dataset


# In[25]:


data[::10] # Returns every 10th row from start to end of the dataset.


# In[26]:


data.columns #Returns the column names in the dataset.


# In[28]:


data['Category'] #Returns the entire Dataset values for the column named 'Category'


# In[29]:


data[['Category','City']] # Returns the entire dataset values for the columns named 'Category','City'


# In[30]:


data['Ship Mode'] #Returns the entire dataset values for the column named 'Ship Mode'


# In[31]:


#Created Categoriical and Numerical datasets
data_cat = data[['Category', 'City', 'Country/Region', 'Customer Name', 'Manufacturer',
       'Order Date', 'Order ID', 'Postal Code', 'Product Name', 'Region',
       'Segment', 'Ship Date', 'Ship Mode', 'State/Province', 'Sub-Category']]
data_num = data[['Discount', 'Profit', 'Quantity', 'Sales']]


# In[32]:


data_cat #Categorical dataset from the entire dataset


# In[33]:


data_num #Numerical data set from the entire dataset


# In[34]:


print(len(data.columns)) #Returns the length of the entire dataset
print(len(data_cat.columns)) #Returns the length of the Categorical data frame from entire data set
print(len(data_num.columns)) # Returns the length of the Numerical data frame from the entire data set


# In[35]:


data_num.head() #Returns the top 5 rows from the numerical dataset


# In[36]:


data_cat.head() #Returns the top 5 rows fromt the categorical dataset


# In[37]:


data_cat.info() #Returns the categorical dataset columns information 


# In[38]:


data_num.info() #Returns the numerical dataset columns information


# In[39]:


data_num.head(1) #Returns the top one row from the numerical dataset


# In[40]:


data_cat.head(1) #Returns the top one row from the categorical dataset


# In[41]:


data_num.head(0) #Returns the headers from the numerical dataset


# In[42]:


data_cat.describe() #Descriptive  statistics information of categorical dataset


# In[43]:


data_num.describe() # Descriptive statistics informaton of Numerical dataset


# In[44]:


data.describe() #By default describe gives the Numerical data analysis.
#if user wants categorical statistics we need to specifically mention the Categorical data.


# In[ ]:




