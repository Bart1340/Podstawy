#!/usr/bin/env python
# coding: utf-8

# ### Line Graph

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


gas = pd.read_csv('gas_prices.csv')


# In[3]:


plt.figure(figsize=(8,5))

plt.title('Gas prices by year(in USD)')
plt.plot(gas.Year,gas.USA, 'b.-', label = "USA")
plt.plot(gas.Year,gas.Canada,'r.-', label = 'Canada')
plt.plot(gas.Year,gas['South Korea'], 'g.-', label = "South Korea")

plt.xlabel('Year')
plt.ylabel('USD')

#print(gas.Year)
print(gas.Year[ : :3])
plt.xticks(gas.Year[ : :3])

plt.legend()
plt.show()


# In[4]:


for country in gas:
    if country != 'Year':
        plt.plot(gas['Year'], gas[country], marker='.', label = country)
        plt.title('Gas prices by year(in USD)')
        plt.xlabel('Year')
        plt.ylabel('USD')
        plt.xticks(gas.Year[ : :3])
        plt.legend()
        
       


# In[ ]:





# In[5]:


Interesting_Countries = ['USA','Australia','Canada','South Korea']
for country in gas:
    if country in Interesting_Countries:
        plt.plot(gas['Year'], gas[country], marker='.', label = country)
        plt.title('Gas prices by year(in USD)', fontdict={'fontweight':'bold', 'fontsize':18})
        plt.xlabel('Year')
        plt.ylabel('USD')
        plt.xticks(gas.Year[ : :3].tolist()+[2011])
        plt.legend()
        
        plt.savefig('Gas.png', dpi=300)


# ## Fifa Data

# In[6]:


fifa = pd.read_csv('fifa_data.csv')


# In[7]:


fifa.head(5)


# ## Histograms

# In[8]:


bins = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(fifa['Overall'], bins = bins, color = '#abcdef')

plt.xticks(bins)

plt.xlabel('Skill level')
plt.ylabel('Number of players')
plt.title('Distribution of player skill')

plt.show()


# ## Pie charts

# In[9]:


left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]


# In[10]:


labels = ['Left','Right']
colors = ['#abcdef','#bbbbbb']

plt.pie([left,right], labels=labels, colors=colors, autopct='%.2f %%')
plt.title('Foot preference of Fifa players')


plt.show()


# In[11]:


fifa.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa.Weight]


# In[12]:


light = fifa.loc[fifa.Weight <125].count()[0]
medium_light = fifa.loc[(fifa.Weight >=125) & (fifa.Weight <150)].count()[0]
medium = fifa.loc[(fifa.Weight >=150) & (fifa.Weight <175)].count()[0]
medium_heavy = fifa.loc[(fifa.Weight >=175) & (fifa.Weight <200)].count()[0]
heavy = fifa.loc[fifa.Weight >200].count()[0]


# In[13]:


weights = [light,medium_light,medium,medium_heavy,heavy]
labels = ['Under 125','125-150','150-175','175-200','Over 200']
explode = (.4,.2,0,0,.4)

plt.style.use('ggplot')
plt.pie(weights, labels=labels, autopct='%.2f %%', pctdistance=0.8, explode=explode)
plt.title('Weight Distribution of Fifa players (in lbs)')

plt.show()


# In[14]:


barcelona = fifa.loc[fifa['Club'] == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa['Club'] == 'Real Madrid']['Overall']
revs = fifa.loc[fifa['Club'] == "New England Revolution"]['Overall']


# In[33]:


labels = ['FC Barcelona', 'Real Madrid', "NE Revolution"]

plt.style.use('default')

plt.figure(figsize = (5,8))

boxes = plt.boxplot([barcelona,madrid,revs],labels=labels,patch_artist=True)

for box in boxes['boxes']:
    box.set(color='#4286f4',linewidth=2)
    box.set(facecolor='#e0e0e0')

plt.title('Team Comparison')

plt.show()


# In[ ]:




