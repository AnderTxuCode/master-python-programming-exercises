# Your code here
def list_and_tuple(*args):
    lista = []
    for i in args:
        lista.append(i)
    tupla = tuple(args)
    return lista, tupla

lista, tupla = list_and_tuple(34,67,55,33,12,98)
print(lista)
print(tupla)
