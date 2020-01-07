s=input()
r=0
for i in range(len(s)):
    p=1
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            p=p+1
        else:break
    if p>=7:
        r=r+1
if r>=1:
    print('yes')
else:
    print('no')
            
            
        
            
