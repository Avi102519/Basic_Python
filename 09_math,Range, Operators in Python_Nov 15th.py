#!/usr/bin/env python
# coding: utf-8

# Import math module
# https://docs.python.org/3/library/math.html

# In[1]:


x=sqrt(25)


# In[2]:


help(math)


# import math

# In[3]:


import math


# In[4]:


x = math.sqrt(25)


# In[5]:


x


# In[6]:


x1 = math.sqrt(15)
x1


# In[7]:


print(math.floor(3.87)) #Floor means base


# In[8]:


print(math.ceil(3.87)) #max or highest value


# In[9]:


print(math.pow(3,2))


# In[10]:


print(math.pi)


# In[11]:


print(math.e)


# In[12]:


m.sqrt(25)


# In[13]:


import math as m


# In[14]:


m.sqrt(25)


# In[15]:


m.sqrt(10)


# In[16]:


from math import sqrt,pow,floor,ceil


# In[17]:


print(pow(2,3))


# In[18]:


from math import *
print(sqrt(25))
print(pow(3,7))
print(floor(3.9))
print(ceil(3.1))


# # User input function in Python || Command line input

# In[150]:


x = input()
y = input()
z = x+y
print(z) # Console waits for the user to enter string values and then concatenates the values


# In[152]:


x1 = input('Enter the 1st number') #input always considers String as a input
y1 = input('Enter the 2nd number') #it wont understand as arithmetic operator
z1 = x1+y1
print(z1) # Output is concatenated and it not adds


# In[153]:


type(x1)


# In[154]:


type(y1)


# In[155]:


x2 = int(input('Enter the 1st number'))
y2 = int(input('Enter the 1st number'))
z2 = x2+y2
print(z2)


# In[157]:


sch1 = input('enter a char')


# In[160]:


print(sch1[1])


# In[161]:


print(sch1[-1])


# In[162]:


print (sch1[1:4])


# # To calculate the expression we have to use Eval

# In[164]:


exp1 = eval(input('enter an expression'))
print(exp1)


# # range()

# In[22]:


r = range(0,10)
r


# In[23]:


#if you want to print the range, Default step is 1
list(range(0,10))


# In[24]:


r1 = list(r)
r1


# In[26]:


# to print even numbers
r2 = list(range(0,10,2))
r2


# In[27]:


d = {1:'one',2:'two',3:'three'}
d


# In[28]:


type(d)


# In[30]:


#print the keys
d.keys()


# In[31]:


#print the values
d.values()


# In[32]:


#to get the required value
d[2]


# In[33]:


#other way to get the value
d.get(2)


# # Operators in Python

# In[34]:


# 1.Arithmetic(+,-,*,/,%%,%), 2.Assignment(=),3.Relational,4.Logical,5.Unary


# In[35]:


#Arithmetic Operator


# In[36]:


x1,y1 = 10,5


# In[37]:


x1+y1


# In[38]:


x1-y1


# In[39]:


x1*y1


# In[40]:


x1/y1


# In[41]:


x1//y1


# In[42]:


x1%y1


# In[44]:


x1**y1


# # Assignment Operator

# In[45]:


x=2


# In[46]:


x=x+2


# In[47]:


x


# In[48]:


x+=2


# In[49]:


x


# In[50]:


x*=2


# In[51]:


x


# In[52]:


x-=2


# In[53]:


x


# In[54]:


x/=2
x


# In[55]:


a,b =5,6


# In[56]:


a


# In[57]:


b


# # Unary Operator
# Unary operator means we are applying minus(-) on the operand.n value with Unary operator becomes -n

# In[58]:


n = 90
m = -(n)


# In[59]:


m


# In[60]:


n


# # Relational Operator
# This is to compare the variables/values

# In[61]:


a=5
b=9


# In[62]:


a==b


# In[63]:


a>b


# In[64]:


a<b


# In[65]:


a<=b


# In[66]:


a>=b


# In[71]:


# for comparision we are not supposed to use = operator, = is will assign a value to the respective variable.
z=10
y = 0


# In[72]:


y=z


# In[73]:


y


# In[74]:


a!=b


# In[75]:


a=9


# In[76]:


a==b


# In[79]:


a <= b


# In[80]:


a >= b


# # Logical Operator
# And(*),or(+),NOT()
# ## LOGICAL OPERATOR 
# AND, OR, NOT
# 
# Truth Tables
# AND
# X Y =X*Y
# 1 0 = 0
# 0 1 = 0
# 0 0 = 0
# 1 1 = 1
# 
# OR
# 
# X Y = X+Y
# 0 0 = 0
# 0 1 = 1
# 1 0 = 1
# 1 1 = 1

# In[81]:


a =5
b =4


# In[82]:


a < 8 and b<5  #(1*1)


# In[83]:


a>8 and b<5 #(0*1)


# In[86]:


a <3 and b>9 #(1*0)


# In[87]:


a>6 and b>5 #(0*0)


# In[88]:


a < 8 or b<5 #( 1 + 0)


# In[89]:


a>8 or b<5 #(0+1)


# In[90]:


a <3 or b>9 #(1+0)


# In[91]:


a>6 or b>5 #(0+0)


# In[92]:


x = False


# In[94]:


not x


# In[95]:


x = not x


# In[96]:


x


# In[97]:


not x


# # Number system Conversion (bit-binary conversion)
# binary : base (0-1) --> please divide 15/2 & count in reverse order 
# octal : base (0-7)
# hexadecimal : base (0-9 & then a-f)
# when you check ipaddress you will these format --> cmd - ipconfig

# In[100]:


x=50
bin(x)


# In[101]:


int(0b110010)


# In[102]:


oct(100)


# In[103]:


oct(245671)


# In[104]:


int(0o737647)


# In[106]:


hex(38734)


# In[107]:


int(0x974e)


# In[108]:


hex(25)


# In[109]:


int(0x19)


# # Swap Variable in Python
# a,b = 5,6 after the swap we should ger a,b = 6,5

# In[110]:


a= 16
b= 23


# In[112]:


temp = a
a = b
b= temp


# In[113]:


a


# In[114]:


b


# In[120]:


a1 = 5
b1 = 6


# In[121]:


a1 = a1+b1
b1 = a1-b1
a1 = a1-b1


# In[122]:


print(a1)
print(b1)


# In[124]:


a2 = 4
b2 = 3

a2 = a2^b2
b2 = a2^b2
a2 = a2^b2


# In[125]:


print(a2)
print(b2)


# In[126]:


a3 = 19
b3 = 25
a3,b3 = b3,a3
print(a3)
print(b3)


# # Bitwise Operator
# we have 6 operators complement(~)||And(&)||OR(|)||XOR(^)||LeftShift(<<),Right Shift(<<)

# In[127]:


print(bin(12))


# In[128]:


print(bin(13))


# # complement --> you will get this key below esc character
# 12 ==> 1100 || 
# first thing we need to understand what is mean by complement. 
# complement means it will do reverse of the binary format i.e. - ~0 it will give you 1 ~1 it will give 0
# 12 binary format is 00001100 ( complement of ~00001100 reverse the number - 11110011 which is (-13)
# 
#  but the question is why we got -13 
#  to understand this concept ( we have concept of 2's complement
#  2's complement mean (1's complement + 1)
#  in the system we can store +Ve number but how to store -ve number
#  
#  lets understand binary form of 13 - 00001101 + 1 

# In[129]:


# COMPLEMENT (~) (TILDE  OR TILD)
#~12 # why we get -13 . first we understand what is complment means (reversr of binary format)


# In[130]:


~3


# In[131]:


~13


# In[132]:


~25


# In[133]:


~-34


# # bit wise and operator 
# 
# AND - LOGICAL OPERATOR ||| & - BITWISE AND OPERATOR  
# (we know that 1 & 1 is 1)
# 12 - 00001100 
# 13 - 00001101
# when we are add both then then outut we will get as 12
# 
# 
# AND
# X Y =X*Y
# 1 0 = 0
# 0 1 = 0
# 0 0 = 0
# 1 1 = 1
# 
# OR
# 
# X Y = X+Y
# 0 0 = 0
# 0 1 = 1
# 1 0 = 1
# 1 1 = 1

# In[134]:


12&13


# In[135]:


23&45


# In[136]:


55|3


# In[137]:


1|0


# In[138]:


1&0


# In[139]:


12|13


# In[140]:


35|40


# # XOR truth table
# x y= x^y
# 0 0= 0
# 0 1= 1
# 1 0= 1
# 1 1= 0
# 
# if x and y are different numbers then the out put is 1

# In[141]:


12^13


# In[142]:


25^30


# In[143]:


bin(25)


# In[144]:


bin(30)


# In[145]:


int(0b11110)


# # BIT WISE LEFT OPERATOR
# #bit wise left operator bydefault you will take 2 zeros ( )
# #10 binary operator is 1010 | also i can say 1010
# 10<<2

# In[146]:


# gain 4 bit
20<<4 #can we do this


# In[147]:


# BITWISE RIGHTSHIFT OPERATOR


# In[149]:


#Looses 2 bit
20>>2


# In[ ]:




