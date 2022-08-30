def addProduct(products):
	code = input('Enter product code: ')
	name = input('Enter product name: ')
	price = int(input('Enter price: '))
	products.append((code, name, price))
	print()

def removeProduct(products):
	if len(products):
		products.pop()

def displayProducts(products):
	print('Code\tName\tPrice')
	for product in products:
		print(*product, sep = '\t')
	print()

products = []
while True:
	op = input('Enter operation: Add (A) / Remove (R) / Display (D) / Exit (E): ').upper()
	if op == 'A':
		addProduct(products)
		displayProducts(products)
	elif op == 'R':
		removeProduct(products)
		displayProducts(products)
	elif op == 'D':
		displayProducts(products)
	else:
		break
