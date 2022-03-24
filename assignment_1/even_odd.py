x=int(input('enter a no'))
a=[]
for h in range (1,x+1):
    a.append(h)
print(a)
i=0
j=0
f=[]
g=[]
for d in a:
    if d%2==0:
       f.append(d)
       i+=1
    else:
        g.append(d)
        j+=1 
print('even numbers are :',f)
print('Number of even numbers :',i)
print('odd numbers are :',g)
print('Number of odd numbers :',j)