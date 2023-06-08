s=input("Enter a string: ")
z=s.split()
p=input("Enter check string:")
c=0
for i in z:
    if i==p:
        c+=1
print(c)