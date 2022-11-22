def reverseStr(s):
	x = ''
	for i in range(len(s)):
		x += s[-i - 1]
	return x

w = input('Enter word: ')
print('Answer:', reverseStr(w))