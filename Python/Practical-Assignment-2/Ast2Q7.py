import pickle

def displayBikes(fileName, flag = False):
    with open(fileName, 'rb') as file:
        l = pickle.load(file)
        print('Make\tModel\tPrice\tRange/Charge')
        for i in l:
            if i[2] >= 80 or flag:
                print(i[0], i[1], i[2], sep = '\t')

def addBike(fileName):
    bike = ['TVS', 'Creon', 88000, 85]
    with open(fileName, 'rb') as file:
        l = pickle.load(file)
    l.append(bike)
    with open(fileName, 'wb') as file:
        pickle.dump(l, file)
    displayBikes(fileName, flag = True)

def displayDetails(fileName):
    make = input('Enter make: ')
    with open(fileName, 'rb') as file:
        l = pickle.load(file)
        for i in l:
            if i[0] == make:
                print(i[1], i[2])

fileName = 'ElectricBike.dat'
data = [
    ['Hero', 'Electric Photon', 72000, 60],
    ['Bajaj', 'Chetak A Brand', 85000, 80],
    ['Hero', 'Electric Dash', 68000, 72],
    ['TVS', 'iQube', 90000, 75],
]
with open(fileName, 'wb') as file:
    pickle.dump(data, file)
while True:
    op = input('Enter operation: Display bikes (D), Add bike (A) Display Products from Make (M), Exit(E): ').upper()
    if op == 'D':
        displayBikes(fileName)
    elif op == 'A':
        addBike(fileName)
    elif op == 'M':
        displayDetails(fileName)
    else:
        break

