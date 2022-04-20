class Power:
    def __init__(self,a,b):
        self.a=a 
        self.b=b 
    def calculate(self):
        print(self.a**self.b)

a=int(input('enter a no : '))
b=int(input('enter how much power you want : '))
x=Power(a,b)
x.calculate() 