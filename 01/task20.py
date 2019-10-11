#choose random number from range (0,3)
from random import randrange
number = randrange(3)
#print(number)

shape = ''
if number == 0:
    shape = 'triangle'
elif number == 1:
    shape = 'square'
else:
    shape = 'circle'
print(shape)

