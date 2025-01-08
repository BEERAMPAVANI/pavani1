#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ask the user to enter a positive integer
n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    # Use a for loop to print all numbers from 1 to n
    print("Numbers from 1 to", n, ":")
    for i in range(1, n + 1):
        print(i)
    
    # Use a while loop to calculate the sum of all numbers from 1 to n
    sum_of_numbers = 0
    counter = 1
    while counter <= n:
        sum_of_numbers += counter
        counter += 1
    
    # Print the result
    print("The sum of numbers from 1 to", n, "is:", sum_of_numbers)


# In[2]:


# Define a function named calculate_square
def calculate_square(n):
    return n ** 2

# Main program
try:
    # Ask the user to input a positive integer
    number = int(input("Enter a positive integer: "))
    
    if number <= 0:
        print("Please enter a positive integer.")
    else:
        # Call the calculate_square function
        result = calculate_square(number)
        # Display the result
        print(f"The square of {number} is: {result}")
except ValueError:
    print("Invalid input! Please enter a valid positive integer.")


# In[ ]:




