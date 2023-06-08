def stringcount(a):
    v=c=u=l=0
    for i in a:
        if i.isalpha():
            if i in 'AEIOUaeiou':
                v+=1
            else:
                c+=1
        if i.isalpha():
            if i.isupper():
                u+=1
            elif i.islower():
                l+=1
    print("No of uppercase characters:",u,"\nNo of lowercase characters:",l,"\nNo of vowels:",v,"\nNo of consonants:",c)
a=input("Enter string:")
stringcount(a)
