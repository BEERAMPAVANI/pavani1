#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculate_grade():
    marks1 = float(input("Enter marks for subject 1: "))
    marks2 = float(input("Enter marks for subject 2: "))
    marks3 = float(input("Enter marks for subject 3: "))
 
    average = (marks1 + marks2 + marks3) / 3
 
    if average >= 90:
        grade = "A"
    elif 80 <= average < 90:
        grade = "B"
    elif 70 <= average < 80:
        grade = "C"
    else:
        grade = "Fail"
 
    print(f"Grade: {grade}")
 
calculate_grade()


# In[ ]:




