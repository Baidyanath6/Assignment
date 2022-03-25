a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
b=len(a)
d=[]
for i in range(b):
    d.append(list(a[i]))
for i in range(b):
    d[i][0],d[i][1]=d[i][1],d[i][0]
d.sort(reverse=False)
for i in range(b):
    d[i][0],d[i][1]=d[i][1],d[i][0]
x=[]
for i in range(b):
    x.append(tuple(d[i]))
print(a)
print(x)





