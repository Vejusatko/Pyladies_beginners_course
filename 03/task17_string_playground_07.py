#task 11 remastered
numbers_range = int(input("For how many numbers you want to calculate square of number (zero included): "))
for number in range (numbers_range):
    result = number ** 2
    print(number,'na druhou je',result)

# task 12 remastered
letter = input("Choose a character you want to use for net drawing: ")
magnitude = int(input("Insert number which will tel me how many characters you want per column and row: "))
for row in range(magnitude):
    for column in range(magnitude):
        print(letter, end=' ')
    print()

# task 13 remastered
magnitude = int(input("I will show you a multiplication table. For how many numbers you want it (zero included): "))
for row in range(magnitude):
    for column in range(magnitude):
        print(row * column, end=' ')
    print()

#task 14 remastered
letter = input("Choose a character you want to use for stairs drawing: ")
steps = int(input("Insert number which will tel me how many steps you want your stairs to be long: "))
number = 1
for step in range (steps):
    for column in range (number):
        print(letter, end=' ')
    number += 1
    print()

#task 15 remastered
row = int(input("Insert how many rows you want to check: "))
for i in range(row):
    if i == 0:
        print('First line')
    else:
        print('Not first')

#task 16 remastered
letter = input("Choose a character you want to use for window drawing: ")
magnitude = int(input("Insert number which will tel me how many characters you want your window to be wide: "))
for row in range(magnitude):
    for column in range(magnitude):
        if row == 0 or row == (magnitude - 1):
            print(letter, end=' ')
        elif column == 0 or column == (magnitude - 1):
            print(letter, end=' ')
        else:
            print(' ', end=' ')
    print()