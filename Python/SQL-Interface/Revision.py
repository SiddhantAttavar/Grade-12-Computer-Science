# Import mysql
from mysql import connector

# Connect
connection = connector.connect(host = 'localhost', user = 'root', database = 'school')
cursor = connection.cursor()

# cursor.execute()
cursor.execute('select * from books;')
for row in cursor:
	print(row)
print()

# cursor.fetchall
cursor.execute('select * from books where Price > 500;')
data = cursor.fetchall()
print(data)
print()

# cursor.fetchone
cursor.execute('select * from books_issued;')
row = cursor.fetchone()
print(row)
cursor.fetchall()
print()

# cursor.fetchmany
cursor.execute('select * from books where Price < 500;')
data = cursor.fetchmany(5)
print(data)
print()

# cursor.rowcount
cursor.execute('select distinct Publisher from books')
data = cursor.fetchall()
print(data)
count = cursor.rowcount
print(count)
print()

# connection.commit
connection.commit()
