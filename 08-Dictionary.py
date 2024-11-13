#!/usr/bin/env python
# coding: utf-8

# # Dictionary

# In[1]:


#Create a empty Dictionary
d1={}
d1


# In[2]:


type(d1)


# In[3]:


#Another way of creating dictionary
d2 = dict()
d2


# In[4]:


type(d2)


# In[6]:


d1={1:'Apple',2:'Banana',3:'Cherry'} # Dictionary with integer keys
d1


# In[7]:


d2 = dict({4:'Dragon_Fruit',5:'egg_fruit'})
d2


# In[9]:


d3 = {'a':'one','b':'two','c':'three'} #Dictionary with Character Keys
d3


# In[10]:


d4 = {1: 'one', 'b':'two',3:'three'} #Dictionary with Mixed Keys
d4


# In[11]:


d1.keys() #Returns dictionary keys with keys() keyword


# In[12]:


d1.values() # Returns dictionary values with values() keyword


# In[13]:


d1.items() #Returns dictionaty key-value pair with items() keyword


# In[14]:


d5 = {1:'one' , 2:'two' , 'A':['asif' , 'john' , 'Maria']} #Dictionary with nested list
d5


# In[16]:


d6 = {1:'one' , 2:'two' , 'A':['asif' , 'john' , 'Maria'],'b':('cat','bat','mat')}
d6


# In[17]:


keys = {'a','b','c','d'} # Creating dict from a sequence of keys
d7 = dict.fromkeys(keys)
d7


# In[19]:


keys = {'a','b','c','d'} #Creating a dict same values
value = 10
d8 = dict.fromkeys(keys,value)
d8


# In[20]:


keys={'a','b','c','d'}
value=[10,20,30,40]
d9 = dict.fromkeys(keys,value)
d9


# In[21]:


value.append(50)
d9


# # Accessing the items from Dictionary

# In[22]:


d6


# In[23]:


d6[1] #Accessing the dict with key


# In[24]:


d6.get(1) #Accessing the value using get method


# In[28]:


d6['A']


# In[29]:


d6.get('A')


# In[33]:


d6.get('A[0]') # Need to check with Sir on this one


# In[32]:


d6


# # Add,Remove and Change items

# In[ ]:


d10 = {'Name':'Asif' , 'ID': 12345 , 'DOB': 1991 , 'Address' : 'Hilsinki'}
d10


# In[35]:


d10['DOB']


# In[37]:


#Changing the DOB
d10['DOB'] = '2000'
d10['Address'] = 'Hyderabad'
d10['Name'] = 'Nit'


# In[38]:


d10


# In[42]:


d11={'DOB':2002} #Changing the Dictionary
d10.update(d11)
d10


# In[43]:


d10['Job'] = 'Analyst'


# In[44]:


d10


# In[45]:


d10.pop('Job') #Removing the items in dictionary using the pop method
d10


# In[46]:


d10.popitem() #A random item is removed
d10


# In[47]:


del[d10['ID']] #Removing item using del method
d10


# In[48]:


d10.clear() #Delete all items of the dictionary using clear
d10


# In[49]:


del d10 # delete the dictionary object
d10


# # Copy Dictionary

# In[50]:


d11 = {'Name':'Asif' , 'ID': 12345 , 'DOB': 1991 , 'Address' : 'Hilsinki'}


# In[51]:


d12 =d11 # Creating a new reference for d11


# In[52]:


id(d12),id(d11) # Id for two dicts are same


# In[53]:


d13 = d11.copy() #Create a copy of Dictionary
d13


# In[54]:


id(d13)


# In[58]:


d11['Address'] = 'Mumbai'
d11


# In[59]:


d12 # D12 impacts since it is poiting to the same address


# In[60]:


d13 #d13 won't impact due to chnages made in original ditionary


# # Loop through the Dictionary

# In[61]:


for i in d11:  # Print Key, Value pair
    print(i, ':',d11[i])


# In[64]:


for i in d11: #print values
    print(d11[i]) #Dictionary items


# # Dicionary Membership

# In[65]:


d11


# In[66]:


'Name' in d11 # check if the key in the dictionary


# In[67]:


'Asif' in d11 #Membership test can only be done on Keys


# In[68]:


'ID' in d11


# In[69]:


'Address' in d11


# # All/Any
# The all method returns 
#  True() if all the keys of the dictionary are True
#  False() if any of the keys of the dictionary are false

# In[70]:


d11


# In[71]:


all(d11) # will return false as one value is false


# In[ ]:




