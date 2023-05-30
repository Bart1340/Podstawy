#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/lego_sets.csv')
theme = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/parent_themes.csv')

pd.set_option('display.max_rows', 100)


# In[2]:


df.head(50)


# In[3]:


theme.head(50)


# ## What percentage of all licensed sets ever released were Star Wars themed?

# In[4]:


pd.set_option('display.max_rows', 100)
df


# In[5]:


theme


# In[6]:


theme = theme.rename(columns={'name':'parent_theme'})
theme


# In[7]:


Merged = pd.merge(df,theme,how='left',on='parent_theme')
Merged.head(50)

# Merge without changing names 
# Merged = df.merge(theme,left_on='parent_theme',right_on='name')


# ## First option

# In[8]:


print(Merged.loc[Merged['is_licensed'] == True].count())
Licensed = Merged.loc[Merged['is_licensed'] == True].count()[0]
print(Licensed)


# In[9]:


#Star_Wars = Merged.loc(([Merged['is_licensed'] == True]) & ([Merged['parent_theme'] == 'Star Wars']))
#print(Star_Wars)
print(Merged.loc[Merged['parent_theme'] == 'Star Wars'].count())
Star_Wars = Merged.loc[Merged['parent_theme'] == 'Star Wars'].count()[0]
print(Star_Wars)


# In[10]:


SW_percent = Star_Wars/Licensed
print(SW_percent)


# ## Second option

# ### Checking for null values

# In[11]:


Merged[Merged['set_num'].isnull()].shape


# In[16]:


licensed = Merged[Merged['is_licensed']]
licensed = licensed.dropna(subset=['set_num'])
#licensed.head()

Star_wars = licensed[licensed['parent_theme'] == 'Star Wars']
#Star_wars.head()

print(Star_wars.shape[0])
print(licensed.shape[0])
SW_percent = (Star_wars.shape[0])/(licensed.shape[0])
print(SW_percent)


# In[ ]:


the_force = 52


# ## In which year was Star Wars not the most popular licensed theme (in terms of number of sets released that year)?

# In[13]:


licensed_sorted = licensed.sort_values('year')


# In[15]:


licensed_sum = licensed_sorted.groupby(['year', 'parent_theme']).sum().reset_index()
licensed_final = licensed_sum.sort_values('is_licensed', ascending=False).drop_duplicates(['year'])
licensed_final.sort_values('year', inplace=True)
licensed_final


# In[45]:


new_era = 2017


# ## Pivot Table

# In[44]:


Pivot = licensed.pivot_table(index = 'year', columns='parent_theme', values='set_num', aggfunc='count')
Pivot


# ## Bonus Task
# ### Number of sets by year

# In[23]:


#Merged.head(50)


# In[40]:


clean_merged = Merged[~Merged['set_num'].isnull()]
clean_merged.head(50)
sorted_merged = clean_merged.sort_values('year')
sorted_merged['count'] = 1
summed_merged = sorted_merged.groupby('year').sum().reset_index()[['year','count']]
summed_merged.sort_values('count', ascending=False)


# In[ ]:




