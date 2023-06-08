#write a program to find the sum of all 3 digit numbers ending with 0 in  a tuple
t=eval(input('Enter elements:'))
c=0
for i in range(0,len(t)):
    if t[i]>99 and t[i]<1000 and t[i]%10==0:
        c+=t[i]
print(c)