
# program for compute lcm

# def compute_lcm(x,y):
#     if x > y:
#         greater = x
#     else:
#         greater = y
#     while(True):
#         if((greater % x == 0) and (greater % y == 0)):
#             lcm = greater
#             break
#         greater += 1
#     return lcm

# num1 = 54
# num2 = 24

# print(f"The L.C.M. is", compute_lcm(num1,num2))

# program to print half pyramid using *

# rows = int(input("Enter number of rows:"))

# for i in range(rows):
#     for j in range(i+1):
#         print("*", end="")

#     print()


# program for to convert kilometers to miles

kilometers = float(input("Enter value in kilometers:"))

conv_fac = 0.621371

miles = kilometers * conv_fac

print("%0.2f kilometers is equal to %0.2f miles" %(kilometers,miles))
