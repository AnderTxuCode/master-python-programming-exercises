# Your code here
def two_dimensional_list(i, j):
    arr = [[i * help for help in range(j)] for i in range(i)]  
    return arr

# Ejemplo de uso

print(two_dimensional_list(3, 5))