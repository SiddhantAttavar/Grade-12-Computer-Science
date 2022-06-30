s1, s2 = input('Enter words: ').split()

print('String 1 alternate: ')
for i in range(0, len(s1), 2):
	print(s1[i], end = '')
print()

print('String 2 alternate: ')
for i in range(0, len(s2), 2):
	print(s2[i], end = '')
print()

print('Reversed: ')
print(s1[::-1], s2[::-1])

print('Encryption: ')
for i in s1 + ' ' + s2:
	if i in 'aeiou':
		print('#', end = '')
	else:
		print(i, end = '')
print()