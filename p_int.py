n,k=map(int,input().split())
for nu in range(n+1,k):
    for i in range(2,nu):
        if nu%i==0:
            break
    else:
        print(nu,end=" ")
