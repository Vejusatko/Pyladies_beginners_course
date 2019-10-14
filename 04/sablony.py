#sablony

soucet = 3 + 4
'''
print('Soucet je', soucet)

hlaska = 'Soucet je' + str(soucet)
print(hlaska)
'''
sablona1 = f"Soucet je {soucet}."

y_a = 'a'
jmeno = 'Elviro'
vysledek = 3 + 4
podpis = 'Vas program'

sablona2 = f"""
Mil{y_a} {jmeno},
Vas vysledek je {vysledek}.

S pozdravem
{podpis}
"""
print(sablona1)
print(sablona2)