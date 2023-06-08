l=eval(input("Enter list:"))
i=0
while i<len(l)-1:
    j=i+1
    while j<len(l):
        if l[i]==l[j]:
            del l[j]
        else:
            j+=1
    i+=1
print(l)
        
