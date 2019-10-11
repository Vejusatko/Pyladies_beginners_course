#Napiš program, který po zadání správného hesla vypíše nějakou tajnou informaci.
#Vhodné tajemství je třeba: V pátek jsem viděla černého havrana.

#password and pwd input
right_password = "jarjarissithlord"
password = input("You wanna know secret? \nFine!\nWhat's the password: ")
#secret
secret = "Dark side lied about the cookies! \nBut are you surprised?"
#pwd check
if password == right_password:
    print(secret)
else:
    print("Looks like you are not worthy of my secret!")