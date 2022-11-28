def displayproduct():
	global res, products
	print('Code\tName\tPrice')
	for i in products:
		print(i[0], i[1], i[2], sep = '\t')
	res += 'Display\n'

def addproduct():
	global res, products
	code = input('Enter code: ')
	name = input('Enter name: ')
	price = int(input('Enter price: '))
	products.append((code, name, price))
	res +=  'Push\t' + code + '\t' + name + '\t' + str(price) + '\n'
	displayproduct()

def removeproduct():
	global res, products
	if products:
		products.pop()
	else:
		print('No products available')
	res += 'Pop\n'
	displayproduct()

res = 'Operation\tCode\tName\tPrice\n'
products = []
while True:
	op = input('Enter operation Add (A) / Remove (R) / Display (D) / Exit (E): ').upper()
	if op == 'A':
		addproduct()
	elif op == 'R':
		removeproduct()
	elif op == 'D':
		displayproduct()
	else:
		break
print(res)
