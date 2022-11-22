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

def add_emp(f):
    emp_code = input('Enter employee code: ')
    name = input('Enter name: ')
    dept = input('Enter department: ')
    email = input('Enter email: ')
    salary = input('Enter salary: ')
    f.write(','.join((emp_code, name, dept, email, salary)))
    return f

def delete_dept(f):
    f.seek(0)
    dept = input('Enter department: ')
    data = f.readlines()
    newData = []
    for i in range(len(data)):
        l = data[i].strip().split(',')
        if l[2] != dept:
            newData.append(data)
        data[i] = ','.join(l)
    f = open('employee.csv', 'w+')
    for i in newData:
        f.write(','.join(i) + '\n')
    return f

def Rnames(f):
    f.seek(0)
    data = f.readlines()
    for i in data:
        l = i.strip().split(',')
        if l[1][0] == 'R':
            print(i)
    return f

f = open('employee.csv', 'w+')
while True:
    op = input('Enter operation: Create (C) / Add (A) / Delete (D) / Display (R) / Exit (E): ').upper()
    if op == 'C':
        f = emp_data(f)
    elif op == 'A':
        f = add_emp(f)
    elif op == 'D':
        f = delete_dept(f)
    elif op == 'R':
        f = Rnames(f)
    else:
        break
f.close()