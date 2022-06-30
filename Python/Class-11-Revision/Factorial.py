def factorial(n):
	res = 1
	for i in range(2, n + 1):
		res *= i
	return res

sum = 0
n = 4
for i in range(1, n + 1):
	sum += (-1) ** (i + 1) * i * 1.0 / factorial(2 * i + 1)
print(sum)

l = int(input('Enter left bound: '))
r = int(input('Enter right bound: '))
for i in range(l, r + 1):
	s = 0
	for c in str(factorial(i)):
		s += int(c)
	if c == i:
		print(i)