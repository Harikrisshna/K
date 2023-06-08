n=int(input("Enter number of elements:"))
i=0
t=()
while i<n:
    a=int(input("Enter elements:"))
    t+=(a,)
    i+=1
print("max:",max(t))
print("min:",min(t))
print("Sum:",sum(t))
print("Average:",sum(t)/n)
