#making of PCs round
from random import randrange
number = randrange(3)
pc_move = ''
if number == 0:
    pc_move = 'rock'
elif number == 1:
    pc_move = 'paper'
else:
    pc_move = 'scissors'
#users round
players_move = input("Rock, paper or scissors? ->")
#user input check
while players_move not in ('rock', 'paper', 'scissors'):
    print('Sorry, but I know only 3 words - rock, paper and scissors')
    players_move = input("So again! Rock, paper or scissors? ->")
#pc choosed
print('Computer choosed:', pc_move)
#user choosed rock
if players_move == 'rock':
    if pc_move == 'rock':
        print ("It's a draw!")
    elif pc_move == 'paper':
        print('You lost!')
    else:
        print('You won!')
#user choosed paper
elif players_move == 'paper':
    if pc_move == 'paper':
        print ("It's a draw!")
    elif pc_move == 'scissors':
        print('You lost!')
    else:
        print('You won!')
#user choosed scissors
elif players_move == 'scissors':
    if pc_move == 'scissors':
        print ("It's a draw!")
    elif pc_move == 'rock':
        print('You lost!')
    else:
        print('You won!')
