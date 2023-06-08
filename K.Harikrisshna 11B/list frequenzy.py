l=eval(input("Enter list:"))
i=0
while i<len(l)-1:
    j=i+1
    c=1
    while j<len(l):
        if l[i]==l[j]:
            c+=1
            l.pop(j)
        else:
            j+=1
    print(l[i],"-",c)
    i+=1
