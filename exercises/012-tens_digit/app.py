# Complete the function to return the tens digit of a given integer
def tens_digit(num):
  numerito = str(num)
  if (num > 9):
    numerito = numerito[len(numerito) - 2] 
  else:
    numerito = 0
  return numerito


# Invoke the function with any integer
print(tens_digit(1435670))
