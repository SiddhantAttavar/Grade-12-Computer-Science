def readFile(fileName):
    with open(fileName, 'r') as file:
        print(file.read())

def printFirstLine(fileName):
    file = open(fileName, 'r')
    print(file.readlines()[0][12:])
    file.close()

def appendData(fileName):
    file = open(fileName, 'a')
    file.write('The methods defined in pickle module are used to perform I/O operations on a binary file.\nPickling functions used with a binary file are dump and load.')
