l = int(input('Enter lower bound: '))
r = int(input('Enter upper bound: '))

for i in range(l, r + 1):
	s = 0
	j = i
	flag = False
	while i:
		s += i % 10
		if i % 10 == 0:
			flag = True
		i //= 10
	if flag:
		print(j, s)