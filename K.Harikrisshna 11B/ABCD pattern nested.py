n=int(input("Enter Limit: "))
for i in range(0,n+1):
    for j in range(0,i):
        print(chr(64+i+j),end=" ")
    print()        
    