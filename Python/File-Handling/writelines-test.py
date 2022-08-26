def write():
    f = open('writelines-test.txt', 'w')
    f.writelines([
        'Phrase 1\n',
        'Hello World'
    ])
    f.close()

def linesStartingWithP():
    f = open('writelines-test.txt', 'r')
    for l in f.readlines():
        if l[0] in 'pP':
            print(l.strip())
    f.close()

def numLines():
    f = open('writelines-test.txt', 'r')
    print(len(f.readlines()))
    f.close()

def numChars():
    f = open('writelines-test.txt', 'r')
    print(len(f.read()))
    f.close()

write()
linesStartingWithP()
numLines()
numChars()
