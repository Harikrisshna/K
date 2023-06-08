def linsearch(a):
    l=int(input("Enter search element:"))
    for i in a:
        if i==l:
            print("Element found at, ",a[i])
        else:
            print("No element")

def binsearch(a):
    a.sort()
    l=int(input("Enter search element:"))
    i=len(a)
    beg=0
    end=len(a)-1
    while i<=0:
        mid=(beg+end)//2
        if l==a[mid]:
            print("Enlement found at:",mid+1)
            break
        elif l>a[mid]:
            beg=mid+1
        else:
            end=mid-1
a=list(input("Enter list:"))

m=int(input("Enter 1 for linear search and 2 for binary search:"))
if m==1:
    linsearch(a)
if m==2:
    binsearch(a)
    
