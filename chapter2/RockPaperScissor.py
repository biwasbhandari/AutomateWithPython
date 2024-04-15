import random, sys

print("Rock, Paper, Scissors")

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'p' or playerMove == 'r' or playerMove == 's':
            break
    if playerMove == 'r':
        print("Rock versus...")
    elif playerMove == 'p':
        print("Paper versus...")
    elif playerMove == 's':
        print("Scissor versus...")
    
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print("Rock")
    elif randomNumber == 2:
        computerMove = 'p'
        print("Paper")
    elif randomNumber == 3:
        computerMove = 's'
        print("Scissor")

    if playerMove == computerMove:
        print("It's a tie")
        ties += 1
    
    elif playerMove == 'p' and computerMove == 's':
        print("You lose!")
        losses += 1
    
    elif playerMove == 'p' and computerMove == 'r':
        print("You won!")
        wins += 1

    elif playerMove == 's' and computerMove == 'p':
        print("You won!")
        wins += 1

    elif playerMove == 's' and computerMove == 'r':
        print("You lose!")
        losses += 1
    
    elif playerMove == 'r' and computerMove == 's':
        print("You won!")
        wins += 1

    elif playerMove == 'r' and computerMove == 'p':
        print("You lose!")
        losses += 1

    else:
        break

    if wins == int(10):
        print("You won ten times")
        sys.exit()
    if losses == int(10):
        print("You lose ten times")
        sys.exit()
