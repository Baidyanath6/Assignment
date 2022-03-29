def reverse_string(s):
    l=len(s)
    for i in range(l-1,-1,-1):
       print(s[i],end='')
    return s
    

s=input('enter the string u want to reverse')
reverse_string(s)





