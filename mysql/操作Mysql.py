from pymysql import Connection

conn = Connection(host="", port=3306, user='root', password='', autocommit=True)

conn.select_db("test")

cursor = conn.cursor()

# cursor.execute("select * from student")
cursor.execute("insert into student(name) values('张三')")
# results = cursor.fetchall()

# print(results)
conn.close()
