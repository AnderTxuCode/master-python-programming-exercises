# Complete the function to return the previous and next number of a given number
def previous_next(num):
  # Your code here
    siguiente = num + 1
    anterior = num - 1
    return (str(siguiente) + ", " + str(anterior))


# Invoke the function with any integer as its argument
print(previous_next(179))
