'''
Author: Gaurav Chakkarwar
Date: 23 Oct 2025
Topic: if else conditions.
Description: In this set i practice 5 if else conditions problem 
'''

# program for pass or fail

score = int(input("Enter The Score:"))

if score > 50:
    print("Pass!")
else:
    print("Fail")

# program for positive,negative or zero 

num = int(input("Enter The Number:"))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

# program for greatest of two numbers

num1 = int(input("Enter The First Number:"))
num2 = int(input("Enter The Second Number:"))

if num1 > num2:
   print("Num1 Is Greater")
elif num2 > num1:
   print("Num2 Is Greater")
else:
   print("Number Is Equal")

# program for character type

char = input("Enter The Single Character:")

if char.isalpha():
    print("It Is A Alphabet")
elif char.isdigit():
    print("It Is A Digit")
else:
    print("It Is A Special Character")

# Note = isalpha() and isdigit() are python built in functions 

# program for triangle type

side1 = int(input("Enter The Length Of Side1:"))
side2 = int(input("Enter The Length Of Side2:"))
side3 = int(input("Enter The Length Of Side3:"))

if side1 == side2 == side3:
    print("This Is Equilateral Triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("This Is Isosceles Triangle")
else:
    print("a Scalene Triangle")



