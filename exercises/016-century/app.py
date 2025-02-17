# Complete the function to return the respective number of the century
def century(year):
  centenar = str(year)
  total = int(centenar[0] + centenar[1]) + 1
  return total


# Invoke the function with any given year
print(century(1501))
