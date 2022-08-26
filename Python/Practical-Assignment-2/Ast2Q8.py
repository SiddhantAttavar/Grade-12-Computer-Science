import pickle

def displayDetails(fileName):
    f = open(fileName, 'rb')
    l = pickle.load(f)
    print('Sname', 'Duration', 'Status', 'Fees', sep = '\t')
    for i in l:
        print(*i.values(), sep = '\t')
    f.close()

def longCourses(fileName):
    f = open(fileName, 'rb')
    l = pickle.load(f)
    print('Sname', 'Duration', 'Status', 'Fees', sep = '\t')
    for i in l:
        if i['Duration'] > 6:
            print(*i.values(), sep = '\t')
    f.close()

def updateRecords(fileName):
    sName = input('Enter Sname: ')
    status = input('Enter status: ')
    f = open(fileName, 'rb')
    l = pickle.load(f)
    f.close()
    for i in l:
        if i['Sname'] == sName:
            i['Status'] = status
    f = open(fileName, 'wb')
    pickle.dump(l, f)
    f.close()

def deleteNARecords(fileName):
    f = open(fileName, 'rb')
    l = pickle.load(f)
    f.close()
    newL = []
    for i in l:
        if i['Status'] != 'NA':
            newL.append(i)
    f = open(fileName, 'wb')
    pickle.dump(newL, f)
    f.close()
    displayDetails(fileName)

data = [
    ['Basketball', 6, 'On Going', 1000],
    ['Chess', 3, 'Scheduled', 650],
    ['Cricket', 10, 'On Going', 1000],
    ['Esports', 4, 'NA', 200],
    ['Football', 3, 'NA', 100]
]
l = []
for i in data:
    l.append({
        'Sname': i[0],
        'Duration': i[1],
        'Status': i[2],
        'Fees': i[3],
    })
fileName = 'sports.dat'
f = open(fileName, 'wb')
pickle.dump(l, f)
f.close()
displayDetails(fileName)
longCourses(fileName)
updateRecords(fileName)
deleteNARecords(fileName)