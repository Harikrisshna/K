def series(c,n):
    x=1
    a=0
    for i in range(1,n+1):
        x=x*i
        if i%2==0:
            a+=(c**i)/x
        elif i==1:
            a+=c
        else:
            a+=-((c**i)/x)
    print(a)
c=int(input('Enter x:'))
n=int(input('Enter n:'))
series(c,n)
#Write a menu driven program to check whether a number is perfect,prime,armstrong or a palindrome
