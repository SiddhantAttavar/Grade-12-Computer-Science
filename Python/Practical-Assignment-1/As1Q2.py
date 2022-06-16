def createFile(data):
    file = open('File2.txt', 'w+')
    file.write(data)
    file.seek(0)
    return file

def numChars(file):
    u = l = p = 0
    for c in file.read():
        u += c.isupper()
        l += c.islower()
        p += not c.isalnum() and c not in ' \n'
    file.seek(0)
    return u, l, p

def lineVowelCount(file):
    for line in file.readlines():
        s = 0
        for c in line:
            s += c in 'aeiouAEIOU'
        print('Vowels:', s)
    file.seek(0)

def pLines(file):
    for line in file.readlines():
        if line[0] in 'pP':
            print(line.strip())
    file.seek(0)

def fileSize(file):
    print('File Size:', len(file.read()))
    file.seek(0)

def lineCount(file):
    print('Line count:', len(file.readlines()))
    file.seek(0)

s = 'Python is a multi-paradigm, object-oriented and structured programming language.\nPython is an example of a FLOSS (Free/Libre and Open Source Software).\nDue to its open-source nature, Python has been ported to many platforms.\nYou can use Python on Linux, Windows, FreeBSD, Macintosh, Solaris, OS/2, Amiga, AROS, AS/400, BeOS, OS/390, z/OS, Palm OS, QNX, VMS, Psion, Acorn RISC OS, VxWorks, PlayStation, Sharp Zaurus, Windows CE and even PocketPC!'
file = createFile(s)
u, l, p = numChars(file)
print('Upper:', u)
print('Lower:', l)
print('Punc:', p)
lineVowelCount(file)
pLines(file)
fileSize(file)
lineCount(file)
file.close()
