a=[]
b=[]
for i in range(97,123):
    a.append(chr(i))
    b.append(i)
x=tuple(a)
c={}
for j in range(26):
    c.update({x[j]:b[j]}) 
print(c)