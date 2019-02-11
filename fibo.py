n=int(input())
n1=0
n2=1
c=0
if n>0:
    while c<n:
        s=n1+n2
        n1=n2
        n2=s
        print(n1)
        c=c+1
