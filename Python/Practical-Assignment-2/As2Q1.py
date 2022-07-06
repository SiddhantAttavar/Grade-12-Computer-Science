import pickle

def displayHeadsets(fileName, flag = False):
    with open(fileName, 'rb') as file:
        l = pickle.load(file)
        print('Code\tName\tPrice\tTechnology')
        for i in l:
            if i[2] >= 10000 and i[2] <= 15000 or flag:
                print(i[0], i[1], i[2], sep = '\t')

def numModels(fileName):
    with open(fileName, 'rb') as file:
        l = pickle.load(file)
        print(len(l))

def costRange(fileName):
    with open(fileName, 'rb') as file:
        l = pickle.load(file)
        if len(l) == 0:
            return
        minItem, maxItem = 0, 0
        for i in range(len(l)):
            if l[minItem][2] > l[i][2]:
                minItem = i
            elif l[maxItem][2] < l[i][2]:
                maxItem = i
        print('Code\tName\tPrice\tTechnology')
        print(l[minItem][0], l[minItem][1], l[minItem][2], l[minItem][3], sep = '\t')
        print(l[maxItem][0], l[maxItem][1], l[maxItem][2], l[maxItem][3], sep = '\t')

def deleteProduct(fileName):
    productCode = input('Enter product code: ')
    with open(fileName, 'rb') as file:
        l = pickle.load(file)
        for i in range(len(l)):
            if l[i][0] == productCode:
                l.pop(i)
                break
    with open(fileName, 'wb') as file:
        pickle.dump(l, file)
    displayHeadsets(fileName, True)

fileName = 'Headset1.dat'
data = [
    ['WX1000', 'Sony', 15456, 'Bluetooth'],
    ['HD800', 'Sennheiser', 35000, 'Wired'],
    ['DT990', 'Beyerdynamic', 23000, 'Wired'],
    ['PRO2', 'Plantronics', 12000, 'Bluetooth'],
]
with open(fileName, 'wb') as file:
    pickle.dump(data, file)
displayHeadsets(fileName)
costRange(fileName)
deleteProduct(fileName)
