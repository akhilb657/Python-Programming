import mysql.connector

conn = mysql.connector.connect(host="localhost",database="mydb",user="root",password ="test18")

if conn.is_connected():
    print("Connected to mysql DB")

cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO emp VALUES (3, 'Kittu', 9000)")
    conn.commit()
    print("Employee added")
except:
    conn.rollback()


cursor.close()
conn.close()