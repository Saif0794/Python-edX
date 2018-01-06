
# coding: utf-8

# # FINAL
# 

# In[ ]:


#working long version
def adding_input():
    var = ""
    while True:
        var = input('Choose Report Type: ("A" or "T"): ')
        print('Report Types inclue All Items ("A") or Total Only ("T")')

        if var.upper() == "T":
            print('\nInput an integer to add to the total or "Q" to quit: ')

            total = 0
            while True:
                num1 = input("Enter an integer or Q: ")
                if num1.isdigit() == True:
                    total = total + int(num1)
                elif num1.upper() == "Q":
                    print("Total: \n", total)
                    break
                else:
                    print(num1, "is an invalid input")

        elif var.upper() == "A":
            print('\nInput an integer to add to the total or "Q" to quit: ')
            item = 0
            itemstr = ""
            while True:
                num2 = input("Enter an integer or Q: ")
                if num2.isdigit() == True:
                    item = item + int(num2)
                    itemstr = itemstr + "\n" + num2
                elif num2.upper() == "Q":
                    print("Items: ", itemstr)
                    print("Total: \n", item)
                    break
                else:
                    print(num2, "is invalid input")
        else:
            print(var, "is an invalid input!")


adding_input()


# In[ ]:


#working
def adding_input():
    var = ""
    while True:
        var = input('Choose Report Type: ("A" or "T"): ')
        print('Report Types inclue All Items ("A") or Total Only ("T")')
        
        if var.upper() == "T" or var.upper() == "A":
      
            print('\nInput an integer to add to the total or "Q" to quit: ')
            
            item = 0
            itemstr = ""
        
            total = 0
            while True:
                num1 = input("Enter an integer or Q: ")
                if num1.isdigit() == True:
                    total = total + int(num1)
                    item = item + int(num1)
                    itemstr = itemstr + "\n" + num1
                elif num1.upper() == "Q":
                    if num1 == "A": 
                        print("Items: ", itemstr)
                        print("Total: \n", item)
                    else:
                        print("Total: \n", item)
                        break
                else:
                    print(num1, "is invalid input")
        else:
            print(var, "is an invalid input!")
          


adding_input()

