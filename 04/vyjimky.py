'''
def nacti_cislo():
    while True:
        odpoved = input('Nacti cislo: ')
        if obsahuje_jen_cislice(odpoved):
            return int(odpoved)
        else:
            print('Toto nebylo cislo')
'''
def nacti_cislo():
    while True:
        odpoved = input('Nacti cislo: ')
        try:
            return int(odpoved)
        except ValueError:
            print('Toto nebylo cislo')


print(nacti_cislo() + 1)
