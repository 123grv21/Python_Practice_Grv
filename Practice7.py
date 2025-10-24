'''
Author: Gaurav Chakkarwar
Date: 24 Oct 2025
Topic: Dictionary Methods.
Description: In this set i demonstrate dictionary methods in python.
'''

# *** Dictionary Methods ***

# clear() - removes all key-value pairs

d = {'a':1, 'b':2}

d.clear()
print(d)

#copy() - returns a copy of the dictionary

d = {'a':1}
new_d = d.copy()
print(new_d)

# fromkeys() - creates a new dictionary from the given keys

keys = ['a','b']

d = dict.fromkeys(keys,0)
print(d)

# get() - returns value for key it exists,else rerturns default

d = {'a':1}
print(d.get('a'))
print(d.get('b',-1))

# items() - returns a view object with dictionary's key-value pairs

d = {'a':1, 'b':2}
print(list(d.items()))

# keys() - returns a view object with dictionary's keys

d = {'a':1, 'b':2}
print(list(d.keys()))

# pop() - removes specified key and returns its value

d = {'a':1, 'b':2}
val = d.pop('a')
print(val)
print(d)

# popitem() - removes and returns the last inserted key-value pair

d = {'a':1, 'b':2}
key,value = d.popitem()
print(key,value)

# setdefault() - returns a value if key exists, else inserts the key with a value and returns it

d = {'a':1}

print(d.setdefault('a',99))

print(d.setdefault('b',99))

print(d)

# update() - updates the dictionary with elements from another dictionary or an iterable

d = {'a':1}
d.update({'b':2})
print(d)

# values() - returns a view object with all values in the dictionary

d = {'a':1, 'b':2}
print(list(d.values()))