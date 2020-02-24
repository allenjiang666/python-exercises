#!/usr/bin/env python
# coding: utf-8

# In[2]:


students = [
    {
"id": "100001",
"student": "Ada Lovelace",
"coffee_preference": "light",
"course": "web development",
"grades": [70, 91, 82, 71],
"pets": [{"species": "horse", "age": 8}],
    },
    {
"id": "100002",
"student": "Thomas Bayes",
"coffee_preference": "medium",
"course": "data science",
"grades": [75, 73, 86, 100],
"pets": [],
    },
    {
"id": "100003",
"student": "Marie Curie",
"coffee_preference": "light",
"course": "web development",
"grades": [70, 89, 69, 65],
"pets": [{"species": "cat", "age": 0}],
    },
    {
"id": "100004",
"student": "Grace Hopper",
"coffee_preference": "dark",
"course": "data science",
"grades": [73, 66, 83, 92],
"pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
"id": "100005",
"student": "Alan Turing",
"coffee_preference": "dark",
"course": "web development",
"grades": [78, 98, 85, 65],
"pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
"id": "100006",
"student": "Rosalind Franklin",
"coffee_preference": "dark",
"course": "data science",
"grades": [76, 70, 96, 81],
"pets": [],
    },
    {
"id": "100007",
"student": "Elizabeth Blackwell",
"coffee_preference": "dark",
"course": "web development",
"grades": [69, 94, 89, 86],
"pets": [{"species": "cat", "age": 10}],
    },
    {
"id": "100008",
"student": "Rene Descartes",
"coffee_preference": "medium",
"course": "data science",
"grades": [87, 79, 90, 99],
"pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
"id": "100009",
"student": "Ahmed Zewail",
"coffee_preference": "medium",
"course": "data science",
"grades": [74, 99, 93, 89],
"pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
"id": "100010",
"student": "Chien-Shiung Wu",
"coffee_preference": "medium",
"course": "web development",
"grades": [82, 92, 91, 65],
"pets": [{"species": "cat", "age": 8}],
    },
    {
"id": "100011",
"student": "William Sanford Nye",
"coffee_preference": "dark",
"course": "data science",
"grades": [70, 92, 65, 99],
"pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
"id": "100012",
"student": "Carl Sagan",
"coffee_preference": "medium",
"course": "data science",
"grades": [100, 86, 91, 87],
"pets": [{"species": "cat", "age": 10}],
    },
    {
"id": "100013",
"student": "Jane Goodall",
"coffee_preference": "light",
"course": "web development",
"grades": [80, 70, 68, 98],
"pets": [{"species": "horse", "age": 4}],
    },
    {
"id": "100014",
"student": "Richard Feynman",
"coffee_preference": "medium",
"course": "web development",
"grades": [73, 99, 86, 98],
"pets": [{"species": "dog", "age": 6}],
    },
]


# #How many students are there?
# How many students prefer light coffee? For each type of coffee roast?
# How many types of each pet are there?
# How many grades does each student have? Do they all have the same number of grades?
# What is each student's grade average?
# How many pets does each student have?
# How many students are in web development? data science?
# What is the average number of pets for students in web development?
# What is the average pet age for students in data science?
# What is most frequent coffee preference for data science students?
# What is the least frequent coffee preference for web development students?
# What is the average grade for students with at least 2 pets?
# How many students have 3 pets?
# What is the average grade for students with 0 pets?
# What is the average grade for web development students? data science students?
# What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
# What is the average number of pets for medium coffee drinkers?
# What is the most common type of pet for web development students?
# What is the average name length?
# What is the highest pet age for light coffee drinkers?

# In[3]:


#How many students are there?
len(students)


# In[5]:


#How many students prefer light coffee? For each type of coffee roast?
len([student for student in students if student["coffee_preference"] == "light"])


# In[19]:


#How many types of each pet are there?
pets = sum([student["pets"] for student in students],[])
len(set([pet["species"] for pet in pets]))


# In[47]:


#How many grades does each student have? Do they all have the same number of grades?
nums_of_grades = [len(student["grades"]) for student in students]
if len(set(nums_of_grades)) == 1:
    print("all the same")
else:
    print("different")


# In[49]:


#What is each student's grade average?
[sum(student["grades"]) / len(student["grades"]) for student in students ]


# In[52]:


#How many pets does each student have?
[len(student["pets"]) for student in students]


# In[68]:


#How many students are in web development? data science?
num_of_student_in_webdev = len([(student["course"]) for student in students if student["course"] == "web development"])
num_of_student_in_datsci = len([(student["course"]) for student in students if student["course"] == "data science"])
print("%s students in data sicence" % num_of_student_in_datsci)
print("%d students in web develpment" % num_of_student_in_webdev)


# In[75]:


#What is the average number of pets for students in web development?
num_of_pets = [len(student["pets"]) for student in students if student["course"] == "web development"]
print("Average number of pets in wed development departmennt is %s" %(sum(num_of_pets) / len(num_of_pets)))


# In[87]:


#What is the average pet age for students in data science?
pets = [student["pets"] for student in students if len(student["pets"]) > 0 and student["course"] == "data science"]
age = [pet[0]["age"] for pet in pets] + [pet[1]["age"] for pet in pets if len(pet) == 2] + [pet[2]["age"] for pet in pets if len(pet) == 3]
print("Average age of pets in wed data science department is %s" %(sum(age) / len(age)))




# In[98]:


#What is most frequent coffee preference for data science students?
cof_pre = [student["coffee_preference"] for student in students if student["course"] == "data science"]
[cof_pre.count("light"), cof_pre.count("medium"), cof_pre.count("dark")]


# In[99]:


#What is the least frequent coffee preference for web development students?
cof_pre = [student["coffee_preference"] for student in students if student["course"] == "web development"]
[cof_pre.count("light"), cof_pre.count("medium"), cof_pre.count("dark")]


# In[104]:


#What is the average grade for students with at least 2 pets?
avg_of_each_stu = [sum(student["grades"]) / len(student["grades"]) for student in students if len(student["pets"]) > 1]
sum(avg_of_each_stu) / len(avg_of_each_stu)


# In[107]:


#How many students have 3 pets?
len([student["pets"] for student in students if len(student["pets"]) == 3])


# In[113]:


#What is the average grade for students with 0 pets?
grades_of_stu_with_0_pets =[student["grades"] for student in students if len(student["pets"]) == 0]
grades = []
for x in grades_of_stu_with_0_pets:
    for y in x:
        grades.append(y)
sum(grades) / len(grades)


# In[11]:


#What is the average grade for web development students? data science students?
avg_grd_of_each_wd = [sum(student["grades"]) / len(student["grades"]) for student in students if student["course"] == "web development" ]
avg_grd_of_wd = sum(avg_grd_of_each_wd) / len(avg_grd_of_each_wd)
avg_grd_of_each_ds = [sum(student["grades"]) / len(student["grades"]) for student in students if student["course"] == "data science" ]
avg_grd_of_ds = sum(avg_grd_of_each_ds) / len(avg_grd_of_each_ds)
print("Average grade of web development is %s ,\n Average grade of data sciecne is %d" 
      %(avg_grd_of_wd, avg_grd_of_ds) )


# In[15]:


#What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
avg_grd_of_each_drkcff = [sum(student["grades"]) / len(student["grades"]) for student in students if student["coffee_preference"] == "dark" ]
print(max(avg_grd_of_each_drkcff))
print(min(avg_grd_of_each_drkcff))


# In[19]:


#What is the average number of pets for medium coffee drinkers?
num_of_pets_by_each = [len(student["pets"]) for student in students if student["coffee_preference"] == "medium"]
avg_num_of_pets_by_medium_coffee_drinkers = sum(num_of_pets_by_each) / len(num_of_pets_by_each)
print(avg_num_of_pets_by_medium_coffee_drinkers)


# In[40]:


# Flat list very useful
#What is the most common type of pet for web development students?
pets_with_wd = [student["pets"] for student in students if student["course"] == "web development"]
pets_flattened = sum(pets_with_wd,[])
species =[]
for pet in pets_flattened:
    species.append(pet["species"])
new_species = list(set(species))
for pet in new_species:
    print(pet)
    print(species.count(pet))

    


# In[44]:


#What is the average name length?
name_len = [len(student["student"]) for student in students]
sum(name_len) / len(name_len)


# In[6]:


#What is the highest pet age for light coffee drinkers?
pets_with_lc = [student["pets"] for student in students if student["coffee_preference"] == "light"]
pets = sum(pets_with_lc,[])
max([pet["age"] for pet in pets])


# In[ ]:




