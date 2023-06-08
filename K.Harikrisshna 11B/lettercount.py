'''s=input("Enter string: ")
u=l=d=al=0
for i in s:
    if i.isalpha():
        al+=1
        if i.islower():
            d+=1
        elif i.isupper():
            u+=1
    elif i.isdigit():
        l+=1
print("Uppercase: ",u)
print("Lowercase: ",l)
print("Digits: ",d)
print("Alphabets: ",al)
'''
s=input("Enter string:")
u=l=v=c=0
for i in s:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    if i in 'aeiouAEIOU':
        v+=1
    else:
        c=u+l-v
print("Uppercase:",u)
print("Lowercase:",l)
print("Vowels:",v)
print("consonants:",c)
