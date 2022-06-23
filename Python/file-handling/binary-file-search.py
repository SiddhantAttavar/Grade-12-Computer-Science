import pickle

def write(data):
    file = open('binary-file-search.bin', 'wb')
    pickle.dump(data, file)
    file.close()

def search(code):
    file = open('binary-file-search.bin', 'rb')
    try:
        data = pickle.load(file)
        file.close()
    except:
        file.close()
        return []
    if code in data:
        return data[code]
    return []

data = {
    0: ['A', 'D1'],
    1: ['B', 'D2'],
    2: ['C', 'D3'],
    3: ['D', 'D4']
}
write(data)
l = search(2)
if len(l) == 2:
    print(l[0], l[1])
else:
    print('Employee not found')
