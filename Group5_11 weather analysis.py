#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("C:\\Users\\INDIA\\OneDrive\\Desktop\\Pyt\\11-weatherAUS.csv")


# In[3]:


df.head()


# In[4]:


#Calculate  no of row and columns
df.shape


# In[5]:


#Checking for duplicates values
df.duplicated().sum()


# In[6]:


#finding out the data type of each varible
df.dtypes


# In[7]:


df.columns


# In[27]:


#Checking For Duplicated values
df.duplicated().sum()


# In[28]:


#Finding out data type of each variable
df.dtypes


# In[60]:


#Shows statistical summary of the numeric variables in the dataset

df.describe().round()


# In[29]:


df.info


# In[30]:


df.describe()  # checking descripion


# In[59]:


df.isnull().sum()  #checking missing values


# In[11]:


df.dropna()


# In[10]:



df.head()


# In[9]:


# Exploring Targeted Variable 

sns.countplot(df["RainTomorrow"])


# In[52]:


sns.countplot(df["RainToday"])


# In[18]:


sns.distplot(df['WindGustSpeed'])


# In[19]:


sns.distplot(df['Rainfall'])


# In[20]:


sns.distplot(df['MinTemp'])


# In[21]:


sns.distplot(df['MaxTemp'])


# In[55]:


plt.figure(figsize=(15,20))
sns.boxplot(x='Rainfall',y='Location',data = df)


# In[47]:


sns.jointplot(x='WindGustSpeed',y='Rainfall', data= df)


# In[51]:


sns.pairplot(df)


# In[61]:


mx=df.corr()


# In[13]:


sns.jointplot(x='MaxTemp',y='MinTemp', data= df)


# In[57]:


plt.figure(figsize=(10,20))
df1 = df.sample(800)
sns.swarmplot(x='Rainfall',y='Location',data=df1)


# In[58]:


plt.figure(figsize=(10,20))
plt.scatter('WindGustSpeed','Location',data=df)
plt.xlabel('WindGustSpeed')
plt.ylabel('Location')


# In[ ]:




