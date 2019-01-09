n=int(input())
l=[int(x) for x in input().split()]
k=int(input())
s=0
for i in range(0,k):
    s=s+l[i]
print(s)
