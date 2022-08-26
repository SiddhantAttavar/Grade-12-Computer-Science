l = int(input('Enter lower: '))
r = int(input('Enter upper: '))
for i in range(l, r + 1):
	for j in range(2, int(i ** 0.5) + 1):
		if i % j == 0:
			print(i, 'is compsite.')
			break