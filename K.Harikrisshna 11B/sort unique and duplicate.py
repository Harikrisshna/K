L=eval(input("Enter list:"))
U=[]
D=[]
for i in range(len(L)):
    c=1
    for j in range(i+1,len(L)):
        if L[i]==L[j] and L[i] not in D:
            c+=1
    if c>1:
        D.append(L[i])
    elif L[i] not in D:
        U.append(L[i])
print("Duplicate",D)
print("Unique",U)
