#!/usr/bin/env python
# coding: utf-8

# # NumPy is a robust tool for image processing in Python. It lets you manipulate images using array operations. This article explores several image processing techniques using NumPy.

# In[1]:


import numpy as np # Used for numerical operations on Arrays


# In[17]:


ones_arr = np.ones((5,5),dtype= int)


# In[18]:


ones_arr


# In[19]:


ones_arr*255


# In[2]:


import matplotlib.pyplot as plt # used to display the Image


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


from PIL import Image #Python Imaging Library used for opening and manipulating the images


# In[51]:


# Load the image using PIL (Python Imaging Library
ele = Image.open(r'/Users/aviswe/Desktop/FSDS/Old/01FSDS/Morning Batch/Elephant.jpg')


# In[52]:


ele


# In[53]:


type(ele)


# In[54]:


# Convert the image to a NumPy array
ele_arr = np.asarray(ele)


# In[55]:


ele_arr


# In[56]:


plt.imshow(ele_arr) # showing the Numpy array with axis


# In[57]:


ele_arr.shape # returns the shape of the image


# In[58]:


ele_red = ele_arr.copy() # copy the Numerical array to ele_red variable


# In[59]:


ele_red


# In[60]:


ele_arr == ele_red # comparing two numerical arrays


# In[61]:


plt.imshow(ele_red) # showing the copied numerical array image


# In[62]:


ele_red.shape


# In[63]:


#R G B
plt.imshow(ele_red[:,:,0])


# In[64]:


ele_red[:,:,0]


# In[65]:


plt.imshow(ele_red[:,:,0],cmap = 'Greys')


# In[95]:


plt.imshow(ele_red[:,:,0], cmap="Purples")


# In[67]:


plt.imshow(ele_red[:,:,1], cmap='YlGn')


# In[68]:


ele_red[:,:,0]


# In[69]:


ele_red[:,:,1]


# In[70]:


ele_red[:,:,2]


# In[71]:


ele_red[:,:,1] = 0


# In[72]:


ele_red[:,:,1]


# In[73]:


plt.imshow(ele_red)


# In[77]:


ele


# In[ ]:




