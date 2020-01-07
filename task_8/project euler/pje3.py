t=int(input())
for i in range(t):
    n=int(input())
    k=0
    l=[]
    for i in range(2,n+1):
        if n%i==0:
            k=1
            for j in range(2,(i//2+1)):
                if i%j==0:
                    k=0
                    break
            if k==1:
                l.append(i)
    print(max(l))
                
        
        
