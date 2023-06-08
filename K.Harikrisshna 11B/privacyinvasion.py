d={}
n=int(input("Enter number of employees:"))
for i in range(n):
    na=input("Enter name:")
    bs=int(input("Enter salary:"))
    hr=int(input("Enter house rent:"))
    ca=int(input("Enter allowance:"))
    d[na]=[bs,hr,ca]
print("Name\t\t\tSalary")
for i in d:
    print(i,'\t\t\t',d[i][0]+d[i][1]+d[i][2])
