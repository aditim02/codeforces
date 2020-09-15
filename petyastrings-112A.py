#petya and strings
k=str(input())
l=str(input())
k=k.lower()
l=l.lower()
e=[]
e.append(k)
e.append(l)
e.sort()
if k==l:
    print('0')
elif k==e[0]:
    print(-1)
else:
    print('1')