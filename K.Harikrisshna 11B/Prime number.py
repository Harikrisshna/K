p=int(input("Enter a number(>2):"))
for i in range (2,p):
    if p%i==0:
        print("Composite number")
else:
    print("Prime number")
