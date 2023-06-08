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
