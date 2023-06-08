def rec(a,b):
    c=a*b
    return c
def circ(a):
    c=3.14*a**2
    return c
def trig(a,b,c):
    d=(a+b+c)/2
    e=(d*(d-a)*(d-b)*(d-c))**0.5
    return e
def square(a):
    c=a**2
    return c
c='y' 
while c=='y' or c=='Y':
    j=int(input("1.Area of circle\n2.Area of rectangle\n3.Area of square\n4.Area of triangle\nEnter choice:"))
    if j==1:
        a=int(input("Enter radius:"))
        print(circ(a))
    elif j==2:
        a=int(input("Enter length:"))
        b=int(input("Enter breadth:"))
        print(rec(a,b))
    elif j==3:
        a=int(input("Enter side length:"))
        print(square(a))
    elif j==4:
        a=int(input("Side 1:"))
        b=int(input("Side 2:"))
        c=int(input("Side 3:"))
        print(trig(a,b,c))
    else:
        print("Invalid input")
    c=input("Do you want to continue?")
    if c=='n' or c=='N':
        print("Thank you")
        break
