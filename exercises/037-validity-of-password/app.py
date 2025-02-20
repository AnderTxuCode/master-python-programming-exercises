# Your code here

def valid_password(contrasena):
    i = 0
    isupper = 0
    isalphabe = 0
    isdollar = 0
    longitud = 0
    for i in range (len(contrasena)):
        if (contrasena[i].isupper()):
            isupper = 1
        elif (contrasena[i].isalpha()):
            isalphabe = 1
        elif (contrasena[i]=="$" or contrasena[i]=="#" or contrasena[i]=="@"):
            isdollar = 1
        if (len(contrasena) >= 6 and len(contrasena) <= 12):
            longitud = 1
        if (isupper == 1 and  isalphabe == 1 and  isdollar == 1 and  longitud == 1):
            return "Valid password"
    return "Not Valid password"


print(valid_password("ABd4@"))




#Al menos 1 letra entre [a-z].
#Al menos 1 número entre [0-9].
#Al menos 1 letra entre [A-Z].
#Al menos 1 carácter de [$#@].
#Longitud mínima de la contraseña: 6.
#Longitud máxima de la contraseña: 12.
#Tu programa debe aceptar una contraseña y verificarla según los criterios anteriores. Si la contraseña es validada correctamente, la función devuelve el siguiente string "Valid password", de lo contrario devuelve "Invalid password. Please try again".

#📎 Ejemplo de entrada:
