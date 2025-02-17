# Complete the function to return the swapped digits of a given two-digit integer
def swap_digits(num):
  # Your code here
  num = str(num)
  return num[1] + num[0]
   
# Invoke the function with any two-digit integer as its argument
print(swap_digits(30))
