import mysql.connector

def delete(id):
    conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Root123!')

    if conn.is_connected():
        print("Connected to MySQL DB")

        cursor = conn.cursor()
        str = "DELETE FROM emp WHERE id = %d"
        args = (id)
        try:
            cursor.execute(str % args)
            conn.commit()
            print("employee deleted")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

empId = int(input("Enter employee id:"))
delete(empId)
