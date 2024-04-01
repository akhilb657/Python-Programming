import psycopg2

conn = psycopg2.connect(database="employeedb",user="test",password="password",host="localhost",port="5432")

print("Connected to employeedb")

cursor = conn.cursor()

cursor.execute("select * from employee")

rows = cursor.fetchall()

for row in rows:
    print("id",row[0])
    print("name",row[1])
    print("salary",row[2])


conn.close()