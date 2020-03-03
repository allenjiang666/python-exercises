#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[7]:


#1. How many negative numbers are there?
mask = a < 0
mask.sum()


# In[9]:


#2. How many positive numbers are there?
len(a[a > 0]) # get the positive numbers and count the numbers of them


# In[17]:


#3. How many even positive numbers are there?
mask = (a > 0) & (a % 2 ==0)
mask.sum()


# In[21]:


#4. If you were to add 3 to each data point, how many positive numbers would there be?
mask = a + 3 > 0
mask.sum() 


# In[27]:


#5. If you squared each number, what would the new mean and standard deviation be?
b = a**2
mean_value = b.mean()
standard_deviation = a.std()


# In[32]:


#6. A common statistical operation on a dataset is centering. 
#     This means to adjust the data such that the center of the data is at 0. 
#     This is done by subtracting the mean from each data point. 
#     Center the data set.
a - a.mean()


# In[35]:


#7. Calculate the z-score for each data point. Recall that the z-score is given by:

#Z = (x −μ) / σ
(a - a.mean()) / a.std()


# In[36]:


import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.


# In[41]:


# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
sum_of_a


# In[42]:


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
min_of_a


# In[43]:


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
max_of_a


# In[46]:


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum(a) / len(a)
mean_of_a


# In[47]:


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = 1
for n in a:
    product_of_a *= n
product_of_a


# In[49]:


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [n ** 2 for n in a]
squares_of_a


# In[51]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [n for n in a if n % 2 != 0]
odds_in_a


# In[52]:


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = [n for n in a if n % 2 == 0]
evens_in_a


# In[134]:


## What about life in two dimensions? 
##A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

b = np.array(b)
b


# In[58]:


# Exercise 1 - refactor the following to use numpy. 
#Use sum_of_b as the variable. 
#**Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
sum_of_b


# In[61]:


b.sum()


# In[63]:


# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
min_of_b


# In[64]:


b.min()


# In[65]:


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
max_of_b


# In[66]:


b.max()


# In[76]:


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
mean_of_b


# In[75]:


b.mean()


# In[78]:


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
product_of_b


# In[79]:


b.prod()


# In[80]:


# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
squares_of_b


# In[81]:


b ** 2


# In[82]:


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
odds_in_b


# In[83]:


b[b % 2 != 0]


# In[84]:


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
evens_in_b


# In[85]:


b[b % 2 == 0]


# In[86]:


# Exercise 9 - print out the shape of the array b.
print(b)


# In[87]:


#Exercise 10 - transpose the array b.
b.transpose()


# In[141]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b.flatten()


# In[143]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b.reshape(6,1)


# In[107]:


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# In[112]:


# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
c = np.array(c)


# In[113]:


# Exercise 1 - Find the min, max, sum, and product of c.
c.max() 


# In[114]:


c.min()


# In[115]:


c.sum()


# In[116]:


c.prod()


# In[117]:


# Exercise 2 - Determine the standard deviation of c.
c.std()


# In[118]:


# Exercise 3 - Determine the variance of c.
c.var()


# In[122]:


# Exercise 4 - Print out the shape of the array c
print(c.shape)


# In[124]:


# Exercise 5 - Transpose c and print out transposed result.
print(c.transpose())


# In[127]:


# Exercise 6 - Get the dot product of the array c with c. 
c.dot(c)


# In[130]:


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
(c * c.transpose()).sum()


# In[131]:


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
(c * c.transpose()).prod()


# In[157]:


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d = np.array(d)
# d = d / 360 * 2 * np.pi
# d


# In[158]:


# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)


# In[159]:


# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)


# In[160]:


# Exercise 3 - Find the tangent of all the numbers in d
np.tan()


# In[161]:


# Exercise 4 - Find all the negative numbers in d
d[d < 0]


# In[162]:


# Exercise 5 - Find all the positive numbers in d
d[d > 0]


# In[163]:


# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)


# In[168]:


# Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(d))


# In[169]:


# Exercise 8 - Print out the shape of d.
d.shape


# In[171]:


# Exercise 9 - Transpose and then print out the shape of d.
d.transpose().shape


# In[172]:


# Exercise 10 - Reshape d into an array of 9 x 2
d.reshape(9, 2)


# In[ ]:




