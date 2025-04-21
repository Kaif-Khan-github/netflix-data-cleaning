#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


data=pd.read_csv("netflix_titles.csv")


# In[3]:


data.head()


# In[6]:


#clean the column name by removing extra space
data.columns=data.columns.str.strip()


# In[8]:


#removing the extra space from text columns
str_cols=data.select_dtypes(include='object').columns
data[str_cols]=data[str_cols].apply(lambda x: x.str.strip())


# In[10]:


#remove the duplicate rows
data.drop_duplicates(inplace=True)


# In[26]:


#For columns with missing values (blank cells), we fill them with "Unknown"
columns = ["director", "cast", "country", "date_added", "rating"]
data[columns] = data[columns].fillna("Unknown")


# In[28]:


# Turn the date added columns into real dates like (2021-03-01)
data["date_added"] = pd.to_datetime(data['date_added'], errors= "coerce")


# In[29]:


#create a new column that only show the year netflix added that title like 2020 , 2023
data["year_added"] = data["date_added"].dt.year


# In[31]:


#making all value in the rating columns uppercase
data['rating'] = data['rating'].str.upper()


# In[32]:


#extract the number from duration
data['duration_num'] = data['duration'].str.extract('(\d+)').astype("float")


# In[33]:


#exracting text part from duration
data['duration_type']=data['duration'].str.extract('([a-zA-Z]+)')


# In[34]:


#Resets the index to keep it clean. Like re-numbering the rows from 0, 1, 2… after all the removals.
data.reset_index(drop=True, inplace=True)


# In[37]:


#saving the clean version  as a new csv file 
data.to_csv("cleaned_netflix_titles.csv", index = False)
print(" Cleaned and saved as 'cleaned_netflix_titles.csv'")


# In[38]:


get_ipython().system('jupyter nbconvert --to script "cleaned_netflix_titles.csv')


# In[ ]:




