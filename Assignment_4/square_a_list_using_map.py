a=[]
b= int(input('no of element you want to put in list '))
for i in range(b):
    x=int(input('enter the no '))
    a.append(x)
def square(a):
    return a**2
y=map(square,a)
print(a)
print(list(y))