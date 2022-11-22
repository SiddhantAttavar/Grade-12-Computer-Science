def write():
    f = open('File2a.txt', 'w')
    f.write('Python is a multi-paradigm, object-oriented and structured programming language.\n')
    f.write('Python is an example of a FLOSS (Free/Libre and Open Source Software).\n')
    f.write('Due to its open-source nature, Python has been ported to many platforms.\n')
    f.write('You can use Python on Linux, Windows, FreeBSD, Macintosh, Solaris, OS/2, Amiga, AROS, AS/400, BeOS, OS/390, z/OS, Palm OS, QNX, VMS, Psion, Acorn RISC OS, VxWorks, PlayStation, Sharp Zaurus, Windows CE and even PocketPC!\n')
    f.close()

def countAlpha():
    f = open('File2a.txt', 'r')
    u = l = p = 0
    for c in f.read():
        if c.isalpha():
            l += c.islower()
            u += c.isupper()
        else:
            p += not c.isalnum() and c not in ' \n'
    print('Upper:', u)
    print('Lower:', l)
    print('Puncutation:', p)
    f.close()

def countVowel():
    f = open('File2a.txt', 'r')
    for l in f.read().split('\n'):
        s = 0
        for c in l:
            s += c in 'aeiouAEIOU'
        print('Vowels:', s)
    f.close()

write()
countAlpha()
countVowel()

