def letters_and_digits(args):
    prueba = {"letras": 0, "num": 0}
    for letrita in args:
        prueba["letras"] += letrita.islower()
        prueba["num"] += letrita.isupper()
    return prueba["letras"], prueba["num"]


letras, numeros = letters_and_digits("heLlo world! 123")
print("UPPERCASE "+ str(numeros) + "\nLOWCASE "+  str(letras))