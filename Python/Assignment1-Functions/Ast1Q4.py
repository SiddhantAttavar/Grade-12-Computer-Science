def check(n):
	if n < 0:
		return n * n
	if n > 0:
		return n ** 0.5
	return 'zero'

x = int(input('Enter no.: '))
print('Answer:', check(x))