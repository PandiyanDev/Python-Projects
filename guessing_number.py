import random

# random number 1 to 10
n = random.randrange(1, 10)
# print(n)
guess = int(input('Enter your guessing number between 1 to 10: '))
while n != guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter the number again: "))
    elif guess > n:
        print("Too high")
        guess = int(input("Enter the number again: "))
    else:
        break
print('you guessed it right!!')