import mysql.connector

def delete(id):
    conn = mysql.connector.connect(host="localhost",database="mydb",user="root",password ="test18")

    if conn.is_connected():
        print("Connected to mysql DB")

    cursor = conn.cursor()

    str = "delete from emp where id='%d'"
    args = (id)

    try:
        cursor.execute(str % args)
        conn.commit()
        print("Employee deleted")
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

empId = int(input("Enter employee ID: "))
delete(empId)