import random, sys

secretNumber = random.randint(1,20)
print("Guess the number from 1 to 20")

for guess in range(1,7):
    guessTaken = int(input())

    if guessTaken < secretNumber:
        print("Your number is lower")
    elif guessTaken > 20:
        print("The number must be less than 20")
    else:
        break

if guessTaken == secretNumber:
    print("Congratulation! Your guess is correct")
else:
    print("Sorry! The number i was thinking is:"+ str(secretNumber))
