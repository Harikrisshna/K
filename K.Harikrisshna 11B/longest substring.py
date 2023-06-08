n=input("Enter string:")
p=n.split()
max=len(p[0])
w=""
for i in p:
    if len(i)>max:
       max=len(i)
       w=i
print(w)
