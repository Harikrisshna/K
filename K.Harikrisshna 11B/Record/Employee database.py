#WAMDP to perform push,pop,display operation on stack containing employee details and given in following structure
#Employee no. and name, program should have push, pop, display
def push(employee):
    
a=int(input("1.Add Employee\n2.delete Employee\n3.View Employee details"))

employee=list()

while p=1:
    if a==1:
        name=input("Enter empoloyee name:")
        num=int(input("Enter employee number:"))
        push(employee,(name,num))
    elif a==2:
        pop(employee)
    elif a==3:
        display(employee)
p=int(input("Press 1 to continue"))
if p!=1:
    print("Thank you")
