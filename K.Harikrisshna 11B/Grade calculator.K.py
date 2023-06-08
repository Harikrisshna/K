s1=int(input("Enter CSE marks: "))
s2=int(input("Enter first language marks: "))
s3=int(input("Enter Physics marks: "))
s4=int(input("Enter Maths marks: "))
s5=int(input("Enter English marks: "))

print(s1+s2+s3+s4+s5,"is the total marks")

p=(s1+s2+s3+s4+s5)/5

print("Percentage: ",p)

if p>90:
    print("A Grade")
elif p>80:
    print("B Grade")
elif p>70:
    print("C Grade")
elif p>60:
    print("D Grade")
else:
    print("FAILURE")
