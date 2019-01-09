n,k=map(int,input().split())
l=[int(x) for x in input().split()]

s=0
for i in range(0,k):
    s=s+l[i]
print(s)
