# Classes In Python

#program for simple class

class employee:
    name = "Kumar"
    age = 25
    salary = 50000

kumar1 = employee()  # create object

print(kumar1.name,kumar1.age,kumar1.salary)


# program for multiple users

class employee:
    name = "Kumar"
    age = 25
    salary = 50000

kumar1 = employee()  # create first object

kumar1.name = "Rohit"  # change instance attribute

print(kumar1.name,kumar1.age,kumar1.salary)

virat = employee()  # create second object

virat.name = "Virat"  # assign new name

print(virat.name,virat.age,virat.salary)

# instance attribute

class employee:
    language = "Python" # this is class attribute
    salary = 120000

kumar1 = employee()

kumar1.language = "Java" # this is instance attribute

print(kumar1.language,kumar1.salary)

# note = instance attributes, take preferance over class attributes during assignmnet and retrival





