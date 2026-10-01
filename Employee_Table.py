import sqlite3

conn = sqlite3.connect("Employee.db")

cur = conn.cursor()

query = '''
    CREATE TABLE IF NOT EXISTS Employee(
        ID integer Primary key AutoIncrement,
        Name text,
        Department text,
        Salary real,
        City text
    )
'''

cur.execute(query)

conn.commit()

print("Table Created Successfully.")

conn.close()