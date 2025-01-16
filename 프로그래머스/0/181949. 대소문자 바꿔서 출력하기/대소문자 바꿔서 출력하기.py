str = input()

if len(str) >=1 and len(str) <=20 :
    for i in str :
        if i.isupper() :
            print(i.lower(), end="")
        else :
            print(i.upper(), end="")
    