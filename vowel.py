n=input()
v="aeiou"
s=n.casefold()
if n.isalpha():
        if s in v:
                print("V")
        else:
                print("cons")
else:
        print("invalid")
        
