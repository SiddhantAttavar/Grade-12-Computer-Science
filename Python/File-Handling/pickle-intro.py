import pickle

def read():
    f = open('file.bin', 'rb')
    try:
        while True:
            print(pickle.load(f))
    except EOFError:
        return
    f.close()

def write():
    f = open('file.bin', 'wb')
    while True:
        pickle.dump(input('Enter data: '), f)
        if input('Press y to continue: ').lower() != 'y':
            break
    f.close()

write()
read()
