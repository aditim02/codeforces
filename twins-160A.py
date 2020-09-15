def twinCoins():
    N=int(input())
    X=[int(i) for i in input().split()]
    X.sort(reverse=True)
    m=sum(X)
    l=0
    cnt=0
    for i in X:
        l+=i
        m-=i
        cnt+=1
        if l>m:
            return(cnt)
print(twinCoins())