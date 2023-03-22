# Interface
import mysql.connector
db = mysql.connector.connect(host = 'localhost', user = 'root', password = '')
c = db.cursor()

# create database and table
c.execute('drop database if exists school')
c.execute('create database school')
c.execute('use school')
c.execute('create table Students(roll_no int PRIMARY KEY, name varchar(50), class int)')

# Insert
c.execute('insert into Students values(001, "A", 10)')
c.execute('insert into Students values(002, "B", 11)')
c.execute('insert into Students(roll_no, name) values(003, "C")')

# update
c.execute('update Students set class = 10 where class > 10')

# select
c.execute('select * from Students')
for row in c:
	print(row)
c.execute('select * from Students where class >= 10')
print(c.rowcount)
print(c.fetchone())
print(c.fetchall())
