#!/usr/bin/env python
# coding: utf-8

# ## Assignment
# ### Python Predefined String Functions

# In[2]:


# Python String
str = "Python Assignment_1 (PIAIC Islamabad Batch)"
# To print above string we can use print() function
print(str)


# In[3]:


# Python String assigning to a variable also works for single, double and tripple quotes
str_single = 'Single Quote'
print(str_single)
str_double = "Double Quotes"
print(str_double)
str_triple ="""Triple Quotes, with triple quotes
string can be extend to multiple Lines"""
print(str_triple)


# ### 1.Conversion Function

# In[4]:


# capitalize()-Returns the string with the first character capitalized and rest of the characters in lower case
var = "PIAIC"
print(var.capitalize())


# In[5]:


# lower()-Converts all the characters of the String to lowercase
var = "ISLAMABAD"
print(var.lower())


# In[6]:


#upper() – Converts all the characters of the String to uppercase
var = "bahria university"
print(var.upper())


# In[7]:


#swapcase() – Swaps the case of every character in the String means that lowercase characters got converted to uppercase and vice-versa.
var = 'Muhammad Usman'
print(var.swapcase())


# In[8]:


var="Muhammad Usman Tariq"
print(var.casefold())


# In[10]:


var="Muhammad Usman Tariq"
print(var.center(10))

var="Muhammad Usman Usman Tariq"
print(var.count("Usman"))


# In[11]:


var="Muhammad Usmån Tariq"
print(var.encode())


# In[12]:


var="Muhammad Usman Tariq"
print(var.endswith("q"))


# In[13]:


var="Muhammad\tUsman\tTariq"
print(var.expandtabs())

var="Muhammad Usman Tariq"
print(var.find("q"))


# In[16]:


var="I am {age:.2f} years old."
print(var.format(age=22))

var = "My name is {0}, I'am {1}".format("Usman",22)
print(var)


# In[19]:



# Input dictionary 
profession = { 'name':['Usman', 'Azhar'], 
               'profession':['DBA', 'Developer'], 
               'age':[22, 23] } 
                       
# Use of format_map() function  
print('{name[0]} is an {profession[0]} and he'
      ' is {age[0]} years old.'.format_map(profession)) 
        
print('{name[1]} is an {profession[1]} and he'
      ' is {age[1]} years old.'.format_map(profession))


# In[21]:


list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5] 
  
# Will print the index of '4' in list1 
print(list1.index(4))

# Random list having sublist and tuple also 
list1 = [1, 2, 3, [9, 8, 7], ('cat', 'bat')] 
  
# Will print the index of sublist [9, 8, 7] 
print(list1.index([9, 8, 7])) 
  
# Will print the index of tuple  
# ('cat', 'bat') inside list  
print(list1.index(('cat', 'bat'))) 


# In[26]:


var="Tariq123"
print(var.isalnum())

var="Tariq 123"
print(var.isalnum())


# In[28]:


var="MuhammadUsman"
print(var.isalpha())

var="Muhammad Usman"
print(var.isalpha())


# In[40]:


var="1230"
print(var.isdecimal())

var="12.3a"
print(var.isdecimal())


# In[41]:


var="123"
print(var.isdigit())


# In[43]:


# String with spaces 
string = "Muhammad Usman"
print(string.isidentifier()) 
  
# A Perfect identifier 
string = "MuhammadUsman"
print(string.isidentifier()) 
  
# Empty string 
string = "" 
print(string.isidentifier()) 
  
# Alphanumerical string 
string = "0smanS0fi"
print(string.isidentifier()) 
  
# Beginning with an integer 
string = "UsmanS0fi"
print(string.isidentifier()) 


# In[45]:


var="12345"
print(var.isnumeric())
var="123abc"
print(var.isnumeric())


# In[47]:


var="123 Usman"
print(var.isprintable())


# In[48]:


# checking for printable characters 
string = 'My name is Usman'
print(string.isprintable()) 
  
# checking if \n is a printable character 
string = 'My name is \n Usman'
print(string.isprintable()) 
  
# checking if space is a printable character 
string = '' 
print( string.isprintable())


# In[52]:


var="\n \n \n"
print(var.isspace())


var="\nUsman\nTariq\n"
print(var.isspace())


# In[55]:


var="Muhammad usman Tariq"
print(var.istitle())

var="Muhammad Usman Tariq"
print(var.istitle())


# In[58]:


var=['U','s','m','a','n']
print("".join(var))

var=['1','2','3','4','5']
print("-".join(var))


# In[62]:


lstr = "I love Pakistan"
  
# Printing the original string 
print ("The original string is : \n", lstr, "\n") 

# Printing the left aligned  
# string with "-" padding  
print ("The left aligned string is : ") 
print (lstr.ljust(40, '-'))


# In[63]:


rstr = "I love geeksforgeeks"
  
# Printing the original string 
print ("The original string is : \n", rstr, "\n") 
  
# Printing the right aligned string 
# with "-" padding  
print ("The right aligned string is : ") 
print (rstr.rjust(40, '-')) 


# In[ ]:




