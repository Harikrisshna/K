L=eval(input("Enter list:"))
for i in range(len(L)):
    for j in range(len(L)-1-i):
        if L[j]<0:
            L[j],L[j+1]=L[j+1],L[j]
print(L)
