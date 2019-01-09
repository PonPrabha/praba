n=int(input())
x=n
r=0
while n>0:
    a=n%10
    r=r*10+a
    n=n//10
if r==x:
    print("yes")
else:
    print("no")
    
