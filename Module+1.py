
# coding: utf-8

# # Module 1 Section 1 and 2 were basics:
# - jupyter basics, commenting, printing
# - variable & types, strings etc. 
# 

# # Module 1 Section 3: 
# - type function

# In[ ]:


type(0.5)


# In[ ]:


print((type(2)))


# # Module 1 Section 4:
# - Addition and Errors

# In[ ]:


"My name is" + "Saif"


# In[ ]:


print ("My name is" + " Saif")


# In[ ]:


# [] ERRORS: 
# (i)TypeError -string+int
# (ii) SyntaxError -missing a quote, variable names starting with a number
# (iii) NameError -Print instead of print or trying to find a variable that isn't there


# # Module 1 Section 5: 
# - ASCII Art: Basically facebook logo designs on girls' profiles in the 2000s :P 

# # Module 1 Section 6: 
# - Input

# In[1]:


print("hello")


# In[2]:


print("Give me a number: ")
numberss = input()


# In[3]:


print("The number given was " +  numberss)


# In[5]:


name = input("Enter your name: ")
print ("Hi " + name + "!")



# In[2]:


choice = input("Please tell me your drink of choice: " )
print("I am serving you the" + " " + choice +" right away!")


# In[3]:


type(choice)


# In[6]:


type(name)


# # Module 1 Section 7
# - Print Formatting
# 

# In[9]:


#Method 1
names = "Saif"
print("Hello" + names + " How are you?")


# In[10]:


#Method 2: use pair of commas instead of plus; autospaced!
print("Hello",names,"How are you?")


# In[13]:


print("Combining a number like",6, "with a string is valid if we use poc instead of +")


# # Module 1 Section 8
# - Double and single quotes
# - Check string tests: e.g. "python".islpha() gives True 
# 
#     .isalpha()
#     .isalnum()
#     .istitle()
#     .isdigit()
#     .islower()
#     .isupper()
#     .startswith()
# 
# 
# 

# # Module 1 Section 9
# .capitalize() 
# .lower() 
# .upper() 
# .swapcase() 
# .title() 

# In[14]:


# review and run code to test if a string is to be found in another string
menu = "salad, pasta, sandwich, pizza, drinks, dessert"
print('pizza' in menu)


# In[17]:


# uppercase is not equal to lower case
menu = "salad, pasta, sandwich, pizza, drinks, dessert"
print('Pizza' in menu)


# In[16]:


# .lowering to eliminate case sensitivity fully
menu = "salad, pasta, sandwich, pizza, drinks, dessert"
print('Pizza'.lower() in menu.lower())


# In[7]:


input_test = input("enter food categories eaten in last 24 hours: ")
print('It is', 'dairy' in input_test, 'that', '"' + input_test + '"', 'contains dairy')


# # Module 1 Assignment

# In[11]:


#ALLERY TEST


# [ ] get input for input_test variable
input_test = input("enter food categories eaten in last 24 hours: ")

# [ ] print "True" message if "dairy" is in the input or False message if not
print('It is', 'dairy'.lower() in input_test.lower(), 'that', '"' + input_test + '"', 'contains dairy')

# [ ] print True message if "nuts" is in the input or False if not
print('It is', 'nuts'.lower() in input_test.lower(), 'that', '"' + input_test + '"', 'contains nuts')


# [ ] Challenge: Check if "seafood" is in the input - print message
print('It is', 'seafood'.lower() in input_test.lower(), 'that', '"' + input_test + '"', 'contains seafood')

# [ ] Challenge: Check if "chocolate" is in the input - print message
print('It is', 'chocolate cake'.lower() in input_test.lower(), 'that', '"' + input_test + '"', 'contains chocolate cake')

