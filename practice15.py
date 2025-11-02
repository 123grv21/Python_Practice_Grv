# string methods

name = input('Enter Your Name:')

phone_number = input("Enter Your Phone #:")

result = name.find(" ") # used to find first index of a character
print(result)

result = len(name)  # gets total length of the string
print(result)

result = name.rfind("o") # finding index number by reverse
print(result)

name = name.capitalize() # make first letter capital of given string
print(name)

name = name.upper() # converts the entire string to uppercase
print(name)

name = name.lower() # converts entire string to lowercase
print(name)

result = name.isdigit() # returns true if all characters are digits, otherwise false
print(result)

result = name.isalpha() # returns True if all characters are letters, otherwise false
print(result)

result = phone_number.count("-") # counts the total number of characters
print(result)

phone_number = phone_number.replace("-","") # replaces all occurances of "-" with an empty string
print(phone_number)



