# Arguments and parameters
# Positional parameters
def foo(a, b):
	return a + b
print(foo(1, 2))

# Default parameters
def bar(a = 1, b = 2):
	return a * b
print(bar(2))
print(bar(b = 3))
print(bar(1, 2))

# Scope of variable
def baz(a):
	global b
	c = 2
	return a + b + c
b = 1
print(baz(1))
