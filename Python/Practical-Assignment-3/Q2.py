s = input('Enter sentence: ')
l = []
for c in s:
	l.append(c)
while l:
	print(l.pop(), end = '')
print()
