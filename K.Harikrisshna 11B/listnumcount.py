L=eval(input("Enter list: "))
l=int(int(input("Enter element:")))
c=0
for i in L:
    if i==l:
        c+=1
if c==0:
    print("Number not found")
else:
    print(l,"is present in list",c,"times")
