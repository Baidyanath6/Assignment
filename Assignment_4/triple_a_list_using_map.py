a=[]
b= int(input('no of element you want to put in list '))
for i in range(b):
    x=int(input('enter the no '))
    a.append(x)
def triple(a):
    return 3*a
y=map(triple,a)
print(a)
print(list(y))
