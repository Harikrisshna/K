l=eval(input("Enter list:"))
n=int(input("Enter shifting number:"))
for i in range(len(l)-n):
    l.append(l[0])
    del l[0]
print(l)
