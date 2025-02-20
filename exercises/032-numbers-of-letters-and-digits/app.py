# Your code here
def letters_and_digits(args):
    prueba = {"letras": 0, "num": 0}
    for letrita in args:
        prueba["letras"] += letrita.isalpha()
        prueba["num"] += letrita.isdigit()
    return prueba["letras"], prueba["num"]


letras, numeros = letters_and_digits("hello world! 123")
print("LETTERS "+ str(letras) + "\nDIGITS "+  str(numeros))