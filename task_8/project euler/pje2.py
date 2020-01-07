s=int(input())
for i in range(s):
    t=[1,2,3]
    n=int(input())
    for i in range(3,n):
        x=t[i-1]+t[i-2]
        if x<=n:
            t.append(x)
        else:
            break
    r=0
    for i in range(len(t)):
        if t[i]<=n and t[i]%2==0:
            r=r+t[i]
    print(r)

        
    
