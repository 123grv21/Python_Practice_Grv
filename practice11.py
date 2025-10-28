# program for total cost

price = int(input("Enter The Price:"))
quantity = int(input("Enter The Quantity Of Item:"))

TotalCost = price * quantity

print("The Total Cost Is:",TotalCost)


# program for area of circle

rad = int(input("Enter The Radius:"))

Area = 3.14 * rad * rad

print("The Area Of Circle Is:", Area)


# program for total & average

sub1 = int(input("Enter Marks In Subject 1:"))
sub2 = int(input("Enter Marks In Subject 2:"))
sub3 = int(input("Enter Marks In Subject 3:"))

Total = sub1 + sub2 + sub3

print("Total Is:",Total)

Average = Total / 3

print("The Average Is:", Average)


# program for finding square & cube

num = int(input("Enter A Number:"))

Square = num * num

print("The Square Is:", Square)

Cube = Square * num

print("The Cube Is:", Cube)