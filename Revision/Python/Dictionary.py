# Introduction
# Accessing items using keys
a = {1: 0, 2: 1, 3: 2}
print(a[1])

# Mutability of dictionary
# Adding new item
a[4] = 3
print(a)

# Modifying existing item
a[3] = 5
print(a)

# Traversing
for i in a:
	print(i, a[i])

# Built-in functions
# len()
print(len(a))

# dict()
b = dict(one = 1, two = 2)
print(b)
c = dict([(1, 2), (3, 4), (5, 6)])
print(c)

# keys()
print(a.keys())

# values()
print(a.values())

# items()
print(a.items())

# get()
print(a.get(1))

# update()
a.update(b)
print(a)

# del
del a[1]
print(a)

# clear()
a.clear()
print(a)

# fromkeys()
a = dict.fromkeys((1, 2, 3), 1)
print(a)

# copy()
d = a.copy()
print(d)

# pop()
a.pop(1)
print(a)

# popitem()
print(a.popitem())

# setdefault()
a.setdefault(1, 0)
print(a)
a.setdefault(1, 1)
print(a)

# max()
print(max(a))

# min()
print(min(a))

# sorted()
print(sorted(a))

# Suggested programs
# Count frequency of characters
s = input('Enter string: ')
d = {}
for c in s:
	if c in d:
		d[c] += 1
	else:
		d[c] = 1
print('Char\tFrequency')
for c, v in d.items():
	print(c, v, sep = '\t')

# Dictionary of employees
n = int(input('Enter no. of employees: '))
d = {}
for i in range(n):
	name = input('Enter employee name: ')
	sal = int(input('Enter employee sal: '))
	d[name] = sal
name = input('Enter name of employee: ')
if name in d:
	print('Salary:', d[name])
else:
	print(name, 'not found')
