s=input("Enter string:")
def digend(s):
    l=s.split()
    b=0
    for i in l:
        if i[-1].isdigit():
            print(i,"ends with digit")
            b+=1
    print(b)

digend(s)            
