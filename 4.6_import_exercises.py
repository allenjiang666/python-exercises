#!/usr/bin/env python
# coding: utf-8

# Create a file named 4.6_import_exercises.py to do your work in.
# 
# Import and test 3 of the functions from your functions exercise file.
# 
# Your functions exercise are not currently in a file with a name that can be easily imported. Copy your functions exercise file and name the copy functions_exercises.py.
# 
# Import each function in a different way:
# 
# import the module and refer to the function with the . syntax
# use from to import the function directly
# use from and give the function a different name
# For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.
# 
# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
# How many different ways can you combine two of the letters from "abcd"?
# Save this file as profiles.json inside of your exercises directory. Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
# 
# Total number of users
# Number of active users
# Number of inactive users
# Grand total of balances for all users
# Average balance per user
# User with the lowest balance
# User with the highest balance
# Most common favorite fruit
# Least most common favorite fruit
# Total number of unread messages for all users

# In[3]:


#Import and test 3 of the functions from your functions exercise file.

#Your functions exercise are not currently in a file with a name that can be easily imported. 
#Copy your functions exercise file and name the copy functions_exercises.py.

#Import each function in a different way:

    # import the module and refer to the function with the . syntax
    # use from to import the function directly
    # use from and give the function a different name


# In[76]:


# import the module and refer to the function with the . syntax
import functions_exercises
functions_exercises.calculate_tip(.2, 100)
calculate_tip(.1, 100)


# In[10]:


# use from to import the function directly
from functions_exercises import is_two as it
it


# In[12]:



from functions_exercises import col_index as ci
ci("AA")


# In[ ]:


#For the following exercises, read about and use the itertools module 
#from the standard library to help you solve the problem.

    #How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
    #How many different ways can you combine two of the letters from "abcd"?


# In[36]:


#How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
from itertools import permutations
len(list(permutations("abc123", 6)))


# In[38]:


#How many different ways can you combine two of the letters from "abcd"?
from itertools import combinations
len(list(combinations("abcd", 2)))


# In[ ]:


#Save this file as profiles.json inside of your exercises directory. 
#Use the load function from the json module to open this file, 
#it will produce a list of dictionaries. Using this data, 
#write some code that calculates and outputs the following information:
    # Total number of users
    # Number of active users
    # Number of inactive users
    # Grand total of balances for all users
    # Average balance per user
    # User with the lowest balance
    # User with the highest balance
    # Most common favorite fruit
    # Least most common favorite fruit
    # Total number of unread messages for all users


# In[45]:


import json
users = json.load(open("profiles.json"))
users


# In[65]:


# Total number of users 
total_number_of_users = len(users)


# In[68]:


# Number of active users
number_of_active_users = len([user for user in users if user["isActive"] == True])


# In[69]:


# Number of inactive users
number_of_inactive_users = len([user for user in users if user["isActive"] == False])


# In[74]:


# Grand total of balances for all users
functions_exercises.handle_commas
# 1. remove $ sign 2.remove "," and change type to float
balance = [functions_exercises.handle_commas(user['balance'][1:]) for user in users] 
total_balances = sum(balance)
total_balances


# In[70]:


#Average balance per user
average_balance = total_balances / total_number_of_users
average_balance


# In[81]:


# User with the lowest balance
lowest_balance = min(balance)
id_and_balance = [(user["index"],functions_exercises.handle_commas(user['balance'][1:])) for user in users]
for balance in id_and_balance:
    if balance[1] == lowest_balance:
        user_with_the_lowest_balance = balance[0]
user_with_the_lowest_balance


# In[85]:


#User with the highest balance
highest_balance = max(balance)
id_and_balance = [(user["index"],functions_exercises.handle_commas(user['balance'][1:])) for user in users]
for balance in id_and_balance:
    if balance[1] == highest_balance:
        user_with_the_highest_balance = balance[0]
user_with_the_highest_balance


# In[104]:


# Most common favorite fruit
fruits = [user['favoriteFruit'] for user in users ]
unique_fruits = list(set(fruits))
fruit_count = []
for u_f in unique_fruits:
    n = 0
    for fruit in fruits:
        if u_f == fruit:
            n = n +1
    fruit_count.append((u_f, n))
fruit_count
       


# In[105]:


#Least most common favorite fruit
fruits = [user['favoriteFruit'] for user in users ]
unique_fruits = list(set(fruits))
fruit_count = []
for u_f in unique_fruits:
    n = 0
    for fruit in fruits:
        if u_f == fruit:
            n = n +1
    fruit_count.append((u_f, n))
fruit_count


# In[133]:


# Total number of unread messages for all users
def remove_spaces(string):
    return ''.join([c for c in string if c.isdigit()])
unread_messages_in_num = [int(remove_spaces(user["greeting"][-18: -20:-1][::-1])) for user in users ]
total_unread_messages = sum(unread_messages_in_num)
total_unread_messages


# In[ ]:





# In[ ]:




