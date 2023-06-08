s=input("Enter string: ")
st=""
p=len(s)
for i in range(0,p):
    if i%2==0:
        st+=s[i].upper()
    else:
        st+=s[i]
print("New string is",st)