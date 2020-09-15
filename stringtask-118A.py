k=str(input())
k=k.lower()
s=['a','e','i','o','u','y']
m=""
for i in range(0,len(k)):
    if k[i] not in s:
        m+='.'
        m+=k[i]
print(m) 