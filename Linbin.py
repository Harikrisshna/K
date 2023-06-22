def linsearch(x,s):
    for i in range(len(s)):
        if s[i]==x:
            print("Element found at",i)
            break
    else:
        print("Not found")

def binsearch(x,s):
    s.sort()
    print("Sorted list",s)
    beg=0
    last=len(s)-1
    while beg<=last:
        mid=(beg+last)//2
        if x==s[mid]:
            print("Element found at",mid)
            break
        elif x>s[mid]:
            beg=mid+1
        else:
            last=mid-1
    else:
        print("Not found")
s=eval(input("Enter a numeric list:"))
x=int(input("Enter search element:"))
print("1.Linear search\n2.Binary search")
c=int(input("Enter choice:"))
if c==1:
    linsearch(x,s)
elif c==2:
    binsearch(x,s)
else:
    print("Invalid hoice")
