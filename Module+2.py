
# coding: utf-8

# # Module 2 Section 1
# - Function

# In[1]:


def hello():
    print("Hello, can you hear me?")
    print("I am calling from the other side!")
hello()


# In[14]:


def hoinaken(baal):
    print(baal.upper() + "!")

hoinaken("kemon asos?")


# In[9]:


def yell_this(phrase):
    print(phrase.upper() + "!")
    
yell_this("hello sdfsdf")


# In[15]:


def yell_this_with_default(halum = "good morning"): #default
    print(halum.capitalize(),"!")
yell_this_with_default("good night")
yell_this_with_default()


# In[19]:


def add_num(num = 10):
    print(num + num)
    
add_num()


# # Module 2 Section 2
# - return in function

# In[38]:


def msg_double(phrase):
    double = (phrase + " " + phrase)
    return double

print(msg_double("hello"))


# In[28]:


def halveit(half):
    return half/2
print(halveit(22))


# In[30]:


def halveit(half):
    print(half/2)
halveit(22)


# In[37]:


#period example practice

def period(p1,p2):
    steptofollow = ("[1st]" + p1.upper() + "[2nd]" + p2.upper())
    return steptofollow
storage = period("history", "mathematics")
print("SCHEDULE:", storage)


# In[58]:


#format example practice
def format(name, age, sex):
    something = ("Student: " + name.upper()+"\nAge:" + str(age) + "\nSex:" + sex.upper()) #comma instead of + doesn't work
    return something
print(format("saif", 23, "male"))


# In[62]:


def add_numbers(num_1, num_2):
    return num_1 + num_2
print(add_numbers (100, 100))


# # Module 2 Section 3
# - Sequence

# In[2]:


#food availability check, just practicing





# In[12]:


#food availability check, just practicing

def food_available(food):
    check = 'burger, pizza, roll, sandwich, french fries, toast'
    return (food.lower() in check)

print(food_available('cheese'))




# In[3]:


#food availability check, just practicing

def food_available(food):
    menu = 'burger, pizza, roll, sandwich, french fries, toast'
    return menu
food = input("Please enter your food: ")

print("It is", food.lower() in food_available(food).lower(), "that", food, "is availabe!")


# In[5]:


#bird problem

def bird_available(bird):
    bird_types = 'crow robin parrot eagle sandpiper hawk pigeon'
    return bird_types

bird = input("Please enter a bird: ")

print("It is", bird.lower() in bird_available(bird).lower(), "that", bird, "is availabe!")


# # Module 2 Assignment

# In[8]:


input1 = input("enter fish name: ")
input2 = input("enter the fish price (no symbol): ")
def fishstore(input1, input2):
    amazing = input1 + " costs $" +input2
    return amazing 
print("Fish Type: " + fishstore(input1,input2))

