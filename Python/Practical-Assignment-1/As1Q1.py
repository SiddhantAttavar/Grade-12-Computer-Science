def createFile(data):
    f = open('File1.txt', 'w+')
    f.write(data)
    f.seek(0)
    return f

def readFileLines(file):
    l = file.readlines()
    for i in l:
        print(i.strip())
    file.seek(0)

def fileCount(file):
    s = file.read()
    print('"File" count:', s.count('file') - s.count('files'))
    file.seek(0)

def wordCount(file):
    print('Word count:', len(file.read().split()))
    file.seek(0)

def stWords(file):
    for word in file.read().split():
       if word and word[0] in 'stST':
        print(word)
    file.seek(0)

s = 'Text File\nThese files can be read by human directly.\nEach line is terminated by a special character, known as EOL.\nProcessing of file is slower than binary file.\nBinary File\nThese files cannot be read by humans directly.\nNo delimeter for a line.\nProcessing of file is faster than text file.'
file = createFile(s)
readFileLines(file)
fileCount(file)
wordCount(file)
stWords(file)
file.close()
