a=int(input("Enter year:"))
if a%100==0:
    if a%400==0:
        print(a,"is a century leap year")
    else:
        print(a,"is not a century leap year")
else:
    if a%4==0:
        print("It is a leap year")
    else:
        print("It is not a leap year")