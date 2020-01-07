n=int(input())
l=[]
for i in range(n):
    x=input()
    l.append(x)
s=0
for i in range(n):
    if l[i]=='++x' or 'x++':
        s=s+1
    if l[i]=='--x' or 'x--':
        s=s-1
print(s)
