def apple_sharing(n,k):
  # Your code here
  sobrante = k % n
  division = int(k / n)
  return (str(division) + ", "+str(sobrante))
 
print(apple_sharing(6,50))
