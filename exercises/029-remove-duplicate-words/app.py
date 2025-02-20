# Your code here

def remove_duplicate_words (var):
    duplicate = var.split()
    unicos = set(duplicate)
    ordenado = sorted(unicos)
    return " ".join(ordenado)
    

print(remove_duplicate_words("hello world and practice makes perfect and hello world again"))