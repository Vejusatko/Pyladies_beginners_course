'''
mocicny_dvou = []
for i in range(10):
    mocicny_dvou.append(2 ** i)

print(mocicny_dvou)
'''
balicek = []
for hodnota in list(range(2,11)) + ['J', 'Q', 'K','A']:
    for barva in 'Srdce', 'Kary', 'Piky','Krize':
        balicek.append (f"{hodnota}{barva}")

print(balicek)
