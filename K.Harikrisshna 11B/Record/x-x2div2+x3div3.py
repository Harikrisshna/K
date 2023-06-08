x=int(input("Enter number: "))
n=int(input("Enter power: "))
a=0
d=1
for i in range(2,n+1):
    d=d*i
    if i%2==0:
        b=1*x**i/d
    else:
        c=-x**i/d
        a=x+b+c
print("Sum= ",a)
