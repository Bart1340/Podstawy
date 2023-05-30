#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df1 = pd.read_csv("Datatoclear.csv",sep=";")


# In[3]:


pd.set_option('display.max_rows', 250)


# In[4]:


df1.head


# In[5]:


df1['age'].fillna(999, inplace=True)
df1.loc[df1['age'] == "370z", 'age'] = 999
df1['age'] = df1['age'].astype(int)
df1.loc[df1['age']>120, 'age'] = 999
df1.head(250)


# In[6]:


df1 = df1[df1['age'] != 999]
df1.head(250)


# In[7]:


df1 = df1[df1['gender'].isin(['m', 'k'])]
df1.head(250)


# In[8]:


df1 = df1[~df1['answer1'].isnull()]
df1 = df1[~df1['answer1'].astype(str).str.contains(r'[a-zA-Z]')]
df1['answer1'] = df1['answer1'].astype(int)
df1.head(250)


# In[9]:


df1 = df1[~df1['answer2'].isnull()]
df1['answer2'] = df1['answer2'].astype(int)
df1.head(250)


# In[10]:


df1 = df1[~df1['answer3'].isnull()]
df1['answer3'] = df1['answer3'].astype(int)
df1.head(250)


# In[11]:


df1 = df1[~df1['answer4'].isnull()]
df1 = df1[~df1['answer4'].astype(str).str.contains(r'[a-zA-Z]')]
df1['answer4'] = df1['answer4'].astype(int)
df1.head(250)


# In[12]:


df1 = df1[~df1['answer5'].isnull()]
df1['answer5'] = df1['answer5'].astype(int)
df1.head(250)


# In[13]:


df1 = df1.drop('Unnamed: 7', axis=1)
df1.to_excel('cleared.xlsx', index=False)


# In[14]:


df1.head(250)
df1.describe()

