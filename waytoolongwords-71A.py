#too long words
N= int(input())
while(N>0):
    N-=1
    k= str(input())
    L=""
    if(len(k)<=10):
        print(k)
    else:
        L+=k[0]
        L+=str(len(k)-2)
        L+=k[len(k)-1]
        print(L)