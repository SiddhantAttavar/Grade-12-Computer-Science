def genPrimes(n):
	l = [True] * (n + 1)
	primes = []
	for i in range(2, n + 1):
		if l[i]:
			primes.append(i)
			for j in range(i + i, n + 1, i):
				l[j] = False
	return primes

def checkPalindrome(n):
	s = str(n)
	return s == s[::-1]

l = int(input('Enter lower bound: '))
r = int(input('Enter upper bound: '))
primes = genPrimes(r)
print('Palindromic Primes: ', end = '')
for i in primes:
	if i >= l and checkPalindrome(i):
		print(i, end = ' ')
print()