import sqlite3

conn = sqlite3.connect("Employee.db")

cur = conn.cursor()

ID = input("Enter ID: ")

query = '''
    DELETE FROM Employee WHERE ID = ?
'''

cur.execute(query,(ID))

conn.commit()

print("Delete Employee Successfully")

conn.close()