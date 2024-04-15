'''
The == operator (equal to) asks whether two values are the same as each other.
The = operator(assignment) puts the value on the right into the variable on the left.

and or not operates only one Boolean Value or expression. This makes it unary operator

Flow control statements often start with a part called the condition and are always followed by a block of code called the clause.
''' 
# name = 'Biwas'
# age = 3000
# if name == 'Biwas':
#     print('HI', name)
# elif age < 12:
#     print('Hey kiddo!')
# elif age >2000:
#     print('Hey young')
# else:
#     print('hey granny')

# spam = 0
# if spam < 5:
#     print('Hello world')
#     spam += 1
  

# while spam < 5:
#     print('Hello world')
#     spam += 1
  
# name = ''
# while True:
#     print('Please type your name.')
#     name = input()
#     if name == 'your name':
#         break
# print("THankyou")


# while True:
#     print('WHO ARE YOU?')
#     name = input()
#     if name != 'asish':
#         continue
#     print('Hello asish. What is the password?(Hint: idiot)')
#     password = input()
#     if password == 'idiotProgram':
#         break
# print('Access Granted')



# Conditions will consider some values in other data types equivalent to True and False. When used in conditions, 0, 0.0, and '' (the empty string) are considered False, while all other values are considered True.

# fname = ''
# while not fname:
#     print("Enter your name")
#     fname = input()
# print("HOw many guests will be there?")
# numOfGuests = int(input())
# if numOfGuests == int(input()):
#     print("Be sure to have enough room")
# print('DONE')

'''
QUESTION:
Run this program and give it some input. Until you claim to be Joe, the program shouldn’t ask for a password, and once you enter the correct password, it should exit.

Who are you?
I'm fine, thanks. Who are you?
Who are you?
Joe
Hello, Joe. What is the password? (It is a fish.)
Mary
Who are you?
Joe
Hello, Joe. What is the password? (It is a fish.)
swordfish
Access granted.


name = ''
while True:
    print("WHO ARE YOU?")
    name = input()
    if name != 'Asish':
        continue
    print('HELLO, ASISH. WHAT IS THE PASSWORD?(Hint password)')
    password = input()
    if password == 'goldfish':
        break
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')
    print('Access Granted', i, 'times')

total = 0
for num in range(101):
    total += num

print(total)
'''

import random, sys

for i in range(5):
    print(random.randint(1,10))

while True:
    print('Type exit to exit the program')
    response = input()
    if response == 'exit':
        sys.exit()
    print("YOU TYPED EXIT")

# Programs 