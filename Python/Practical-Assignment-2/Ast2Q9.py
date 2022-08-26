def emp_data(f):
    f.seek(0)
    data = [
        ['9012', 'Rachel', 'Sales', 'rachel@company.com', '56000'],
        ['2070', 'Rahul', 'Production', 'rahul@company.com', '65000'],
        ['4081', 'Sam', 'Sales', 'sam@company.com', '55000'],
        ['5079', 'Raj', 'Engineering', 'raj@company.com', '67000'],
    ]
    f.close()
    f = open('employee.csv', 'w+')
    for i in data:
        f.write(','.join(i) + '\n')
        print(*i, sep = ',')
    return f

def total_salary(f):
    f.seek(0)
    res = 0
    for i in f.readlines():
        l = i.strip().split(',')
        res += int(l[4])
    print(res)
    return f

def max_salary(f):
    f.seek(0)
    res = []
    for i in f.readlines():
        l = i.strip().split(',')
        if len(res) == 0 or l[4] > res[0][4]:
            res = [l]
        elif l[4] == res[0][4]:
            res.append(l)
    for i in res:
        print(*i, sep = '\t')
    return f

def change_dept(f):
    f.seek(0)
    emp_code = input('Enter employee code: ')
    dept = input('Enter department: ')
    data = f.readlines()
    for i in range(len(data)):
        l = data[i].strip().split(',')
        if l[0] == emp_code:
            l[2] = dept
        data[i] = ','.join(l)
    f = open('employee.csv', 'w+')
    for i in data:
        f.write(i + '\n')
    return f

f = open('employee.csv', 'w+')
while True:
    op = input('Enter operation: Create (C) / Total (T) / Max (M) / Change (D) / Exit (E): ').upper()
    if op == 'C':
        f = emp_data(f)
    elif op == 'T':
        f = total_salary(f)
    elif op == 'M':
        f = max_salary(f)
    elif op == 'D':
        f = change_dept(f)
    else:
        break
f.close()