# program for profit & loss

sp = int(input("Enter Selling  Price:"))
cp = int(input("Enter Cost Price:"))

Profit = sp - cp

print("The Profit Is:",Profit)


cp = int(input("Enter Cost Price:"))
sp = int(input("Enter Selling  Price:"))

Loss = cp - sp

print("The Loss Is:",Loss)


# program for successive discounts

dis1 = int(input("Enter First Discount:"))
dis2 = int(input("Enter Second Discount:"))

TotalDiscount = dis1 + dis2 - (dis1 * dis2) / 100

print("The Successive Discount Is:", TotalDiscount)

# program for three successive discounts

dis1 = int(input("Enter First Discount:"))
dis2 = int(input("Enter Secondt Discount:"))
dis3 = int(input("Enter Third Discount:"))

NetDiscount = dis1 + dis2 + dis3 - (dis1 * dis2 + dis2 * dis3 + dis3 * dis1) / 100 + (dis1 * dis2 * dis3) / 10000

print("The Successive Discounts Are",NetDiscount)

# note = successive discounts means giving more than one discount one after another on the same time
