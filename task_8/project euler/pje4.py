def palindrome(s):
        s=str(s)
        x=(len(s)//2)   
        r=0
        if s[0]==s[-1]:
                r=r+1
        for i in range(x):
            if i==0:continue
            if s[i]==s[-i-1]:
                r=r+1
        if r==len(s)//2:
            return "yes"
        else:
            return "no"
t=int(input())
for k in range(t):
    n=int(input())
    l=[]
    for i in range(100,1001):
        for j in range(100,1001):
            s=i*j
            if palindrome(s)=='yes':
                if s<n:
                    l.append(s)
    print(max(l))
            
            
