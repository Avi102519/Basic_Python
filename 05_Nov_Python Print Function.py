#!/usr/bin/env python
# coding: utf-8

# In[2]:


#It only prints last value
a=100
b=200
a
b


# In[3]:


#if user wants to print all values, user has to use Print function
a= 200
b = 100
print(a)
print(b)


# In[4]:


#Multiple values can be printed using print function with multiple values
print(10)
print(10,20)
print('Python')
print(10,20,'Python')


# In[6]:


num1 = 25
num2 = 35
add = num1+num2
print(add)


# # Print result with string

# In[7]:


num1 = 30
num2 = 50
add = num1+num2
print('The addition of',num1,'and',num2,'is=',add)


# In[15]:


name = 'Python'
age = '38'
city = 'Hyderabad'
print('Hello my name is',name,'I am',age,'old,','I am from',city)


# # Print format method
# Decide the format to be printed
# Write entire print statement in single quotations by replacing variables with {}
# Once the print statement end with single quote start writing.format and in paranthesis enter the variables

# In[16]:


num1 = 20
num2 = 30
add = num1+num2
print('The addition of {} and {} is {}'.format(num1,num2,add))


# In[17]:


name = 'Python'
age = '38'
city = 'Hyderabad'
print('Hello my {} is, i am {} old, I am from {}'.format(name,age,city))


# In[18]:


x = 33
y= 45
z= 56
avg = (x+y+z)/3
avg1 = round((x+y+z)/3)
print('the avegare of {},{} and {} is {} or {}'.format(x,y,z,avg,avg1))


# # Simplified print function with format method
# Variables in {} braces
# write everything in single quotes
# Write the print function starts with letter 'f'

# In[19]:


name = 'Python'
age = '38'
city = 'Hyderabad'
print(f'Hello my name is {name}, I am {age} and i am from {city}')


# In[20]:


x = 33
y= 45
z= 56
avg = (x+y+z)/3
avg1 = round((x+y+z)/3)
print(f'the avegare of {x},{y} and {z} is {avg} or {avg1}')


# # 3 Print formats

# In[23]:


a= 10
b=20
add= a+b
print('The addition of',a,'and',b,'is',add)
print('The addition of {},{} is {}'.format(a,b,add))
print(f'The addition of {a},{b} is {add}')


# # End statement
# End statement that joint  line from end of one string to starting of other string

# In[25]:


print('Hello',end=' ')
print('Good Morning')


# # Seperator
# we use one print statement
# inside one print statement we have multiple values
# we want to seperate these values with anything

# In[27]:


print('hi','hello','how are you',sep= '-->')


# In[28]:


print('hi','hello','how are you',sep='@')


# In[29]:


print('hi','hello','how are you', sep= '&')


# In[30]:


print('hi','hello','how are you',sep = ' ')


# In[31]:


print(3,'.') # here . is far away from 3 in the below print statement lets add them together using sep


# In[33]:


print(3,'.',sep='')


# In[34]:


print(1,2,end=' ')
print(3,'.',sep= '')


# In[ ]:




