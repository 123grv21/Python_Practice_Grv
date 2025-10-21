'''
Author: Gaurav Chakkarwar
Date: 21 Oct 2025
Topic: Python Function
Description: Practiced Python functions — including no parameters, multiple parameters, return statements, and default arguments to strengthen core function concepts.
'''

#*** Creating An Function ***

# Function with no parameter

def greet():
    print("Hello, World!")

greet()

# Function With Parameter

def student(name):
    print(f"The Name Of Student Is: {name}")

student("Gaurav")

# Function With Multiple Parameters

def employee(name,age,salary):
    print(f" The Name Of Employee Is:{name}\n The Age Of Employee Is:{age}\n The Salary Of Employee Is:{salary}")

employee("Kumar", 24, 50000)


# Function with return statement

def add(a,b):
    return a + b

total = add(5,4)
print(f"The Addition Is:", total)

# function with deafult arguments

def student(name, greeting="Hello"):
    print(f"{greeting} {name}")

student("Gaurav")
student("Gaurav","Good Morning") # this call overrides the default
