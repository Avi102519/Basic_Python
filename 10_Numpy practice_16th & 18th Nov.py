#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as np


# In[29]:


np.array([1,2,3])


# In[3]:


np.arange(15)


# In[4]:


np.arange(3.0)


# In[5]:


np.arange(10)


# In[6]:


np.arange(10,20)


# In[7]:


np.arange(20,10) #1st argument is always less than second argument


# In[8]:


np.arange(-20,10)


# In[9]:


np.arange(-20,-10)


# In[10]:


np.arange(30,20)


# In[11]:


ar = np.arange(10,20)


# In[12]:


ar


# In[13]:


np.arange() #atleast one value present


# In[14]:


np.arange(10,20,3) # Start, stop and step


# In[15]:


np.arange(10,30,4)


# In[16]:


np.zeros(3) #parameter tuning


# In[17]:


np.zeros(3,dtype = int) #Hyper Parameter tuning on dtype


# In[18]:


np.zeros([2,2],dtype = int)


# In[19]:


np.zeros((2,10))


# In[20]:


np.zeros((10,5))


# In[23]:


n = (6,7)
n1 = (7,8)
print(np.zeros(n1))


# In[24]:


np.ones(3)


# In[25]:


np.ones(4,dtype=int) #Hyper Parameter tuning


# In[28]:


np.ones((3,5),dtype = int)


# In[33]:


rand(3,2)


# In[34]:


random.rand(3,2)


# In[38]:


np.random.rand(5)


# In[39]:


np.random.rand(5)


# In[40]:


np.random.rand(2,4)


# In[41]:


np.random.randint(2,10)


# In[46]:


np.random.randint(2,4)


# In[47]:


np.random.randint(2,20)


# In[48]:


np.random.rand(2,20)


# In[50]:


np.random.randint(10,20,3)


# In[51]:


np.random.rand(3)


# In[52]:


np.random.randint(1)


# In[53]:


np.random.randint(30,20,10)


# In[54]:


np.random.randint(10,40,(10,10))


# In[58]:


np.random.randint(1,100,(12,12))


# In[59]:


np.arange(1,10).reshape(3,3)


# In[69]:


np.arange(1,12).reshape(11,1) #1d array we can reshape it 3*3


# In[61]:


b = np.random.randint(1,100,(12,12))


# In[62]:


b


# In[63]:


type(b)


# In[64]:


b[:]


# In[65]:


b[1:5]


# In[66]:


b[1,5]


# In[70]:


b[2:3]


# In[71]:


b[0:-2]


# In[72]:


b[-5,-3]


# In[73]:


b[-4,2]


# In[80]:


c=np.random.randint(10,20,(4,4))
c


# In[81]:


c[-4:2]


# In[82]:


c[-4,2]


# In[83]:


d = np.random.randint(10,20,10)


# In[84]:


d


# In[86]:


id(d)


# In[87]:


arr = np.random.randint(0,100,(10,10))


# In[88]:


arr


# In[89]:


arr[::-1]


# In[90]:


arr[::-2]


# In[91]:


arr[::-3]


# In[92]:


arr[:-3]


# In[93]:


arr.max()


# In[94]:


arr.min()


# In[96]:


arr.mean()


# In[ ]:


mat = np.random.randint(10,10,(0,100))


# # Practice

# In[97]:


a = np.array([10,25,2019,1986,8,30]) #Vector
a


# In[98]:


type(a)


# In[101]:


#2d Array (Matrix)
a2 = np.array([[10,25,2019],[8,30,1986]])
a2


# In[104]:


#3d Array (Tensor)
a3 = np.array([[2019,10,25,800],[7,6,1989,1000],[1986,8,30,1200]])
a3


# # Dtype
# The desired data type for the array, if not  given , Then the type will be determined as the minimum type required to hold  the objects  in these objects

# In[106]:


a4 = np.array([11,22,33],dtype = float)
a4


# In[107]:


a5 = np.array([11,22,33],dtype = int)
a5


# In[108]:


a6 = np.array([11,22,33],dtype = bool)
a6


# In[110]:


a7 = np.array([11,22,33],dtype = complex)
a7


# Numpy Arrays Vs Python Sequences
# NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically).
# Changing the size of an ndarray will create a new array and delete the original.
# The elements in a NumPy array are all required to be of the same data type, and thus will be
# the same size in memory.
# NumPy arrays facilitate advanced mathematical and other types of operations on large
# numbers of data. Typically, such operations are executed more efficiently and with less code
# than is possible using Python’s built-in sequences.
# A growing plethora of scientific and mathematical Python-based packages are using NumPy
# arrays; though these typically support Python-sequence input, they convert such input to
# NumPy arrays prior to processing, and they often output NumPy arrays.

# # arange
# arange can be called with a varying number of positional arguments

# In[114]:


a8 = np.arange(1,21) # 1 Includes, 21 excludes
a8


# In[112]:


a9 = np.arange(1,25,2) # Step count is 2, matrix will be returned with alternate numbrs
a9


# In[113]:


a10 = np.arange(1,25,3)
a10


# # Reshape
# reshape size both the numbers product shall be equal to the number of values in a matrix
# 

# In[115]:


a11 = a8.reshape(5,4)
a11


# In[116]:


a12 = np.arange(1,11)
a12


# In[118]:


a13 = a12.reshape(2,5)
a13


# In[119]:


a14 = a12.reshape(5,2)
a14


# # Ones & Zeros

# In[121]:


a15 = np.zeros((3,3))   # mention the size of the zeros in the tuple
a15


# In[124]:


a16 = np.zeros((3,4),dtype=int)
a16


# In[125]:


a17=np.ones((2,5))
a17


# In[126]:


a18 =np.ones((3,4),dtype= int)
a18


# In[127]:


a19 = np.ones((2,3),dtype = bool)
a19


# In[137]:


np.random.random((2,3))


# # Practice 

# In[133]:


a20 = np.array([3,4])
a20


# In[135]:


np.array([[2,3],[4,5]])


# In[136]:


np.arange(1,11).reshape(2,5)


# # Linspace
# linspace is called linery space, linearly separates the values in the given range.

# In[139]:


a21=np.linspace(-10,10,10)
a21


# In[140]:


np.linspace(1,10,20)


# # Identity
# Returns the identity matrix wherer diagonal items will be ones and everything will be zeros

# In[142]:


np.identity(2)


# In[143]:


np.identity(4)


# # Array Attributes

# In[146]:


a22 = np.arange(10) #ID
a22


# In[148]:


a23 = np.arange(12,dtype = int).reshape(3,4) #matrix
a23


# In[150]:


a24 = np.arange(8).reshape(2,2,2)  #3D-- Tensor
a24


# # ndim
# To findout the given array dimensions

# In[151]:


a22.ndim


# In[152]:


a23.ndim


# In[153]:


a24.ndim


# # Shape
# Returns the shape of the matrix, Rows and Columns

# In[155]:


a22.shape


# In[156]:


a23.shape


# In[157]:


a24.shape


# # Size
# returns the number of values in the matrix

# In[158]:


a22.size


# In[159]:


a23.size


# In[160]:


a24.size


# # Itemsize
# Returns the memory occupie by the item

# In[161]:


a22.itemsize


# In[162]:


a23.itemsize


# In[164]:


a24.itemsize


# # Dtype
# returns the datatype of the array

# In[167]:


print(a22.dtype)
print(a23.dtype)
print(a24.dtype)


# # Indexing and Slicing

# In[168]:


p1 = np.arange(10)
p2 = np.arange(12).reshape(3,4)
p3 = np.arange(8).reshape(2,2,2)
p4 = np.arange(16).reshape(4,4)


# In[169]:


p1


# In[170]:


p2


# In[171]:


p3


# In[172]:


p4


# # Indexing on 1d Array

# In[173]:


p1[-1] #Fetching the last item


# In[174]:


p1[0] #Fetching the first item


# # Indexing on 2D Array

# In[176]:


p2


# In[178]:


p2[2,3] #2 row(3rd row since the matrxi index starts from 0), 3rd column(4th column)
#Fetching desired elements


# # Indexing on 3D(Tensors)

# In[179]:


p3


# In[180]:


p3[1,0,1] #fetchign the desired element


# # Slicing on 1D Array

# In[181]:


p1


# In[182]:


p1[0:6]


# In[183]:


p1[:]


# In[184]:


p1[:6]


# In[185]:


p1[1:]


# In[186]:


p1[::-1]


# In[187]:


p1[1:6:1]


# In[188]:


p1[1:6:3]


# # Slicing on 2D array

# In[189]:


p2


# In[190]:


p2[:]


# In[191]:


p2[::-1]


# In[192]:


p2[:1]


# In[193]:


p2[1:]


# In[194]:


p2[::]


# In[195]:


p2[[0,2],[1,2]]


# In[196]:


p2[1,2]


# In[197]:


p2[1,1]


# In[198]:


p2[2,2]


# In[200]:


p2[2,3]


# In[201]:


p2[2,0]


# In[202]:


p2[0,0] #1st row,1st column


# In[203]:


p2[0,1] #1st row ,2nd column


# In[204]:


p2[0,3] #1st rwo 4th column


# In[205]:


p2[0,2] #1st row 3rd column


# In[206]:


p2[1,0] # 2nd row 1st column


# In[207]:


p2[1,1] # 2nd row 2nd column


# In[208]:


p2[1,2] # 2nd row 3nd column


# In[209]:


p2[1,3] # 2nd row 4th column


# In[210]:


p2[2,0] #3rd row 1st column


# In[211]:


p2[2,1] # 3rd row 2nd column


# In[212]:


p2[2,2] # 3 rd row 3 rd column


# In[213]:


p2[2,3] #3 rd row 4th column


# In[214]:


p2[0:] # fetching the entire matrix


# In[215]:


p2[0,:] #fetching entire 1st row


# In[216]:


p2[:,2]# fetching entire 3rd column


# In[218]:


p2[:,0] # fetching entre 1st column


# In[219]:


#fetching 5,6 and 9,10


# In[220]:


#to get 5,6
p2[1:3]


# In[222]:


p2[1:3,1:3] 


# EXPLANATION :Here first [1:3] we slice 2 second row is to third row is not existed which is 2
# and Secondly , we take [1:3] which is same as first:we slice 2 second row is to third row is not
# included which is 3

# In[226]:


#to get 6,7 and 10,11
p2[1:4]


# In[227]:


p2[1:4,2:4]


# In[228]:


p2


# In[229]:


#to get 0 1 and 4,5
p2[:2]


# In[230]:


p2[:2,:2]


# In[232]:


#fetch 0,3 and 8,11
p2


# In[233]:


p2[::2]


# In[235]:


p2[::2,::3]  
#EXPLANATION : Here we take (:) because we want all rows , second(:2) for alternate value,
#and (:) for all columns and (:3) jump for two steps


# # Array Functions

# In[238]:


a25 = np.random.random((3,3))
a25


# In[239]:


a26 = np.round(a25*100)
a26


# In[240]:


#Max
np.max(a26)


# In[241]:


#min
np.min(a26)


# In[242]:


#sum
np.sum(a26)


# In[243]:


np.prod(a26)                                


# In[244]:


a26


# In[245]:


#mean
np.mean(a26)


# In[246]:


#median
np.median(a26)


# In[251]:


np.median(a26,axis=1)


# In[248]:


#std
np.std(a26)


# In[250]:


np.std(a26,axis=0)


# In[249]:


#variance
np.var(a26)


# In[ ]:




