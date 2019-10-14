def obsah_ctverce(strana):
    if strana <= 0:
        raise ValueError('Strana musi byt kladna')
    return strana * strana

print(obsah_ctverce(5))
print(obsah_ctverce(-5))
