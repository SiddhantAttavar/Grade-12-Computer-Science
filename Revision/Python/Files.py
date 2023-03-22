# Text file
# Relative path
f1 = open('file1.txt', 'w+')
f1.close()
f2 = open('/home/siddhantattavar/file2.txt', 'w+')
f2.close()

# Basic operations
# read()
f = open('file.txt', 'r')
print(f.read())

# readline()
f.seek(0)
print(f.readline())

# readlines()
f.seek(0)
print(f.readlines())

# seek()
f.seek(0)
print(f.tell())
f.close()

# write()
f = open('file.txt', 'w+')
f.write('Example text\n')
f.seek(0)
print(f.read())

# writelines()
f.writelines(['Line 1\n', 'Line 2\n'])
f.seek(0)
print(f.read())
f.close()

# append
f = open('file.txt', 'a+')
f.write('Line 3\n')
f.seek(0)
print(f.read())
f.close()

# CSV file
import csv
f = open('file.csv', 'r')
reader = csv.reader(f, delimiter = ',')

# Reading files
for l in reader:
	print(l)
f.close()

# writerow()
f = open('file.csv', 'a')
writer = csv.writer(f)

# writwrow()
writer.writerow(['D', 12, 60])

# writwrows()
writer.writerows([['E', 9, 80], ['F', 6, 78]])
f.close()
f = open('file.csv', 'r')
reader = csv.reader(f)
for row in reader:
	print(row)
f.close()

# Binary file
import pickle

# Dump
f = open('file.dat', 'wb')
data = [0, 1, 2, 3]
for i in data:
	pickle.dump(i, f)
f.close()

# Load
f = open('file.dat', 'rb')
while True:
	try:
		print(pickle.load(f))
	except:
		break
f.close()
