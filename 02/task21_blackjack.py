'''Naprogramuj hru Oko bere:

Začínáš se skóre 0 bodů.
V každém kole:
    Počítač vypíše, kolik máš bodů.
    Počítač se zeptá, jestli chceš pokračovat.
    Pokud byla odpověď „ne“:
        Hra končí.
    Jinak:
        Počítač „vybere kartu“ – náhodně vybere číslo od 2 do 10;
        vybranou hodnotu vypíše;
        přičte tuto hodnotu ke skóre.
    Pokud máš víc než 21 bodů:
        Počítač vypíše, že prohráváš;
        hra končí.
Po skončení hry počítač vypíše dosažené skóre.
Cílem hry je neprohrát a získat přitom co nejvíc bodů, ideálně 21.'''

from random import randint 
#variables setup
rounds = True
score = 0
answer = ''
card = randint(2,10)
#round beginning
while rounds == True:
    #current score anouncement and round check
    print('Your score is currently: ', score)
    answer = input('Do you wanna continue? Yes/No ')
    #correct input check
    while answer not in ['Yes','No']:
        print("That's not acceptable answer. Please answer yes or no!")
        answer = input('So again. Do you wanna continue? Yes/No ')
    #ending game
    if answer == 'No':
        rounds = False
        print('GAME OVER! Your score is: ', score)
    #game continues
    else:
        #score evaluation
        card = randint(2,10)
        score = score + card
        #so far so good
        if score <= 21:            
            print('Last card was: ',card)
        #not great, terrible
        else:
            rounds = False
            print('Last card was: ', card)
            print('You loosed! Your score is: ', score)
