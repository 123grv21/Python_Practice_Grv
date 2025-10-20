# program for result checker
num1 = int(input("Enter The Number:"))
if num1 >= 89:
    print("Distinction!")
else:
    print("Pass!")

# program for eligiblity of vote

age = int(input("Enter The Age:"))
if age >= 18:
    print("You Are Eligible For The Vote!")
else:
    print("You Are Minor!")

# program for mul using function

def calculation(num1,num2):
    total = num1 * num2
    print(f"The Multiplication Is: {total}")
calculation(5,8)

# program for given number is divisible or not

num1 = int(input("Enter The First Number:"))
num2 = int(input("Enter The Second Number:"))

if num1 % 4 == 0 and num2 % 2 == 0:
    print("The Given Numbers Is Divisible By Both 4 & 3")
else:
    print("The Given Numbers Is Not Divisible By 4 & 3")

# program for how many vowels in given name

name = input("Enter The Name:")
vowels = "aeiouAEIOU"
for letter in name:
    if letter in vowels:
        print(f"{letter} is a vowel!")

# program for calculating volume of cuboid
l = int(input("Enter The Length:"))
b = int(input("Enter The Breadth:"))
h = int(input("Enter The Height:"))

volume = l * b * h
print(f"The Volume Of Cuboid Is: {volume}")



