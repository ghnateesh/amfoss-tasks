def staircase():
    n=int(input())
    for i in range(n+1):
        for j in range(i,n):
            print(' ',end='')
        print('#'*i)
staircase()
