n=input("Enter string: ")
a=input("Enter Character: ")
num=0
for i in n:
    if i==a:
        num+=1
print("Number of occurences: ",num)