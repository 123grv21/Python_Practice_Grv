# program for number guessing game

secret_number = 7
attempts = 3

for i in range(attempts):
    guess = int(input("Enter Your Guess (1-10):"))

    if guess == secret_number:
        print("Correct! You Win")
        break
    elif guess < secret_number:
        print("Too Low!")
    else:
        print("Too High!")
else:
    print("Out of attempts! The Number was",secret_number)

# program for vowel counter

text = input("Enter  a word or sentence:")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1
print("Total vowels:", count)
    
        
# program for prime number

num = int(input("Enter a number:"))

if num <= 1:
    print(num, "is not a prime number")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
