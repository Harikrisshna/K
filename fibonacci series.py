a=int(input("Enter number of digits: "))
x=0
y=1
z=1
print(x,',','1',',',y,',',end="")
while(z<a):
    x=y
    y=z
    z=x+y
    print(z,',',end=" ")
