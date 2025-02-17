# Complete the function to return the number of day of the week for k'th day of year
def day_of_week(k):

  dia = (k - 1 + 4) % 7
  return (dia)

# Invoke function day_of_week with an integer between 1 and 365
print(day_of_week(16))
