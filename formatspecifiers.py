# format sepecifiers = {value:flags} format a value based on what flags are inserted

price1 = 234.456
price2 = -23.45
price3 = 1200.4556

print(f"Price 1 is {price1:+.1f}")
print(f"Price 2 is {price2:+.1f}")
print(f"Price 3 is {price3:+.1f}")


price1 = 234897
price2 = 453882
price3 = 1200564


print(f"Price 1 is {price1:,}")
print(f"Price 2 is {price2:,}")
print(f"Price 3 is {price3:,}")


price1 = 1.234456
price2 = -237.45
price3 = 12.67

print(f"Price 1 is {price1:^10}")  # ^ makes values centre
print(f"Price 2 is {price2:^10}")
print(f"Price 3 is {price3:^10}")