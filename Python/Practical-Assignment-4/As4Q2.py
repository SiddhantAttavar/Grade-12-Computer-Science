s = input('Enter string: ')
l = []
for i in s:
	l.append(i)
while l:
	print(l.pop(), end = '')
print()
