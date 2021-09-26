#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


mean_1 = [1, 2]
cov_1 = [[1, 0], [0, 1]]
x_1 = np.random.multivariate_normal(mean_1, cov_1, 100)
mean_2 = [4, 5]
cov_2 = [[2, 0], [0, 2]]
x_2 = np.random.multivariate_normal(mean_2, cov_2, 100)


# In[3]:


plt.scatter(x_1[:,0], x_1[:,1], color = "green")
plt.scatter(x_2[:,0], x_2[:,1], color = "red")


# In[4]:


abc = [*[[*x,1] for x in x_1],*[[*x,0] for x in x_2]]
import random
random.shuffle(abc)


# In[5]:


a = b = c = 0
speed = 0.1


# In[6]:


abcx = [[x[2], 1/(1 + np.exp(-x[0] * a - x[1] * b - c))] for x in abc]


# In[7]:


def cost(abcx,abc):
    c = [0]*2
    d1 = c1 = 0
    for i in range(200): 
        d1 = (abcx[i][0]-abcx[i][1])
        for j in range(2):
            c[j] += d1*abc[i][j]
        c1 += d1
    return(c[0],c[1],c1)


# In[8]:


for i in range(1000):
    c1 = cost(abcx,abc)
    a+=speed*c1[0]
    b+=speed*c1[1]
    c+=speed*c1[2]
    print(c1)
    abcx = [[x[2], 1/(1 + np.exp(-x[0] * a - x[1] * b - c))] for x in abc]


# In[9]:


a


# In[10]:


b


# In[11]:


c


# In[12]:


x = np.linspace(-2, 6, 2)
y = -a*x/b-c/b


# In[13]:


plt.scatter(x_1[:,0], x_1[:,1], color = "green")
plt.scatter(x_2[:,0], x_2[:,1], color = "red")
#plt.plot(x_1[:,0], -a*x_1[:,0]/b-c/b)
plt.plot(x,y)


# In[14]:


abcx


# In[15]:


zzz1 = [1 if x[1] >= 0.5 and x[0] == 1 else 1 if x[1] < 0.5 and x[0] == 0 else 0 for x in abcx]
np.sum(zzz1)/len(zzz1)


# In[ ]:




