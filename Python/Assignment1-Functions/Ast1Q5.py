def palPrime(n):
	s = str(n)
	if s != s[::-1]:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True

c = 0
for i in range(100, 501):
	if palPrime(i):
		print(i, end = ' ')
		c += 1
		if c == 3:
			c = 0
			print()