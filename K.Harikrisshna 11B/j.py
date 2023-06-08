'''Write a menu driven program to input your friends names and their phone numbers and store them in a dictionary as key value pairs.perform the following operations
1.Display name and phone numbers of all your friends
2.Add a new key value pair in this dictionary and display modified dictionary
3.Delete a particular friend from the dictionary
4.Modify the phone number of an existing friend
5.Check if a friend is present in the dictionary or not
6.Display dictionary in sorted order of names'''
print("Enter dictionary")
n=int(input("Enter number of friends:"))
d={}
for i in range(n):
    na=input("Enter name:")
    ph=input("Enter phone number:")
    d[na]=ph
c=='y' or c=='Y'
while c=='y' or c=='Y':
    
    print("1.Display name and phone numbers of all your friends\n2.Add another friend\n3.Delete a particular friend \n4.Modify the phone number of an existing friend\n5.Check if a friend is present in the dictionary or not\n6.Display dictionary in sorted order of names")
    g=int(input("Enter choice:"))
    if g==1:
        print("Name\t\t\tPhone number")
        for i in d:
            print(i,'\t\t\t',d[i])
    if g==2:
        na=input("Enter name:")
        ph=input("Enter phone number:")
        d[na]=ph
        print("Name\t\t\tPhone number")
        for i in d:
            print(i,'\t\t\t',d[i])
    if g==3:
        na=input("Enter name:")
        del d[na]
        print("Name\t\t\tPhone number")
        for i in d:
            print(i,'\t\t\t',d[i])
    if g==4:
        na=input("Enter name:")
        ph=input("Enter phone number:")
        d[na]=ph
        print("Name\t\t\tPhone number")
        for i in d:
            print(i,'\t\t\t',d[i])
    if g==5:
        c=input("Search:")
        for i in d:
            if i==c:
                print("Phone number:",d[i])
                break
        else:
            print("No such person")
    if g==6:
        print("Sorted dictionary:",sorted(d.items()))

    c=input("Do you want to choose another option? ")
    if c=="N" or c=="n":
        print("Thank you")
        break
 
