#Reverse_a_string

a=input('Enter a string')
b=len(a)
b+=1
for i in range(-1,-b,-1):
    print(a[i],end='')