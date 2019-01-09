n,k=map(int,input().split())
for i in range(n+1,k):
    a=0
    x=i
    while i>0:
        p=i%10
        a=p**3+a
        i=i//10
    if a==x:
        print(a)
