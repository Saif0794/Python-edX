
# coding: utf-8

# # Module 3 Section 1
# - if else pass
# 

# In[2]:


#Book title practice

title = input("Please enter your book title: ")

if title.istitle():
    print(title, 'is a nice title!')
else: 
    print(title, 'needs capitalization.')


# In[7]:


#from quiz
year = "2001" 

if year.isdigit():
   print(year, "is all digits")  
else:
  pass


# # Module 3 Section 2
# - Comparison < > =

# In[8]:


5==5


# In[9]:


5!=4


# In[10]:


3>=3


# In[11]:


3<=2


# In[15]:


x = 3
if x is 2:
    print(x)
else:
    print("1")


# In[17]:


x = 3
if x==3:
    print("yes")
else:
    print("no")


# In[23]:


someone = True

if someone:
    print('use "=" to assign values')
else:
    pass


# # Module 3 Section 3
# - String Comparison
# - Challenging codes using function

# In[12]:


#TF Quiz, the most challenging code so far!



def tf_quiz(question,answer):
    code = input("(T/F)" + question +": ")
    if code.upper() == answer:
            code = "correct"
    else:
            code = "incorrect"
        
    return code


   
    
quiz_eval = tf_quiz("Octopuses have green blood","F")
print("Your answer is", quiz_eval)

quiz_eval = tf_quiz("Batman is better than Superman","F")
print("Your answer is", quiz_eval)

quiz_eval = tf_quiz("Rutba loves Avik more than Avik loves Rutba :P ","T")
print("Your answer is", quiz_eval)


# In[18]:


# Y/N quiz for driving

def license(question,answer):
    car = input(question + ": ")
    if car.upper() == answer:
        car = "cool"
    else:
        car = "fucked"
    return car

drive = license("Receive an important call while driving", "N")
print("You are", drive + "!")


# # Module 3 Section 4
# - Elif and Casting

# In[20]:


# elif is basic
# casting involves making a DIGIT string to an integer, for instance
x="8"
y= int(x)+9
print(y)


# # Module 3 Section 5
# - Math Operator

# In[21]:


x = 3
y = 4
calculation = x*y
print(calculation)


# # Module 3 ASSIGNMENT

# In[53]:


#Cheese

cheese = input("Enter cheese order weight: ")

if cheese.isdigit() == False:
    print("Invaid input, numeric values only")
elif float(cheese) < 10.0:
    print(cheese, "is below minimum order amount")
elif float(cheese) > 100.0:
    print(cheese, "is more than currently available stock")
else:
        print(cheese+ " costs $", float(cheese)*2)


