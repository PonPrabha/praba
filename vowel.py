n=input()
v="aeiou"
s=n.casefold()
if n.isalpha():
        if s in v:
                print("Vowel")
        else:
                print("Consonant")
else:
        print("invalid")
        
