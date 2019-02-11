n=input()
c=0
for i in n:
    if i.isnumeric()==False:
        if i.isalpha()==False:
            c=c+1
print(c)
