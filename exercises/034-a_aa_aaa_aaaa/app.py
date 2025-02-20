# Your code here

def computed_value(number):
    ayuda = str(number)
    valor1 = ayuda
    valor2 = ayuda + ayuda
    valor3 = ayuda + ayuda + ayuda
    valor4 = ayuda + ayuda + ayuda + ayuda

    resultado = int(valor1) + int(valor2) + int(valor3) + int(valor4)
    return resultado


print(computed_value(9))