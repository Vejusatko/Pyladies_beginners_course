'''Vytvoř hru sibenice podle následujícího popisu. Snaž se projekt rozdělit do funkcí a modulů s hezkými jmény, piš testy a dokumentační řetězce, funkční kousky dávej postupně do Gitu.
Počítač náhodně zvolí slovo (zatím třeba ze tří možností). Pro jednoduchost používej malá písmena a nepoužívej slova, ve kterých se stejné písmeno opakuje dvakrát (třeba čokoláda).
Zkus třeba slova: trávník, stromek, stavení.

Výchozí stav je řetězec s tolika podtržítky, kolik je ve vybraném slově písmen.
Výchozí počet neúspěšných pokusů je nula.

Stále dokola:

Zeptej se hráče na písmeno.
Pokud je to písmeno ve vybraném slově, zaměň ve stavu příslušná podtržítka za ono písmeno. (Bude se hodit řetězcová metoda index a funkce zamen ze srazu.)
Pokud dané písmeno není ve vybraném slově, započítej neúspěšný pokus.
Vypiš stav (slovo s případnými podtržítky).
Pokud už ve slově nejsou podtržítka, pogratuluj hráči a ukonči hru.
Vypiš počet neúspěšných pokusů a odpovídající obrázek. Funkci, která ti vrátí obrázek podle počtu pokusů, si můžeš zkopírovat z Gistu.
Pokud je počet neúspěšných pokusů 9 (nebo víc), hráč prohrál. Dej mu to najevo a ukonči program.'''

def return_state(state):
    for i in state:
        print(i, end=' ')

def hang(level):
    if level == 0:
        return """
        ~~~~~~~
        """
    elif level == 1:
        return """
        +
        |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif level == 2:
        return """
        +---.
        |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif level == 3:
        return """
        +---.
        |   |
        |
        |
        |
        |
        ~~~~~~~
        """
    elif level == 4:
        return """
        +---.
        |   |
        |   O
        |
        |
        |
        ~~~~~~~
        """
    elif level == 5:
        return """
        +---.
        |   |
        |   O
        |   |
        |
        |
        ~~~~~~~
        """
    elif level == 6:
        return """
        +---.
        |   |
        |   O
        | --|
        |
        |
        ~~~~~~~
        """
    elif level == 7:
        return """
        +---.
        |   |
        |   O
        | --|--
        |
        |
        ~~~~~~~
        """
    elif level == 8:
        return """
        +---.
        |   |
        |   O
        | --|--
        |  /
        |
        ~~~~~~~
        """
    else:
        return """
        +---.
        |   |
        |   O
        | --|--
        |  / \\
        |
        ~~~~~~~
        """

word = 'travnik'
state = '_' * len(word)

return_state(state)