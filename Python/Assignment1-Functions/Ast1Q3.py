def Factorial(n):
	x = 1
	for i in range(2, n + 1):
		x *= i
	return x

x = int(input('Enter no.: '))
print('Answer:', Factorial(x))