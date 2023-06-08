n=int(input("Enter Limit: "))
c=65
for i in range(0,n+1):
    for j in range(1,i+1):
        print(chr(c),end=" ")
        c+=1
    print()

