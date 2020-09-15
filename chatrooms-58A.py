def check(st,k):
    
    cnt=0
    l=0
    
    if ((st=="" or k=="")):
        return cnt
        
    if(k[0] in st):
        l=st.index(k[0])
        cnt+=1
        if(len(st)==1):
            st=st[l:]
        else:
            st=st[l+1:]
        k=k[1:]
        return cnt + check(st,k) 
    else:
        return cnt


st=input()
t="hello"
cnt=check(st,t)
        
    
if(cnt==5):
    print('YES\n')
else:
    print('NO\n')