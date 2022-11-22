def numDigits(n):
	x = 0
	while n:
		x += 1
		n //= 10
	return x

x = int(input('Enter no.: '))
print('Answer:', numDigits(x))