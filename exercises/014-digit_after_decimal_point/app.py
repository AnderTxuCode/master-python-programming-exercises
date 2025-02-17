# Complete the function to return the first digit to the right of the decimal point
def first_digit(num):
  numerito = str(num)
  punto = numerito.find(".")
  return numerito[punto + 1]


# Invoke the function with a positive real number. ex. 34.33
print(first_digit(34.33))
