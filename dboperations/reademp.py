import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Root123!')

if conn.is_connected():
    print("Connected to MySQL DB")

cursor = conn.cursor()

cursor.execute("SELECT * FROM emp")

# row = cursor.fetchone()

'''while row is not None:
    print(row)
    row = cursor.fetchone()'''


rows = cursor.fetchall()
print("Total no. of records:", cursor.rowcount)
for row in rows:
    print(row)

cursor.close()
conn.close()
