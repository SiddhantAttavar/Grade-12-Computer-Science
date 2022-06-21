def createFile(file, data):
    file.write(data)
    file.seek(0)

def writeALines(file):
    outFile = open('TextA.txt', 'w')
    for line in file:
        if line[0] in 'aA':
            outFile.write(line)
    file.seek(0)
    outFile.close()

def copyThe(file):
    outFile = open('Copy.txt', 'w+')
    for line in file:
        if 'the' in line:
            outFile.write(line)
    file.seek(0)
    outFile.seek(0)
    print(file.read())
    print(outFile.read())
    file.seek(0)
    outFile.close()

def fewVowelWords(file):
    for word in file.read().split():
        s = 'aeiouAEIOU'
        r = 0
        for c in s:
            r += word.count(c)
        if word.isalpha() and r < 3:
            print(word)
    file.seek(0)

def threeLetterWords(file):
    for word in file.read().split():
        if word.isalpha() and len(word) < 3:
            print(word)
    file.seek(0)

s = 'An apple a day keeps the doctor away.\nProverb 2\nProverb 3\nProverb 4\nProverb 5\n'
file = open('proverb.txt', 'w+')
createFile(file, s)
writeALines(file)
copyThe(file)
fewVowelWords(file)
threeLetterWords(file)
file.close()
