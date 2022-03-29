def count(s):
    x=0
    y=0
    for i in s:
        if i.islower():
            y+=1
        elif i.isupper():
            x+=1
    print('No of uppercase :',x)
    print('No of lowerercase :',y)
    return s

s=input('enter the string')
count(s)

