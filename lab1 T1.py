#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


z = np.random.uniform(-1, 1, 100)
z


# In[3]:


a = -17
b = 9


# In[4]:


x = np.random.uniform(-0.5, 0.5, 100)
y = a*x+b+z
plt.scatter(x, y)


# In[5]:


a1 = 1
b1 = 1
speed = 0.01


# In[6]:


def J1(a,b,x,y):
    j = 0
    for i in range(100):
        j+=2*(a*x[i]+b-y[i])*x[i]
    return j/(2*100)


# In[7]:


def J2(a,b,x,y):
    j = 0
    for i in range(100):
        j+=2*(a*x[i]+b-y[i])
    return j/(2*100)


# In[8]:


for i in range(10000):
    c1 = J1(a1,b1,x,y)
    c2 = J2(a1,b1,x,y)
    a1 = a1 - speed * c1
    b1 = b1 - speed * c2
    #print(c1,c2)


# In[9]:


plt.scatter(x, y, color = "green")
plt.plot(x,a1*x+b1, color = "red")


# In[10]:


a1


# In[11]:


b1


# In[ ]:




