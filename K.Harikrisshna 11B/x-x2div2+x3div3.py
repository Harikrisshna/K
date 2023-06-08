x=int(input("Enter number: "))
n=int(input("Enter power: "))
a=0
for i in range(2,n+1):
    if i%2==0:
        b=-1*x**i/i
    else:
        c=x**i/i
        a=x+b+c
print("Sum= ",a)
