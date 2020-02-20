# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)
# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruit =  [fruit[0].upper() + fruit[1:] for fruit in fruits]
print(capitalized_fruit)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
def more_than_two_vowels(word):
    n = 0
    for letter in word:
        if letter.lower() in ['a','e','i','o','u']:
            n += 1
    if n > 2: 
        return True  # fruits.count("a")

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if more_than_two_vowels(fruit)]
print(fruits_with_more_than_two_vowels)

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
def with_only_two_vowels(word):
    n = 0
    for letter in word:
        if letter.lower() in ['a','e','i','o','u']:
            n += 1
    if n == 2: 
        return True

fruits_with_only_two_vowels = [fruit for fruit in fruits if with_only_two_vowels(fruit)]
print(fruits_with_only_two_vowels)
# Exercise 5 - make a list that contains each fruit with more than 5 characters
def more_than_5_char(word):
    n = 0
    for letter in word:
        n += 1
    if n > 5:
        return True
fruit_with_more_than_5_char = [fruit for fruit in fruits if more_than_5_char(fruit)] # if len(fruit) > 5
print(fruit_with_more_than_5_char)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
def exactly_5_char(word):
    n = 0
    for letter in word:
        n += 1
    if n == 5:
        return True
fruit_with_exactly_5_char = [fruit for fruit in fruits if exactly_5_char(fruit)]
print(fruit_with_exactly_5_char)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
def less_than_5_char(word):
    n = 0
    for letter in word:
        n += 1
    if n < 5:
        return True
fruit_with_less_than_5_char = [fruit for fruit in fruits if less_than_5_char(fruit)]
print(fruit_with_less_than_5_char)
# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
def num_char(word):
    n = 0
    for letter in word:
        n += 1
    return n
number_of_char = [num_char(fruit) for fruit in fruits]
print(number_of_char)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
def contain_a(word):
    for letter in word:
        if letter.lower() == "a":
            return True
fruits_with_letter_a = [fruit for fruit in fruits if contain_a(fruit)] #if "a " in fruit
print(fruits_with_letter_a)
# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
even_numbers = [num for num in numbers if is_even(num)] # num % 2 == 0
print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
def is_odd(num):
    if num % 2 != 0:
        return True
    else:
        return False
odd_numbers = [num for num in numbers if is_odd(num)]
print(odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
def is_positive(num):
    if num > 0:
        return True
    else:
        return False
positve_numbers = [num for num in numbers if is_positive(num)] 
print(positve_numbers)
# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
def is_negative(num):
    if num < 0:
        return True
    else:
        return False
negative_numbers = [num for num in numbers if is_negative(num)]
print(negative_numbers)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
def more_than_2_numerals(num):
    if  abs(num) / 10 >= 1:
        return True
    else:
        return False
more_than_2_numerals = [num for num in numbers if more_than_2_numerals(num)]
print(more_than_2_numerals)
    
# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [num ** 2 for num in numbers]
print(numbers_squared)
# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [num for num in numbers if is_odd(num) and is_negative(num)]
print(odd_negative_numbers)
# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = [num + 5 for num in numbers]
print(numbers_plus_5)
# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not
def is_prime(num):
    if num <= 0:
        return False
    else:
        for n in range(2,abs(num)):
            if num % n == 0: 
                return False
            else:
                return True
primes = [num for num in numbers if is_prime(num)]
print(primes)
    