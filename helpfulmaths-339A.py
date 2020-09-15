k=str(input())
if "+" not in k:
    print(k)
else:
    s=k.split("+")
    s.sort()
    x='+'
    print(x.join(s))