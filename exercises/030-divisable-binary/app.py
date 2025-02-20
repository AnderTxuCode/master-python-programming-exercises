# Your code here
def divisible_binary(lista):
    lista = lista.split(",")
    nuevaLista = []
    for i in lista:
        num = int(i, 2)
        if (num % 5 == 0):
            nuevaLista.append(i)
    
    return ", ".join(nuevaLista)


print(divisible_binary("0100,0011,1010,1001"))