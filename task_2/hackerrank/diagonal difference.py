def diagonalDifference():
    n=int(input())
    arr=[]
    for i in range(n):
        l=list(map(int,input().split()))
        arr.append(l)
    s=0
    for i in range(n):
        s=s+arr[i][i]
    k=0
    for i in range(n):
        k=k+arr[i][n-i-1]
    a=s-k
    if a>0:
        print(a)
    else:
        print(-a)
diagonalDifference()
        
