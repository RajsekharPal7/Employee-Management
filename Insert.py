import sqlite3

conn = sqlite3.connect("Employee.db")

cur = conn.cursor()

Name = input("Enter Name: ")
Department = input("Enter Department: ")
Salary = float(input("Enter Salary: "))
City = input("Enter City: ")


query = '''
    INSERT INTO Employee (Name, Department, Salary, City) values(?, ?, ?, ?)
'''

cur.execute(query,(Name, Department, Salary, City))

conn.commit()

print("Employee Inserted Successfully.")

conn.close()