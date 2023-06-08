name=input("Enter Name: ")
password=input("Enter Password: ")

if name=='admin' and password=='root':
    print("You are Admin")
elif name=='user' and password=='root':
    print("You are User")
elif name=='guest':
    print("You are Guest")
else:
    print("Invalid user")
