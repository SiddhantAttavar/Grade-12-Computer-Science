# Introduction
# Indexing
a = [1, 2, 3]
print(a[0])

# List operations
# Concatenation
b = [4, 5, 6]
print(a + b)

# Repetition
print(a * 2)

# Membership
print(2 in a)
print(4 in a)

# Slicing
print(a[1:])
print(a[:3])
print(a[1:3])
print(a[0:3:2])
print(a[2:0:-1])

# Traversal
for i in a:
	print(i)

# Built-in functions
# len()
print(len(a))

# list()
c = list((1, 1, 2, 3))
print(c)

# append()
a.append(4)
print(a)

# extend()
a.extend(b)
print(a)

# insert()
a.insert(5, 2)
print(a)

# count()
print(c.count(1))
print(c.count(2))

# index()
print(c.index(1))

# remove()
c.remove(1)
print(c)

# pop()
a.pop()
print(a)
a.pop(3)
print(a)

# reverse()
a.reverse()
print(a)

# sort()
a.sort()
print(a)

# sorted()
d = sorted([2, 3, 1])
print(d)

# min()
print(min(a))
print(max(a))

# sum()
print(sum(a))

# nested lists
e = [
	[0, 1, 2],
	[3, 4, 5],
	[6, 7, 8]
]
print(e)

# Suggested programs:
# find max, min, mean of values in list
n = int(input('Enter no. of elements: '))
l = []
for i in range(n):
	l.append(int(input('Enter number: ')))
m = l[0]
M = l[0]
s = l[0]
for i in range(1, n):
	if l[i] < m:
		m = l[i]
	elif l[i] > M:
		M = l[i]
	s += l[i]
print('Min:', m)
print('Max:', M)
print('Avg:', s / n)

# Linear search
n = int(input('Enter no. of elements: '))
l = []
for i in range(n):
	l.append(int(input('Enter number: ')))
x = int(input('Enter number to search: '))
flag = False
for i in range(n):
	if a[i] == x:
		print(x, 'found at', i)
		flag = True
		break
if not flag:
	print(x, 'not found')
