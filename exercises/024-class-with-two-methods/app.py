# Your code here
class InputOutString:
    def __init__(self):
        self.string = "" 

    def get_string(self):
        self.string = input("Introduce una palabra ")

    def print_string(self):
        print(self.string.upper())

obj = InputOutString()

obj.get_string() 
obj.print_string() 