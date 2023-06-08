#write a program to create a numeric tuple and find the frequenzy of a particular element w/o count function
t=eval(input('Enter tuple:'))
c=0
n=int(input("Enter element:"))
for i in range(0,len(t)):
    if t[i]==n:
        c+=1
print(n,"-",c)
