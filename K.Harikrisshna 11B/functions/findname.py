phonebook=eval(input("Enter dictionary:"))
def findname(name):
    for i in phonebook:
        if i==name:
            del i
    print(phonebook)
name=input("Enter name:")
findname(name)
