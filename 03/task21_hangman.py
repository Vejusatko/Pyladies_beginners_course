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
    print()

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

def replace_character(slovo, stav, character):
    index = slovo.index(character)
    while stav[index] == '_':
        stav.replace(stav[index], character)
        index = slovo.index(character, index + 1)


.
..

secret_word = 'travnik'
word_lenght = len(secret_word)
alphabet = "abcdefghijklmnopqrstuvwxyz"
guessed_characters = []

def guessing():
    wrong_answer = 0
    state = '_' * word_lenght
    while wrong_answer <= 9:
        guess = input("Guess your character, puny human: ").lower()
        if guess not in alphabet:
            guess = input("Incorrect input! Enter a letter from a-z alphabet only: ").lower()
        elif guess in guessed_characters:
            guess = input("You already guessed that character, but I will give you another try: ").lower()
        else:
            guessed_characters.append(guess)
            if guess in secret_word:
                print("You got that right! Good for you!")
                for i in range(0,word_lenght):
                    if secret_word[i] == guess:
                        state = state.replace(state[i],guess)
                        return_state(state)
            else:
                wrong_answer += 1
                if wrong_answer == 9:
                    print("You looooosed!")
                    hang(9)
                else:
                    print("Wrong guess! Try again!")
                    hang(wrong_answer)

guessing()