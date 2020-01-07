a= list(map(int,input("enter rating ").split()))
b=list(map(int,input("enter rating ").split()))
score_a=0
score_b=0
for i in range(3):
    if a[i]>b[i]:
        score_a=score_a+1
    elif b[i]>a[i]:
        score_b=score_b+1
print(score_a,end=" ")
print(score_b)
