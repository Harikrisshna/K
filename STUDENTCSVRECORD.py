import csv
f=open('student.csv','w+')
l=[("st1","password"),('st2','password')]
t=csv.writer(f)
t.writerows(l)
f.seek(0)
r=csv.reader(f)
w=list(r)
while True:
    u=input("Enter user ID:")
    p=input("Enter password:")
    for i in w:
        if i[0]==u:
            if i[1]==p:
                print("Welcome student")
                break
            else:
                print("Wrong Password")
        else:
            print("Invalid ID")
    break
f.close()
    
