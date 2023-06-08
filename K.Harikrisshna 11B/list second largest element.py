L=eval(input("Enter list elements:"))
n=len(L)
for i in range(n-1):
    for j in range(n-i-1):
        if L[j]>L[j+1]:
            L[j],L[j+1]=L[j+1],L[j]
print("Second largest=",L[-2])
