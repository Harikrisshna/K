c='y' or c=='Y'
while c=='y' or c=='Y':
    
    print("1.Area of circle")
    print("2.Area of rectangle")
    print("3.Area of square")
    print("4.Circumference of circle")


    ch=int(input("Enter choice: "))

    if ch==1:
        a=int(input("Enter radius: "))
        ar=22/7*a*a
        print("Area of circle: ",ar)

    elif ch==2:
        a=int(input("Enter length: "))
        b=int(input("Enter breadth: "))
        ar=a*b
        print("Area of rectangle: ",ar)

    elif ch==3:
        a=int(input("Enter length: "))
        ar=a*a
        print("Area of square: ",ar)

    elif ch==4:
        a=int(input("Enter radius: "))
        ar=2*22/7*a
        print("Circumference of circle: ",ar)

    else:
        print("Invalid option")

    c=input("Do you want to choose another option? ")
    if c=="N" or c=="n":
        print("Thank you")
        break
 
