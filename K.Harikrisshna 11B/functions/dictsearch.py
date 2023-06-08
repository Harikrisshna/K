def authenticate(users,loginid,password):
        if loginid in users:
           if users[loginid]==password:
               print("Access granted")
           elif users[loginid]!= password:
               print("Incorrect password")
        elif loginid not in users:
            print("Wrong credentials")

users=eval(input("Enter dictionary"))
loginid=input("Enter loginid")
password=input("Enter password")
authenticate(users,loginid,password)
