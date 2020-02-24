#!/usr/bin/env python
# coding: utf-8

# # Make sure your promot gets what exactly you want
# 

# # Conditional Basics
# 
# prompt the user for a day of the week, print out whether the day is a weekday or a weekend
# 
# create variables and make up values for
# 
# the number of hours worked in one week
# the hourly rate
#     how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

# In[13]:


#     prompt the user for a day of the week, print out whether the day is Monday or not
day = input("what day is it? ")
if day == "Monday":
    print("Yes, it's Monday")
else:
    print("NO, it's not Monday")


# In[15]:


#     prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day = input("What day is it ")
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("It's a weekday")
elif day in ["Saturday", "Sunday"]:
    print("It's a weekend")
else:
    print("Invalid input!")


# In[2]:


#create variables and make up values for

#     the number of hours worked in one week
#     the hourly rate
#     how much the week's paycheck will be
#write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
hours =  int(input("your working hours:"))
hourly_rate = 10
weekly_paycheck = 0

if hours <= 40:
    weekly_paycheck = hours * hourly_rate
else:
    weekly_paycheck = 40 * hourly_rate + (hours - 40) * 1.5 * hourly_rate
print(weekly_paycheck)



# ## Loop Basics
# While
# 
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.

# In[16]:


i = 5
while i <= 15:
    print(i)
    i += 1


# # 
# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
# Alter your loop to count backwards by 5's from 100 to -10.
# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

# In[6]:


#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2


# In[4]:


#Alter your loop to count backwards by 5's from 100 to -10.
i = 100 
while i >= -10:
    print(i)
    i -= 5
    


# In[29]:


#Create a while loop that starts at 2, 
#and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
i = 2
while i < 1000000:#1_0 00_000
    print(i)
    i = i ** 2 # i *=i


# In[7]:


#Write a loop that uses print to create the output shown below.
i = 100
while i >= 5:
    print(i)
    i -= 5


# In[9]:


#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
num = int(input("Input a number: "))
for n in range(1,11):
    product = n * num
    print(str(num), "x", str(n), "=", str(product) )


# In[59]:


#Create a for loop that uses print to create the output shown below
for n in range(1,10):
    num = str(n) * n
    print(num)
    


# #break and continue
# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). 

# In[27]:


def is_even(num):
    return num % 2 == 0
num = input("Please input a number: ")
while num.isdigit() == False or is_even(int(num)) or (int(num) >= 50 or int(num) < 0):
    num = input("Please input a number: ")
    
        
    



# #
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

# In[11]:


num = int(input("Number to skip is: "))
i = -1
while i < 49:
    i += 2
    if i == num:
        print("Here is number you skipped:", str(i))
        continue
    print("Here is an odd number:", str(i))
    
    
       


# #
# The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

# In[95]:


num = int(input("Please input a positive number: "))
while num < 0:
    num = int(input("Please input a positive number: "))
for x in range(num+1):
     print(x)


# #
# Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.

# In[24]:


num = int(input("Please input a positive interger: "))
while num < 0:
    num = int(input("Please input a positive interger: "))
    
while num >= 0:
    print(num)
    num -= 1


# ##### One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# 
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

# In[100]:


for n in range(1,101):
    if n % 3 == 0 and n % 5 != 0 :
        print("Fizz")
    elif n % 5 == 0 and n % 3 != 0:
        print("Buzz")
    elif n % 15 == 0:
        print("FizzBuzz")
    else:
        print(n)


# #
# Display a table of powers.
# 
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

# In[11]:


num = int(input("What number would you like to go up to? "))
print("\nHere is your table!\n")
print("number | squared | cubed\n------ | ------- | -----")
for x in range(1,num + 1):
    print(str(x).ljust(6), "|", str(x**2).ljust(7), "|", str(x**3))


# #
# Convert given number grades into letter grades.
# 
# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:
# 
# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

# In[32]:


continuation = "Y"
while continuation == "Y":
    num = input("Please type in your grade: ")
    while not (num.isdigit() and int(num) > 0 and int(num) < 100): # Sequence of the condtion also matters
        num = int(input("Please type in your grade: "))
    num = int(num)
    if num in range(0, 60):
        print("F")
    elif num in range(60, 67):
        print("D")
    elif num in range(67, 80):
        print("C")
    elif num in range(80, 88):
        print("B")
    else:
        print("A")
    continuation = input("Do you wish to enter another grade, Y or N ?")


# #
# Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
# 
# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

# In[125]:


books = []
while input("Adding a new book, Y or N") == "Y":
    t = input("title: ")
    a = input("author: ")
    g = input("genre: ")
    D={"title": t, "author": a, "genre": g}
    books.append(D)
    print(books)


# In[129]:



while input("Do you want to check books in a genre, Y or N ? ") == "Y":
    genre = input("please input a book genre: ")
    for book in books:
        if book["genre"] == genre:
            print(book)
    if input("Do you want to continue, Y or N ? ") == "Y":
        continue
    else:
        break


# In[115]:





# In[ ]:





# In[ ]:





# In[ ]:




