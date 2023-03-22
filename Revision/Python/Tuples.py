# Introduction
# Indexing
a = (1, 1, 2, 3)
print(a[0])

# Tuple operations
# Concatenation
b = (6, 5, 4)
print(a + b)

# Repetition
print(a * 2)

# Membership
print(1 in a)
print(4 in a)

# Slicing
print(a[1:])
print(a[:3])
print(a[1:3])
print(a[0:4:2])
print(a[4:1:-1])

# Built-in functions
# len()
print(len(a))

# tuple()
print(tuple([1, 2, 3]))

# count()
print(a.count(1))
print(a.count(2))
print(a.count(4))

# index()
print(a.index(2))

# sorted()
print(sorted(b))

# min()
print(min(a))

# max()
print(max(a))

# sum()
print(sum(a))

# Tuple assignment
c = (2, 3, 5)
print(c)

# Nested tuple
d = (
	(0, 1, 2),
	(3, 4, 5),
	(6, 7, 8)
)

# Suggested programs:
# Find min, max, mean of tuple
n = int(input('Enter no. of elements: '))
l = []
for i in range(n):
	l.append(int(input('Enter number: ')))
t = tuple(l)
m = t[0]
M = t[0]
s = t[0]
for i in range(1, n):
	if t[i] < m:
		m = t[i]
	elif t[i] > M:
		M = t[i]
	s += t[i]
print('Min:', m)
print('Max:', M)
print('Avg:', s / n)

# Linear search
n = int(input('Enter no. of elements: '))
l = []
for i in range(n):
	l.append(int(input('Enter number: ')))
t = tuple(l)
x = int(input('Enter number to search: '))
flag = False
for i in range(n):
	if t[i] == x:
		print(x, 'found at', i)
		flag = True
		break
if not flag:
	print(x, 'not found')

# Frequency of elements in tuple
n = int(input('Enter no. of elements: '))
l = []
for i in range(n):
	l.append(int(input('Enter number: ')))
t = tuple(l)
d = {}
for i in t:
	if i in d:
		d[i] += 1
	else:
		d[i] = 1
print('No.\tFrequency')
for i, x in d.items():
	print(i, x, sep = '\t')
