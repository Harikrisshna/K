def lin(l):
    p=int(input("Search element:"))
    for i in range(len(l)):
        if l[i]==p:
            print(p,"found at position",i+1)
            break
    else:
        print("Search unsuccessful")
def bin(l):
    l.sort()
    p=int(input("Enter search element:"))
    print(l)
    a=0
    b=len(l)-1
    v=(a+b)//2
    while a<=b:
        if p==l[v]:
            print("Element found at",m+1)
            break
        elif p>l[v]:
            a=m+1
        else:
            b=m-1
    else:
        print("Element not found")

l=eval(input("Enter list:"))
i=input("Enter choice:")
if  i==1:
    lin(l)
else:
    bin(l)
    
