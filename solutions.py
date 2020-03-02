#Write a function named isnegative. 
#It should accept a number 
#and return a boolean value based on whether the input is negative.
def isnegative(num):
    return num < 0

#Write a function named count_evens. 
#It should accept a list 
#and return the number of even numbers in the list.
def count_evens(nums):
    even_nums = 0
    for num in nums:
        if num % 2 == 0:
            even_nums +=1
    return even_nums

#Write a function named increment_odds. 
#It should accept a list of numbers 
#and return a new list with the odd numbers from the original list incremented.
def increment_odds(nums):
    odd_nums = []
    for num in nums:
        if num % 2 !=0:
            odd_nums.append(num + 1)
        else:
            odd_nums.append(num)
    return odd_nums


#Write a function named average. 
#It should accept a list of numbers 
#and return the mean of the numbers.
def average(nums):
    return sum(nums) / len(nums)


#Create a function named name_to_dict. 
#It should accept a string that is a first name and last name separated by a space, 
#and return a dictionary with first_name and last_name keys.
def name_to_dict(name):
    name_in_list = name.split()
    name_in_dict = dict([('first_name',name_in_list[0] ), ('last_name', name_in_list[1])]) 
    return name_in_dict
name_to_dict('Ada Lovelace')


#Write a function named capitalize_names. 
#It should accept a list of dictionaries 
#where each dictionary represents a person 
#and has keys first_name and last_name. 
#It should return a list of dictionaries with each person's name capitalized.
def capitalize_names(names):
    for name in names:
        name["first_name"] = name["first_name"].capitalize()
        name["last_name"] = name["last_name"].capitalize()
    return names


#Write a function named count_vowels. 
#It should accept a word 
#and return a number that is the number of vowels in the given word. 
#"y" should not count as a vowel.
def count_vowels(word):
    n = 0
    for letter in word:
        if letter.lower() in "aeiou":
            n += 1
    return n


#Write a function named analyze_word. 
#It should accept a string that is a word 
#and return a dictionary with information about the word: 
#the total number of characters in the word, the original word, and the number of vowels in the word.
def analyze_word(word):
    a = word
    b = 0
    c = 0
    for letter in word:
        b += 1
        if letter.lower() in "aeiou":
            c += 1
    word_info = {'word': a, 'n_letters': b, 'n_vowels': c}
    return word_info
