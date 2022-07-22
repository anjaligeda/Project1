#!/usr/bin/env python
# coding: utf-8

# In[15]:


#importing the library of numpy
import numpy as np


# In[27]:


#importing the csv file
taxi=np.genfromtxt('nyc_taxis.csv',delimiter=',',skip_header=True)
taxi


# In[18]:


#calculating the mean speed of all rides
speed=taxi[:,7]/(taxi[:, 8]/3600)


# In[19]:


mean_speed=speed.mean()
print(mean_speed)


# In[20]:


#calculate the number of rides taken in the month of february  and it is given the 2 month column
rides_feb=taxi[taxi[:,1]==2,1]
print(rides_feb.shape[0])


# In[21]:


#calculating the number of rides where tip was more than $50
print(taxi[taxi[:,-3]>50,-3].shape[0])


# In[26]:


#calculating the number of rides where drop as JFK airport
print(taxi[taxi[:,6]==2,6].shape[0])


# In[ ]:




