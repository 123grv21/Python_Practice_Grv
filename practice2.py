# simple calculator

print("*****Welcome To Calculator!*****")
num1 = int(input("Enter The First Number:"))
num2 = int(input("Enter The Second Number:"))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print(f"The Addition Is: {add}")
print(f"The Subtraction Is: {sub}")
print(f"The Multiplication Is: {mul}")
print(f"The Division Is: {div}")

print("***Thank You!***")

# program for area of rectangle

l = int(input("Enter The Length:"))
b = int(input("Enter The Breadth:"))

area = l * b

print(f"The Area Of Rectangle Is: {area}")

#program for conversion of celsius to fahrenheit

C = int(input("Enter The Temperature:"))

F = (C * 9 / 5) + 32

print(f"The Temperature In Fahrenheit Is: {F}")

# program for simple interest

P = int(input("Enter The Principal:"))
R = int(input("Enter The Rate:"))
T = int(input("Enter The Time:"))

SI = (P * R * T) / 100

print(f"The Simple Interest Is: {SI}")

# program for Average speed

distance = int(input("Enter The Distance In Km :"))
time = int(input("Enter The Time In Hours:"))

Speed = distance // time

print(f"The Average Speed Is: {Speed} Km/hr")
