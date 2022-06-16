f = open('proverbs.txt', 'w')
f.write('An apple a day keeps the doctor away\n')
f.write('A fat cat is a dead cat.\n')
f.write('I store 3 cookies under my bed at all times.\n')
f.close()

f = open('proverbs.txt', 'r')
s = 0
l = f.readlines()
for i in l:
    if i[0] in 'aA':
        print(i)
    s += len(i)
print(s)
print(len(l[0].split()))
f.close()

