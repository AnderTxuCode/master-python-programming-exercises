# Complete the function to return how many hours and minutes are displayed on the 24h digital clock
def digital_clock(n):
  horas = int(n / 60)
  minutos = int(n % 60)


  return str(horas) + ", " + str(minutos)

# Invoke the function with any integer (minutes after midnight)
print(digital_clock(150))
