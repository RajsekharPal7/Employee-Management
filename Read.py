import sqlite3

conn = sqlite3.connect("Employee.db")

cur = conn.cursor()

query = '''
    SELECT * FROM Employee
'''

cur.execute(query)

data = cur.fetchall()

print("\nEmployee Records: \n")

for row in data:
    print("ID: ", row[0])
    print("Name: ", row[1])
    print("Salary: ", row[2])
    print("City: ", row[3])
    print("*******************")

conn.close()


