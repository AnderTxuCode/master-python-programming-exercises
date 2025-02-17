# Complete the function "digits_sum" so that it prints the sum of a three-digit number
def digits_sum(num):
  numerito = str(num)

  return int(numerito[0]) + int(numerito[1]) + int(numerito[2])


# Invoke the function with any three-digit number
print(digits_sum(123))
