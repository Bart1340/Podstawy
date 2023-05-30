#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# ## The Basics

# In[2]:


a = np.array([1,2,3])
a


# In[3]:


b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
b


# In[4]:


# Get Dimensions
a.ndim
b.ndim


# In[5]:


# Get Shape
a.shape
b.shape


# In[6]:


# Get Type
a.dtype
b.dtype


# In[7]:


# Get Size
a.itemsize
b.itemsize


# In[8]:


# Get total size
a.nbytes
b.nbytes


# ## Accessing/Changing specific elements, rows, columns, etc

# In[9]:


a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
a.shape


# In[10]:


# Get a specific element [row, column]
a[1,5]
a[1,-2]


# In[11]:


# Get a specific row
a[0,:]


# In[12]:


# Get a specific column
a[:,2]


# In[13]:


# [Start:End:Stepsize]
a[0,1:6:2]


# In[14]:


# Replacing values
a[1,5] = 20
a[:,2] = [1,2]
print(a)


# In[15]:


# 3D Example


# In[16]:


b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)


# In[17]:


# Get a specific elements (work outside in)
b[0,1,1]


# In[18]:


# replace
b[:,1,:] = [[9,9],[8,8]]
b


# ## Initializing different types of arrays

# In[19]:


# All zeros matrix
np.zeros(5)


# In[20]:


np.zeros((2,3))


# In[21]:


# All 1 matrix
np.ones(5)


# In[22]:


# Any other number
np.full((2,2),99)


# In[23]:


# Like an existing array
np.full_like(a,4)


# In[24]:


# Random Numbers Array (decimal numbers)
np.random.rand(4,2,3)


# In[25]:


# Random like and existing array
np.random.random_sample(a.shape)


# In[26]:


# Random Numbers Array (integer numbers)
np.random.randint(-4,8,size=(3,3))


# In[27]:


# Identity matrix
np.identity(4)


# In[28]:


# Repeat an array
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3, axis=0)
print(r1)


# In[34]:


# Manually typing
np.array([[[[[1,1,1,1,1],[1,0,0,0,1],[1,0,9,0,1],[1,0,0,0,1],[1,1,1,1,1]]]]])


# In[39]:


# Smarter way
output = np.ones((5,5))
print(output)

z= np.zeros((3,3))
z[1,1] = 9
print(z)

output[1:4,1:4] = z
print(output)


# ## Be careful when copying arrays

# In[44]:


#Not like that
a=np.array([1,2,3])
b=a
print(b)
b[0] = 100
print(b)
print(a)


# In[45]:


# Use .copy function
a=np.array([1,2,3])
b=a.copy()
print(b)
b[0] = 100
print(b)
print(a)


# ## Math

# In[46]:


a = np.array([1,2,3,4])
print(a)


# In[47]:


a+2


# In[48]:


a - 2


# In[49]:


a * 2


# In[50]:


a / 2 


# In[51]:


a ** 2


# In[52]:


b = np.array([1,0,1,0])
a+b


# In[53]:


np.sin(a)


# In[54]:


np.cos(a)


# ## Linear Algebra

# In[59]:


a = np.ones((2,3))
print(a)
b = np.full((3,2),2)
print(b)

np.matmul(a,b)


# In[60]:


# Find the determinant
c=np.identity(3)
np.linalg.det(c)


# ## Statistics 

# In[62]:


stats  = np.array([[1,2,3],[4,5,6]])
stats


# In[67]:


np.min(stats)


# In[68]:


np.min(stats, axis=1)


# In[70]:


np.max(stats)


# In[72]:


np.max(stats, axis=1)


# In[73]:


np.sum(stats)


# In[74]:


np.sum(stats, axis = 0)


# ## Reorganizing Arrays 

# In[78]:


before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((8,1))
print(after)

after2 = before.reshape((2,2,2))
print(after2)


# ## Vertically stacking vectors

# In[80]:


# Vertical stack
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

np.vstack([v1,v2])


# In[84]:


# Horizontal stack
h1 = np.ones((2,4))
h2 = np.zeros((2,4))

print(h1)
print(h2)

np.hstack([h1,h2])


# ## Miscellaneous

# In[88]:


# Load Data from file
filedata = np.genfromtxt('data.txt', delimiter=',')
print(filedata)


# In[91]:


# Boolean masking and advanced indexing
filedata > 5


# In[92]:


filedata[filedata>5]


# In[95]:


# You can index with a list in NumPY
a = np.array([1,2,3,4,5,6,7,8,9])
a[[1,2,8]]


# In[98]:


np.any(filedata > 5)


# In[102]:


np.any(filedata > 5, axis=0)


# In[104]:


np.all(filedata > 5, axis=0)


# In[106]:


((filedata > 5) & (filedata <10))


# In[109]:


(~((filedata > 5) & (filedata <10)))


# In[ ]:


#a[2:4,0:2]
#a[[0,1,2,3],[1,2,3,4]]
#a[[0,4,5],3:]

