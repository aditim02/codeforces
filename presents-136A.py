a=[]
j=0
n=int(input())
no=[int(i)for i in input().split()]
for j in range(0,n+1):
    for i in  range(0,n):
        if no[i]==j:
            if(i+1<n):
                a.append(i+1)
            elif(i+1==n):
                if i+1 in no:
                    a.append(i+1)
                else:
                    a.append(i)
            elif(i+1>n):
                a.append(i)
print(*a,sep=" ")  