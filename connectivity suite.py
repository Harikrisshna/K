#ABC INFOTECH
import mysql.connector as mysql
con=mysql.connect(user='root',password='root',host='localhost',database='record')
cur=con.cursor()
cur.execute("Select * from employee where Salary>70000")
rec=cur.fetchall()
for i in rec:
    print(i)
con.close()
#OUTPUT
'''
('Bruce', '003', 100000)
('Selina', '004', 90000)
('Alfred', '005', 80000)
'''
import mysql.connector as mysql
con=mysql.connect(user='root',password='root',host='localhost',database='record')
cur=con.cursor()
cur.execute("Update employee set salary=salary+1000 where salary<80000")
print("Number of rows affected:",cur.rowcount)
con.commit()
con.close()
#OUTPUT
'''Number of rows affected: 3'''

import mysql.connector as mysql
con=mysql.connect(user='root',password='root',host='localhost',database='record')
cur=con.cursor()
sal=int(input("Enter salary:"))
d="Delete from employee where Salary= % s"%(sal)
cur.execute(d)
print("Number of rows affected:",cur.rowcount)
con.commit()
con.close()
#OUTPUT
'''Enter salary:80000
Number of rows affected: 1
'''
