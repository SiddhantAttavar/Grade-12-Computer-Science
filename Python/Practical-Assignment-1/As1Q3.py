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
    file.close()

def searchAndReplace(fileName):
    file = open(fileName, 'r')
    s = file.read()
    s = s.replace('object', 'handle')
    file.close()
    file = open(fileName, 'w')
    file.write(s)
    print(s)
    file.close()

def deletePythonLines(fileName):
    file = open(fileName, 'r')
    s = []
    for l in file.readlines():
        if 'Python' not in l:
            s.append(l)
    file.close()
    file = open(fileName, 'w')
    file.writelines(s)
    file.close()

s = 'All reading and writing functions work sequentially in a text file.\nPython provides seek and tell methods to access the contents of a file randomly.\ntell() method returns an integer giving the current position of object in the file.\nThe integer returned specifies the number of bytes from the beginning of the file till the current position of file object.\nseek() method can be used to position the file at a particular place in the file. In seek method offset is used to calculate the position of file object in the file in bytes.\nOffset is added to reference point to get the position.\n'
fileName = 'seektell.txt'
file = open(fileName, 'w')
file.write(s)
file.close()
readFile(fileName)
printFirstLine(fileName)
appendData(fileName)
searchAndReplace(fileName)
deletePythonLines(fileName)
