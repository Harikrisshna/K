#WAMDP to perform push,pop,display operation on stack containing employee details and given in following structure
#Employee no. and name, program should have push, pop, display
def push(employee):
    x=input("Enter name:")
    y=input("Enter employee number:")
    employee.append([x,y])
def pop(employee):
    if employee==[]:
        print("Underflow")
    else:
        a=employee.pop()
        print("Employee name:",a[0],"\nEmployee number:",a[1])
def display(employee):
    if employee==[]:
        print("Underflow")
    else:
        print(employee[-1],"<-top")
        for i in range(len(employee)-2,-1,-1):
            print(employee[i][0],employee[i][1])
employee=list()
c='y'
while c=='y' or c=='Y':
    a=int(input("1.Add Employee\n2.Delete Employee\n3.Employee details\nEnter choice:"))
    if a==1:
        push(employee)
    elif a==2:
        pop(employee)
    elif a==3:
        display(employee)
    c=input("Do you want to continue?Y/N")
    if c=='n' or c=='N':
        print("Thank you")
        break
