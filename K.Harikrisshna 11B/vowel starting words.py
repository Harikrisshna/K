s=input("Enter the string:")
p=s.split()
c=0
for i in p:
    if i[0] in 'aeiouAEIOU':
        print(i,end=" ")
        c+=1
print(" ",c,sep="\n")