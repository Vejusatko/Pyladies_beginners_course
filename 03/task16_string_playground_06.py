'''Pomocí cyklů for a příkazu if napiš program, který z jednotlivých 'X' a mezer vypíše:

X X X X X X
X         X
X         X
X         X
X         X
X X X X X X
'''
letter = 'x'
magnitude = 6
for row in range(magnitude):
    for column in range(magnitude):
        if row == 0 or row == (magnitude - 1):
            print(letter, end=' ')
        elif column == 0 or column == (magnitude - 1):
            print(letter, end=' ')
        else:
            print(' ', end=' ')
    print(end='\n')