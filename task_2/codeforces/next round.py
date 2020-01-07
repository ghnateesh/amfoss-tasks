n,k=map(int,input().split())
a=list(map(int,input().split()))
if a[k-1]>0:
    s=0
    for i in range(n):
        if a[i]>=a[k-1]:
            s=s+1
    print(s)
else:
    print(0)
