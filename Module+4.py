
# coding: utf-8

# # Module 4 Section 1
# - Nested Loop

# In[ ]:


#cheese burger example

burger = input("Please choose C for Cheese and V for Veggie: ")

if burger.upper() == "C":
    flavor = input("Please enter C for Chicken and B for Beef: " )
    if flavor.upper() == "C":
        print ("Here is your Chicken Cheese burger!")
    else:
        print("Here is your Beef Cheese burger!")
else:
    print("Here is your Veggie burger!")


# In[3]:


if True:
 if False:
     print("Banana")
 else:
     print("Apple")
else:
 if True:
     print("Dates")
 else:
     print("Corn")


# # Module 4 Section 2
# - Escape Characters

# In[5]:


#Backslash display 
print("to go to a new line use \\n")


# In[6]:


#Quotation
print("I\'ve said, \"Go to hell.\"")


# In[11]:


#New line
print("Name: Saif\nAge:23")


# In[17]:


#Tab
print("Name:\tSaif\nAge:\t\t23\nSex:\t\t\tMale")


# In[18]:


print("'\''\''\''\''\'")


# In[19]:


#Important
print("\\\\") 


# In[21]:


#Important
print("\\\\\\\\")


# In[4]:


print("'\'")


# In[8]:


print("\\")


# #Module 4 Section 3
# - While loop, Break & Increment

# In[10]:


while True:
    print("Keep printing until break")
    break


# In[1]:


while True:
    name = input("Enter your first name: ")
    if name.isalpha():
        break
        print(name.title(), "Welcome!")
    else:
        print(name.title() ,"is not a single word name!")


# In[ ]:


while True:
    name = input("Enter your first name: ")
    if name.isalpha():
        break
    else:
        print(name.title() ,"is not a single word name!")
print(name, "Welcome!")


# In[6]:


#Vote

votes = 1
votes = votes + 1 #or votes +=1
print(votes)

zotes = 1
zotes = zotes +2
print(zotes)

xotes = 2
xotes = xotes - 3
print(float(xotes))


# In[4]:


# seat counts
seats = 0
while True:
    
    seats = seats + 1
    if seats == 10:
        print("No more seats")
        break
    else: print("seat count: ",seats)


# In[9]:


# seat counts
seats = 10
while True:
    
    
    print("seats remaining: ",seats)
    seats = seats - 1 #if you swap this line with previous line then count is 9 to 0 !!
    if seats == 0:
        print("No more seats remainaing, final count: ", seats)
        break
    


# In[4]:


num_1 = 0
num_temp = 0
num_final = 0

while True:
 num_1 = input("Enter an integer: ")
 if num_1.isdigit():
     num_final = num_temp + int(num_1)
     num_temp = num_final
 else:
     print(num_final)
     break


# In[5]:


num_1 = ""
num_temp = ""
num_final = ""

while True:
 num_1 = input("Enter an integer: ")
 if num_1.isdigit():
     num_final = num_temp + num_1
     num_temp = num_final
 else:
     print(num_final)
     break


# In[2]:


x = 0 

while True:
 if x < 10:
     print('run forever')
     x += 1
 else:
     break

 


# # Module 4 Section 4 
# - while Boolean
# - while Boolean String Tests
# 

# In[12]:


green_count = 5

while green_count > 0:
    print(green_count,"!")
    green_count = green_count - 1
print("IGNITION!")


# In[15]:


seat_count = 1
while seat_count <=5:
    print ("seats booked: ", seat_count)
    seat_count = seat_count+1
print("No more, all", seat_count -1 , "seats are filled up!")


# In[2]:


"hello".isalpha()


# In[3]:


"".isalpha()


# In[ ]:


f_name = ""
while f_name.isalpha() == False:
    f_name=(input("Enter your First Name: "))
   
    
print(f_name.title(), "is recorded.")   


# In[ ]:


f_name = ""
while f_name.isalpha() == False:
    f_name=(input("Enter your First Name: "))
    if f_name.isalpha()== False:
        print("First name cannot contain two words")
    else:
        print(f_name.title(), "is recorded.") 


# In[ ]:


message = "hi"

while message.isupper() != True:
    message = input("Can\'t hear, please yell: ")
print (message, "is  yelled!")


# In[ ]:


number = ""
while number.isdigit()!=True:
    number=input("Enter a positive integer: ")
print(number,"is an integer!")


# # Module 4 Assignment 
# -A God Damn One!

# In[3]:


def str_analysis():
    last = ""
    while (last.isalpha() or last.isdigit()) != True:
        last = input("Give me a number or digit: ")
        if last.isdigit() == True:
            if int(last) >= 100:
                print(last, "is a pretty big number!")
            else:
                print(last,"is a smaller number than expected!")    
        elif last.isalpha() == True:
            print(last, "is all alphabetical characters!")
        else:
            print(last, "is neither all alphabetical nor all digits!")
        break
  
str_analysis()


# In[3]:


#rewriting the code fast!


last = ""
while (last.isalpha() or last.isdigit) != True:
    last = input("Enter a word or integer: ")
    if last.isdigit() == True:
        if int(last) <100:
            print(last,"is a small number.")
        else:
            print(last,"is a big number.")
    elif last.isalpha() == True:
        print(last,"is all alpha.")
    else: 
        print(last,"is neither all alpha nor all digits.")
    break   

