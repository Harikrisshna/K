print("1.Perfect Number")
print("2.Armstrong Number")
print("3.Palindrome Number")
print("4.Prime Number")
a=int(input("Enter choice: "))

if a==1:
    a=int(input("Enter a number: "))
    s=0
    for i in range(1,a):
        if a%i==0:
            s+=i
    if s==a:
        print(a,'is a perfect number')
    else:
        print(a,'is not a perfect nuumber')
          
elif a==2:
    n=int(input("Enter number: "))
    N=n
    s=0
    while n>0:
        r=n%10
        s+=r**3
        n=n//10
    if N==s:
        print(s,"is an Armstrong number")
    else:
        print(s,"is not an Armstrong number")

elif a==3:
    n=int(input("Enter number: "))
    N=n
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if N==rev:
        print("Palindrome")
    else:
        print("Not palindrome")

elif a==4:
    p=int(input("Enter a number(>2):"))
    for i in range (2,p):
        if p%i==0:
            print("Composite number")
    else:
        print("Prime number")

else:
    print("Choice does not exist")
