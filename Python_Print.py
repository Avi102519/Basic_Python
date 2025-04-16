#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Print us used to see the result of te code
a= 10
b=20
a
b


# In[2]:


a=20
b=10
print(a)
print(b)


# In[3]:


print(10)
print(10,29)
print('Python')
print(10,20,'Python')


# In[4]:


num1 = 20
num2= 30
add=num1+num2
print(add)


# # Print result with string

# In[5]:


num1 = 20
num2=30
add= num1+num2
print('The sum of',num1,'and',num2, 'is',add )


# In[12]:


name= 'Python'
age= 40
City = 'Nashville'
print('Myname is',name, 'I am from ', City, 'and I am',age, 'old')


# # Print Format Method

# In[14]:


num1 = 20
num2 = 30
add = num1+num2
print('The addition of{} and{} is = {}'.format(num1,num2,add))


# first deside how the print statement
# Eg:- The addition of 20 and 30 is = 50
# then replace the variable position with curly braces { }
# then appply .format(val1,val2,....val-n) method

# In[16]:


name = 'Python'
age = 20
city ='Hyderabad'
print('Hello my name is {} and i am {} years old from {}'.format(name,age,city))


# In[17]:


num1 = 100
num2= 25
num3 = 333
avg = (num1+num2+num3)/3
avg1 = round(avg,2)
print('The average of {} , {} and {} is = {}'.format(num1,num2,num3,avg1))


# In[ ]:


round(avg,2) #round of till 2 digit after decimal


# More short format meythod(f string method)
# variable should be in curly braces
# and write everything inside quots ''
# at starting simpaly add f

# In[19]:


num1 =20
num2=30
print(f'The addition of {num1} and {num2} is = {add} ')


# In[20]:


name = 'Python'
age = 20
city = 'Hyderabad'
print(f'Hello my name is {name} and I am {age} years old from {city}')


# In[21]:


num1 = 100
num2 = 25
num3 = 333
avg = (num1+num2+num3)/3
avg1 = round(avg,2)
print(f'The average of {num1}, {num2} and {num3} is = {avg1}')


# In[23]:


num1= 20
num2= 30
add= num1+num2
print(f'The addition of {num1} and {num2} is = {add}')
print('The addition of {} and {} is= {}'.format(num1,num2,add))
print(f'The addition of {num1} and {num2} is= {add}')


# # End statement

# In[24]:


print('hello')
print('Good Morning')


# In[25]:


print('hello',end = ' ')
print('world good day')


# # seprator
# here one print statement only we use
# insisde one print statement we have multipal values
# we want to seperate these multipal values with anything

# In[26]:


print('Hello','Hai','How are you',sep='--->')


# In[27]:


print('Hai','Hello','How are you',sep='&')


# In[28]:


print('Hai','Hello','How are you',sep=' ')


# In[29]:


print('Hai','Hello','How are you',sep='@')


# In[30]:


print(3,'.')


# In[31]:


print(3,'.',sep='')


# In[32]:


print(1,2,end=' ')
print(3,'.' ,sep='')


# 
