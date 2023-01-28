import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Root123!')

if conn.is_connected():
    print("Connected to MySQL DB")

cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO emp VALUES(3, 'Jill', 20000)")
    conn.commit()
    print("employee added")
except:
    conn.rollback()


cursor.close()
conn.close()
