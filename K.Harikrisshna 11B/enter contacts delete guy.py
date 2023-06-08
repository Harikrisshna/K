d={}
c='Y'
while c=='y' or c=='Y':
    na=input("Enter name:")
    ph=input("Enter phone number:")
    d[na]=[ph]
    c=input("Do you want to continue?Y/N")
    if c=='N':
        break
e=input("Enter name for deletion:")
if e in d:
    del e
else:
    print("Contact not found")
    
