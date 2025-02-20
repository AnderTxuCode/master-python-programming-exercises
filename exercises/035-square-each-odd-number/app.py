# Your code here

def square_odd_numbers(args):
    var = args.split(",")
    lista = []
    for i in range(len(var)):
        num = int(var[i]) 
        if num % 2 != 0:  
            var[i] = str(num ** 2)  
    return ", ".join(var)  


print(square_odd_numbers("1,2,3,4,5,6,7,8,9"))