letter = 'x'
steps = 4
number = 1

for step in range (steps):
    for column in range (number):
        print(letter, end=' ')
    number += 1
    print(end='\n')