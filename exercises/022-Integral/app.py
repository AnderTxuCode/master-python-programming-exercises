# Your code here
def squares_dictionary(number):
    squares = {} 

    for i in range(1, number + 1): 
        squares[i] = i * i
    return squares 
print(squares_dictionary(8))