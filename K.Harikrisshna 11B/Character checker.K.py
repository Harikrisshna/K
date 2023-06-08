#Write a program to print whether a given character is an uppercase or a lowercase or a digit or any other character
ch=input("Enter character: ")
if ch>='A' and ch<='Z':
    print("Uppercase letter")
elif ch>='a' and ch<='z':
    print("Lowercase letter")
elif ch>='0' and ch<='9':
    print("Number character")
else:
    print("Special character")
