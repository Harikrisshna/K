L=eval(input("Enter list:"))
i=0
while i<len(L)-1:
    c=1
    j=i+1
    while j<len(L):
        if L[i]==L[j]:
            c+=1
        else:
            L.pop(j)
    print(L[i],"-",c)
    i+=1
            
