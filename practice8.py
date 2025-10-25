'''
Author: Gaurav Chakkarwar
Date: 25 Oct 2025
Topic: python random library.
Description: In this set i learn some common random functions.
'''
# **Random Library ***


# generate random numbers

import random

num = random.random()
print(num)


# random integer in range

num = random.randint(1,10)
print(num)

# random choice from sequence

colors = ['red','green','blue']

choice = random.choice(colors)
print(choice)


# shuffle a list - randomly rearranges items in a list

cards = ['A','B','R','T','J']
random.shuffle(cards)
print(cards)

# seed - helps reproduce random results,useful for testing

random.seed(10)

print(random.randint(1,100))

# note - 1 seed changes = output changes,  2 same seed = output same every time
        
