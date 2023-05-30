#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# ## Basic Graph

# In[81]:


x = [0,1,2,3,4]
y = [0,2,4,6,8]

#resize (dpi - pixels per inch, figsize - dimensions)
plt.figure(figsize=(5,3), dpi=150)

#Base Graph
plt.plot(x,y, label = '2x', color ="red", linewidth = 2, linestyle = '--', marker = '.', markersize = 10, markeredgecolor = 'blue')

# Title + Labels
plt.title('Title', fontdict={'fontname': 'Times New Roman', 'fontsize':15})
plt.xlabel('x')
plt.ylabel('y')

#Line number two (with numpy)

#Interval to plot points
x2 = np.arange(0,4.5,0.5) 
print(x2)

#Plot part of the graph as a line
plt.plot(x2[:6],x2[:6]**2, 'b', label = "x^2")

#Plot the rest of the graph
plt.plot(x2[5:],x2[5:]**2, 'b--')

#Graph Ticks (Scale of the graph)
plt.xticks([0,1,2,3,4])
#plt.yticks([0,2,4,6,8])

#Legend
plt.legend()

#Save Graph
plt.savefig('Graph1.png', dpi = 300)

plt.show()


# ### Shorthand notation
# fmt = '[color][marker][line]'

# In[41]:


x = [0,1,2,3,4]
y = [0,2,4,6,8]

plt.plot(x,y, 'b*--', label = '2x')

plt.title('Title', fontdict={'fontname': 'Times New Roman', 'fontsize':15})
plt.xlabel('x')
plt.ylabel('y')

plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8])

plt.legend()



plt.show()


# ## Bar Chart

# In[92]:


labels = ['A','B','C']
values = [1,4,2]

plt.bar(labels,values)
bars = plt.bar(labels,values)

bars[0].set_hatch('/')
bars[1].set_hatch('O')
bars[2].set_hatch('*')

plt.figure(figsize = (6,4))


plt.show()


# In[115]:


labels = ['A','B','C']
values = [1,4,2]
plt.bar(labels,values)
bars = plt.bar(labels,values)

bars[0].set_hatch('/')
bars[1].set_hatch('O')
bars[2].set_hatch('*')

plt.figure(figsize = (6,4))


plt.show()


# In[109]:





# In[ ]:




