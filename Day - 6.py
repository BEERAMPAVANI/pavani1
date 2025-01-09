#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

# Data for the DataFrame
data = {
    "Name": ["John", "Alice", "Bob", "Diana"],
    "Age": [28, 34, 23, 29],
    "Department": ["HR", "IT", "Marketing", "Finance"],
    "Salary": [45000, 60000, 35000, 50000]
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)


# In[7]:


# Display the first 2 rows of the DataFrame
print("First 2 rows:")
print(df.head(2))
df['Bonus'] = df['Salary'] * 0.1
print("\nDataFrame with Bonus column:")
print(df)
average_salary = df['Salary'].mean()
print(f"\nAverage Salary: {average_salary:.2f}")
filtered_df = df[df['Age'] > 25]
print("\nEmployees older than 25:")
print(filtered_df)


# In[ ]:




