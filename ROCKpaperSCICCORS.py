import random, sys

print ('ROCK, PAPER,SCISSORS')

#these variable to keep track of the wins
wins = 0
losses = 0
ties = 0

#The main game loop
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins,losses,ties))
    while True:
        print('Enter you move:(r)ock,(p)aper, (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            print('Bye!')
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Type one of q, r, s or q.')

    #diplay what the person has chosen
    if playerMove == 'r':
        print('Rock versus...')
    elif playerMove == 'p':
        print('Paper versus...')
    elif playerMove == 's':
        print('Scissors versus...')

    #display what the computer chosen
    ranNum = random.randint(1,3)
    if ranNum == 1:
        comMove = 'r'
        print('ROCK')
    if ranNum == 2:
        comMove = 'p'
        print('PAPER')
    if ranNum == 3:
        comMove = 's'
        print('SCISSORS')

    #display win loss record
    if playerMove == comMove:
        print("it's a tie")
        ties = ties + 1
    elif playerMove == 'r' and comMove == 's':
        print('you win!')
        wins = wins + 1
    elif playerMove == 'p' and comMove == 'r':
        print('you win')
        wins = wins + 1
    elif playerMove == 's' and comMove == 'p':
        print('you win')
        wins = wins + 1
    elif playerMove == 'r' and comMove == 'p':
        print('you lose!')
        losses = losses + 1
    elif playerMove == 'p' and comMove == 's':
        print('you lose!')
        losses = losses + 1
    elif playerMove == 's' and comMove == 'r':
        print('you lose!')
        losses = losses + 1

















