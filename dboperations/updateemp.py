import mysql.connector


def updateName(id, name):
    conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Root123!')

    if conn.is_connected():
        print("Connected to MySQL DB")

        cursor = conn.cursor()
        # str = "UPDATE emp SET name = %s WHERE id = %s"
        # args = (name, id)
        try:
            cursor.execute("UPDATE emp SET name = %s WHERE id = %s", (name, id))
            conn.commit()
            print("employee updated")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


empId = int(input("Enter employee id:"))
name = input("Enter new name")
updateName(empId, name)
