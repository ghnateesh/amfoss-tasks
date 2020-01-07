n=int(input())
for i in range(n):
    t=int(input())
    p=[]
    q=[]
    for j in range(1,t):
        if j%3==0:
            p.append(j)
        if j%5==0:
            q.append(j)
        if j%15==0:
            q.remove(j)
    print(sum(p)+sum(q))
    
