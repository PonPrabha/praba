n=int(input())
x=n
a=0
while n>0:
    p=n%10
    a=p**3+a
    n=n//10
if a==x:
    print("yes")
else:
    print("no")
    
