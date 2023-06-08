a=int(input("enter 1st number:"))
b=int(input("enter 2st number:"))
c=int(input("enter 3st number:"))

if a>b:
    if a>c:
        print("Greatest:",a)
        if c>b:
            print("Least:",b)
        else:
            print("Least:",c)
    else:
        print("Greatest:",c)
        print("Least:",b)

elif b>a:
    if b>c:
        print("Greatest:",b)
        if c>a:
            print("Least:",a)
        else:
            print("Least:",c)
    else:
        print("Greatest:",c)
        print("Least:",a)
