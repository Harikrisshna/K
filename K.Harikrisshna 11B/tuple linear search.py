t=eval(input("Enter tuple:"))
e=int(input("Search element:"))
for i in range(len(t)):
    if t[i]==e:
        print(e,"found at position",i+1)
        break
else:
    print("Search unsuccessful")