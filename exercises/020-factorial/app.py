# Your code here
def factorial (num):
    suma = 1
    for i in range(1, num + 1):
        suma = suma * i
    return suma

print(factorial(10))
    