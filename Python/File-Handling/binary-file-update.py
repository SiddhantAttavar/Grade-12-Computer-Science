import pickle

def write(fileName, data):
    file = open(fileName, 'wb')
    for i in data:
        pickle.dump(i, file)
    file.close()
    
def read(fileName):
    l = []
    with open(fileName, 'rb') as file:
        try:
            while True:
                l.append(pickle.load(file))
        except:
            pass
    return l

x = int(input('Enter integer: '))
i = int(input('Enter index: '))
l = read('binary-file-update.bin')
if len(l) > i:
    l[i] = x
else:
    l.append(x)
write('binary-file-update.bin', l)
for i in l:
    print(i)
