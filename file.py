import sqlite3
con=sqlite3.connect("data.db")
print("connection established")
#con.execute("CREATE TABLE student(name varchar(20),rollno int,place varchar(30))")
#con.execute("INSERT INTO student values('Arun',10,'Aluva')")
#con.execute("INSERT INTO student values('Alby',24,'banglore')")
#con.execute("INSERT INTO student values('Aksa',21,'kochi')")
x=con.execute("SELECT*FROM student")
for i in x:
    print(i)
con.commit()
con.close()