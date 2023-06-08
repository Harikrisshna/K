print("Enter dictionary")
n=int(input("Enter number of customers:"))
d={}
for i in range(n):
    na=input("Enter name:")
    ph=input("Enter phone number:")
    it=input("Enter item name:")
    cs=input("Enter cost")
    d[na]=[ph,it,cs]

print("Name\t\t\tPhone number\t\tItemName\t\tCost")
for i in d:
        print(i,'\t\t\t',d[i][0],'\t\t\t',d[i][1],'\t\t\t',d[i][2])
