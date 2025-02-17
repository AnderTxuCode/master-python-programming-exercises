# Complete the function to print the last two digits of an integer greater than 9
def last_two_digits(num):
    numerito = str(num)
    numero2 = str(num)
    if (num > 9):
        numerito = numerito[len(numerito) - 1]
        numero2 = numero2[len(numero2) - 2]
    return numero2 + numerito

# Invoke the function with any integer greater than 9
print(last_two_digits(1230))
