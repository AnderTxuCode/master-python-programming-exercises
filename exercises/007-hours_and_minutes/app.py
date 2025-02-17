def hours_minutes(seconds):
    # Calcular horas y minutos
    horas = int(seconds / 3600)
    minutos = int((seconds % 3600) / 60)
    
    # Retornar el resultado en formato de cadena
    return str(horas) + ", " + str(minutos)

# Invocar la función con 3900 segundos
print(hours_minutes(3900))