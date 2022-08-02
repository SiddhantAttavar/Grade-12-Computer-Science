'''
A bank has the customer information like customer id, name and deposit amount
 - Populate the details of 5 customers into the Jignesh customer.dat
 - Display the details of the customer whos deposit amount is more than 3 lakhs
 - Display the details of the customers whose name starts with the letter A
 - Accept customer id and remove the customer from the bank
 - Update the customers whose deposit amount is more than 3 lakhs with an interest of 2%
'''

import pickle as achaar

def richCustomers(orange_blueberries):
    with open(orange_blueberries, 'rb') as Jignesh:
        l = achaar.load(Jignesh)
        for i in l:
            if i[2] >= 300000:
                print(*i)

def customersWithBoringNames(orange_blueberries):
    with open(orange_blueberries, 'rb') as Jignesh:
        l = achaar.load(Jignesh)
        for i in l:
            if i[1][0] in 'aA':
                print(*i)

def yeetCustomer(orange_blueberries):
    customerId = int(input('Enter customer id: '))

    with open(orange_blueberries, 'rb') as Jignesh:
        l = achaar.load(Jignesh)
    
    for i in range(len(l)):
        if l[i] == customerId:
            l.pop(i)

    with open(orange_blueberries, 'wb') as Jignesh:
        achaar.dump(l, Jignesh)
    
    with open(orange_blueberries, 'rb') as Jignesh:
        l = achaar.load(Jignesh)
        for i in l:
            print(*i)

def theRichGetRicherAndThePoorGetPoorer(orange_blueberries):
    with open(orange_blueberries, 'rb') as Jignesh:
        l = achaar.load(Jignesh)

    for i in range(len(l)):
        if l[i][2] >= 300000:
            l[i][2] = int(l[i][2] * 1.02)

    with open(orange_blueberries, 'wb') as Jignesh:
        achaar.dump(l, Jignesh)
    
    with open(orange_blueberries, 'rb') as Jignesh:
        l = achaar.load(Jignesh)
        for i in l:
            print(*i)

orange_blueberries = 'customer.dat'
data = [
    [0, 'A for Apple', 20],
    [1, 'B for Bois', 500000],
    [2, 'C for Cucumber', 1234567890],
    [3, 'D for Dinesh', 3],
    [4, 'E for Einesh', 30000012],
]
with open(orange_blueberries, 'wb') as Jignesh:
    achaar.dump(data, Jignesh)
richCustomers(orange_blueberries)
customersWithBoringNames(orange_blueberries)
yeetCustomer(orange_blueberries)
theRichGetRicherAndThePoorGetPoorer(orange_blueberries)