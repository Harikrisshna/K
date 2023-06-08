n=int(input("Enter number of names:"))
d={}
for i in range(n):
    na=input("Enter name:")
    ph=input("Enter phone number:\n")
    d[na]=ph
e=input("Enter search term:\n")
for i in d:
    if i==e:
        print("Name:",e,"Phone number:",d[i])
        break
else:
    print("Search unsuccessful")