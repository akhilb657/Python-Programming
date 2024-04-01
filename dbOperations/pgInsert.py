import psycopg2

conn = psycopg2.connect(database="employeedb",user="test",password="password",host="localhost",port="5432")

print("Connected to employeedb")

cursor = conn.cursor()

cursor.execute("insert into employee (name,sal) values ('Ranga', 7500)")

conn.commit()

print("Employee created")

conn.close()