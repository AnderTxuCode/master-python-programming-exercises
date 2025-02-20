# Your code here


def net_amount(variable):
    splited = variable.split()
    suma = 0
    for i in range (len(splited)):
        if (splited[i] == "D"):
            suma = suma + int(splited[i + 1])
        elif (splited[i]== "W"):
            suma = suma - int(splited[i + 1])
    return suma
print(net_amount("D 300 D 300 W 200 D 100"))