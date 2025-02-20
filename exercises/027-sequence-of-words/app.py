# Your code here
def sequence_of_words(nombre):
    lista = nombre.split(",")
    lista.sort()
    return ", ".join(lista)



print(sequence_of_words("without,hello,bag,world"))