'''
pi = 3.1415926
def obsah_kruhu(polomer):
    return pi * polomer ** 2

print(obsah_kruhu(100))
'''
'''
def nastav_x(hodnota):
    x = hodnota  # Přiřazení do lokální proměnné!
    print('V ramci funkce je x ',x)

nastav_x(40)
print('x =', x)
'''
from math import pi
obsah = 0
a = 30

def obsah_elipsy(a, b):
    obsah = pi * a * b  # Přiřazení do `obsah`
    a = a + 3  # Přiřazení do `a`
    return obsah

print(obsah_elipsy(a, 20))
print(obsah)
print(a)