def guess_gender(surname):
    if surname[-3:] == 'ová':
        return 'You are probably woman!'
    else:
        return 'You are probablu man!'

print(guess_gender('Novák'))
print(guess_gender('Nováková'))
print(guess_gender('Straka'))
print(guess_gender('Straková'))
print(guess_gender('Hladík'))
print(guess_gender('Hladíková'))
print(guess_gender('Nový'))
print(guess_gender('Nová'))