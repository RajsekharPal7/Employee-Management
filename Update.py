import sqlite3

conn = sqlite3.connect("Employee.db")

cur = conn.cursor()

ID = input("Enter ID: ")
Salary = float(input("Enter Salary: "))

query= '''
    UPDATE Employee SET  Salary = ? WHERE ID = ?
'''

cur.execute(query,(Salary, ID))

conn.commit()

print("Employee updated Successfully")

conn.close()