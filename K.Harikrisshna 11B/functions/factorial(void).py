#factorial(void)
def factorial(x):
    f=1
    for i in range(1,x+1):
        f*=i
    print("Factorial of",x,"is",f)
a=int(input("Input:"))
factorial(a)
