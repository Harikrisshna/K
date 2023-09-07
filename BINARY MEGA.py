import pickle
def insert():
    d={}
    d['Roll no']=int(input("Roll no:"))
    d['Name']=input("Name:")
    d['Mark']=int(input("Mark:"))
    d['Grade']=input("Grade")
    f=open('student.dat','ab')
    pickle.dump(d,f)
    f.close()
def read():
    f=open('student.dat','rb')
    print("Roll no\tName\tMark\tGrade")
    while True:
        try:
            R=pickle.load(f)
            print(R['Roll No'],'\t',R['Name'],'\t',R['Mark'],'\t',R['Grade'])
        except EOFError:
            break
    f.close()
def search():
    f=open('student.dat','rb')
    r=int(input("Enter roll no:"))
    while True:
        try:
            R=pickle.load(f)
            if R['Roll no']==r:
                print('Element found')
                print(R['Roll No'],R['Name'],R['Mark'],R['Grade'])
                break
        except EOFError:
            print("Not found")
            break
    f.close()
