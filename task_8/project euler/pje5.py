t=int(input())
for i in range(t):
    n=int(input())
    k=0
    p=n
    while k==0:
        r=0
        for j in range(1,n+1):
            if p%j==0:
                r=r+1
    
        
        if r==n:
            print(p)
            break
        p=p+1

            
            
               
        
