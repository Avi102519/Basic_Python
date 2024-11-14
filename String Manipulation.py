#!/usr/bin/env python
# coding: utf-8

# # Manipulating the String
# Escape character Prints as
# `\'` Single quote
# `\"` Double quote
# `\t` Tab
# `\n` Newline (line break)
# `\\` Backslash
# `\b` Backspace
# `\ooo` Octal value
# `\r` Carriage Return

# In[2]:


print("Hello There!\nHow are you?\nI\'m doing good'")


# # Raw String
# Raw string entiely ignores all escape characters and print backslash that appers in the string
# Raw strings are mostly used for regular expression definitions.

# In[3]:


print(r"Hello There!\nHow are you?\nI\'m doing good")


# # Multi Line String

# In[4]:


print(

"""Dear Alice,

Eve's cat has been arrested for catnapping,
cat burglary, and extortion.

Sincerely,
Bob"""
)


# # Indexing and Slicing a string

# In[5]:


#Indexing
s1 = 'Hello World!'
s1[0]


# In[6]:


s1[4]


# In[7]:


s1[-1]


# In[9]:


#Slicing
s1[0:4]


# In[10]:


s1[:5]


# In[12]:


s1[6:]


# In[13]:


s1[6:-1]


# In[14]:


s1[:-1]


# In[15]:


s1[-12:-4]


# In[18]:


s1[::-1]


# In[19]:


str = s1[1:5]
str


# # The in and not in operators

# In[20]:


"Nit" in "i am a NIT student"


# In[21]:


"NIT" in "i am a NIT student"


# In[22]:


"HELLO" in "Hello World"


# In[23]:


'' in 'Hello'


# In[24]:


"World" not in "Hello World"


# # Upper(), Lower() and title()
# Transforms a string upper,lower and title cases

# In[28]:


s3 = 'Hello world!'
s3.upper()


# In[29]:


s3.lower()


# In[30]:


s3.title()


# # isupper() and islower() methods
# returns True or False after evaluating if a string is in upper and lower case

# In[31]:


s4 = 'Hello world!'
s4.islower()


# In[32]:


s4.isupper()


# In[34]:


'HELLO'.isupper()


# In[35]:


'abc12345'.islower()


# In[36]:


'367890'.islower()


# In[37]:


'367890'.isupper()


# # The is X string methods
# Method Description
# isalpha() returns `True` if the string consists only of letters.
# isalnum() returns `True` if the string consists only of letters and numbers.
# isdecimal() returns `True` if the string consists only of numbers.
# isspace() returns `True` if the string consists only of spaces, tabs, and new-lines.
# istitle() returns `True` if the string consists only of words that begin with an
# uppercase letter followed by only lowercase characters.

# # startswith() and endswith()

# In[38]:


'Hello World!'.startswith('HELLO')


# In[39]:


'Hello World!'.startswith('Hello')


# In[40]:


'Hello World!'.endswith('World')


# In[41]:


'Hello World!'.endswith('!')


# In[42]:


'Hello World!'.endswith('World!')


# In[43]:


'Hello World!'.endswith('Hello World')


# In[44]:


'Hello World!'.endswith('Hello World!')


# # Join() and split()

# # Join()
#     The join method takes all the items in an iterable like a List,tuple,set or Dict and joins them into a string. User can specify the seperator.

# In[46]:


''.join(['My','name','is','seperator'])


# In[47]:


','.join(['My','name','is','seperator'])


# In[48]:


' '.join(['I', 'am', 'Dev'])


# In[49]:


'WHY'.join(['I', 'am', 'Dev'])


# # Split()
# Split method splits string into a list,By default split uses the whitespace to seperate the items in a list, however user can cutomoze the seperator

# In[50]:


'Hi what is the  weather prediction today'.split(' ')


# In[51]:


'HiABCwhatABCisABCtheABCweatherABCpredictionABCtoday'.split('ABC')


# In[52]:


'Hi what is the  weather prediction today'.split('a')


# In[53]:


'Hi what is the  weather prediction today'.split()


# # Justifying the text with rjust(),ljust() and center()

# In[54]:


'Hello'.rjust(10)


# In[57]:


'H'.rjust(10)


# In[58]:


'h'.ljust(10)


# In[59]:


'howareyou'.ljust(10) #Wanted to know the limitation


# In[60]:


#An optional second argument to rjust() and ljust() will specify a fill character apart from a space character


# In[63]:


'Hello'.rjust(20,'*')


# In[69]:


'Hello'.ljust(20,'-')


# In[70]:


'Hello'.center(20,'=')


# # Removing whitespace with strip(), rstrip(), and lstrip()

# In[71]:


s5 = '          Hello World         ' 
s5


# In[74]:


s5.rstrip()


# In[75]:


s5.strip()


# In[76]:


s5.lstrip()


# In[80]:


s6 = 'acti love pythonact'
s6.strip('act')


# # The count() Method
# Counts the number of occurrences of a given character or substring in the string it is
# applied to. Can be optionally provided start and end index

# In[81]:


s7 = 'actiactloveactpythonact'
s7.count('act')


# In[82]:


s7.count('a')


# In[83]:


s7.count('act',5)


# # replace() Method
# Replaces all occurences of a given substring
# with another substring. Can be optionally
# provided a third argument to limit the number of replacements. Returns a new string.

# In[84]:


s8 = 'i love pickleball'
s8.replace('pickleball','Tennis')


# In[85]:


s9 = 'cricket,tennis,football,cricket'
s9.replace('cricket','pickleball',1)


# In[86]:


s10 = 'I play Pickle ball, my favorite game is Tennis'
s10.replace('pickleball','footbal')


# In[ ]:




