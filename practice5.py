'''
Author: Gaurav Chakkarwar
Date: 22 Oct 2025
Topic: Python top 10 built in functions
Description: Practiced various python buiit in functions.
'''
# *** top 10 Python built in functions ***


# len() - Length of object

numbers = [1,2,3]
print(len(numbers))

name = "Python"
print(len(name))


# zip() - combine two or more iterables

a = [1,2]
b = ['a','b']

print(list(zip(a,b)))

# map() - apply a function to all elements

nums = [1,2,3]

result = map(str,nums) # convert all numbers to string
print(list(result))

# filter() - filter elements based on a condition

nums = [-1,0,1,2]

result = filter(lambda x: x > 0, nums) # keep only numbers > 0
print(list(result))

# any() - true if any element is True

values = [False,True,False] # check atlesat one item is True
print(any(values))

# all() - True if all elements are True

values = [False,True,True] # checks if every element is True
print(all(values))

# sum() - adds up numbers in a list or tuple

nums = [1,2,3]
print(sum(nums))

# sorted() - return a sorted version of an iterable

nums = [3,1,2]
print(sorted(nums))

# enumerate() - get index and value together

for index, letter in enumerate('abc'): # adds index numbers while looping
    print(index,letter)

# range() - generate a sequence of numbers

for i in range(3):
    print(i)







