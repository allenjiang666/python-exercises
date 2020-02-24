#!/usr/bin/env python
# coding: utf-8

# Exercises
# 
# Create a file named 4.5_function_exercises.py for this exercise. After creating each function specified below, write the necessary code in order to test your function.
# 
# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
# Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
# Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
# Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
# Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed
# Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]
# Bonus
# 
# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.
# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27

# In[ ]:


# Define a function named is_two. It should accept one input and return True 
#if the passed input is either the number or the string 2, False otherwise.
def is_two(a):
    return str(a) == "2"

is_two(3)    


# In[ ]:


# Define a function named is_vowel. 
#It should return True if the passed string is a vowel, False otherwise.
def is_vowel(string):
    return string.lower() in "aeiou" and len(string) == 1
 
is_vowel("U")


# In[ ]:


#Define a function named is_consonant. 
#It should return True if the passed string is a consonant, False otherwise. 
#Use your is_vowel function to accomplish this.
def is_consonant(string):
    letters = "abcdefghijklmnopqrstuvwxyz" # isalpha()
    return len(string) == 1 and string.lower() in letters and not is_vowel(string)

is_consonant("c")


# In[ ]:


#Define a function that accepts a string that is a word. 
#The function should capitalize the first letter of the word if the word starts with a consonant.
def cap_word_begin_with_consonant(word):
    if is_consonant(word[0]):
        return word.capitalize()
    return word

cap_word_begin_with_consonant("aloha")


# In[ ]:


#Define a function named calculate_tip. 
#It should accept a tip percentage (a number between 0 and 1) and the bill total, 
#and return the amount to tip.
def calculate_tip(tip_percentage, bill_total):
    return tip_percentage * bill_total

calculate_tip(.15,100)


# In[ ]:


#Define a function named apply_discount. 
#It should accept a original price, and a discount percentage, 
#and return the price after the discount is applied.
def apply_discount(price, discount):
    return price * (100 - discount) * 0.01
assert apply_discount(100, 30) == 70


# In[ ]:


#Define a function named handle_commas. 
#It should accept a string that is a number that contains commas in it as input, 
#and return a number as output.
def handle_commas(string):
    new_string = ""
    for letter in string:
        if letter == ",":
            continue
        new_string = new_string + letter
    return float(new_string)                # string.replace(",", "")
handle_commas("123,456.789")


# In[ ]:


#Define a function named get_letter_grade. 
#It should accept a number 
#and return the letter grade associated with that number (A-F).
def get_letter_grade(num):
    if num >= 90:
        return "A"
    elif num >= 80:
        return "B"
    elif num >= 70:
        return "C"
    elif num >= 60:
        return "D"
    else:
        return "F"
get_letter_grade(90)


# In[ ]:


#Define a function named remove_vowels 
#that accepts a string and returns a string with all the vowels removed.
def remove_vowels(string):
    new_string = ''
    for letter in string:
        if is_vowel(letter):
            continue
        new_string += letter
    return new_string
remove_vowels("codeup")


# In[ ]:


#Define a function named normalize_name. 
#It should accept a string and return a valid python identifier, that is:
    #anything that is not a valid python identifier should be removed
    #leading and trailing whitespace should be removed
    # everything should be lowercase
    # spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed
def remove_special_characters(string):
    return ''.join([c for c in string if c.isalnum()  and  not c == " "])
def normalize_name(string):
    withou_special_char = remove_special_characters(string)
    return withou_special_char.lstrip().rstrip().lower().replace(' ', '_')
    

normalize_name('   aAF bc d     ')
            
    
        
        
    


# In[ ]:


#Write a function named cumsum that accepts a list of numbers 
#and returns a list that is the cumulative sum of the numbers in the list.
    #cumsum([1, 1, 1]) returns [1, 2, 3]
    #cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]
def cumsum(lst):
    new_lst = []
    cumsum = 0
    for n in lst:
        cumsum += n
        new_lst.append(cumsum)
    return new_lst
cumsum([1, 1, 1, 1])


# In[ ]:


#Create a function named twelveto24. 
#It should accept a string in the format 10:45am or 4:30pm 
#and return a string that is the representation of the time in a 24-hour format. 
#Bonus write a function that does the opposite.
def twelveto24(string):
    time = string.split(":")
    hour = time[0]
    minute = time[1]
    if string[-2] == "p":
        new_hour = str(int(hour) + 12)
    else:
        new_hour = hour  
    new_minute = minute[:2]
    new_time = new_hour + ":" + new_minute
    return  new_time
        
twelveto24("4:30pm")        
        


# In[ ]:


#Create a function named col_index. 
#It should accept a spreadsheet column name, 
#and return the index number of the column.
    #col_index('A') returns 1
    #col_index('B') returns 2
    #col_index('AA') returns 27
def col_index(column_name):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    column_index = []
    # get the index of each letter in column_name
    for letter in column_name[:]:
        for alpha in alphabet:
            if alpha == letter.lower():
                column_index.append(alphabet.index(alpha) + 1)
    #reverse the order of the index
    column_index = column_index[::-1]
    index = 0
    #cover 26th counting system to decimal system
    for i in range(len(column_index)):
        index += column_index[i] * 26 ** i
    return index
col_index("AB")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




