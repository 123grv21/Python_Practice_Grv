
# program for student information using functions
def student(name,age,fees):
  
  print(f"{name} {age} {fees}")

student("Gaurav",21,50000)


# program for swapping two numbers

a = 10
b = 20

print(f"Before swap: a = {a}, b = {b}")

a = a + b
b = a - b
a = a - b

print(f"After swap: a = {a}, b = {b}")


# program for finding volume of sphere

rad = int(input("Enter The Radius:"))

V = 4 / 3 * 3.14 * rad * rad * rad

print("Volume Of Sphere Is:", V)


