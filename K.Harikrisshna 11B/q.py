s=input("string: ")
st=""
for i in range len(s[0,-1,-1]):
    st+=s[i]
    if s==st:
        print("Palindrome")
    else:
        print("Not a palindrome")
