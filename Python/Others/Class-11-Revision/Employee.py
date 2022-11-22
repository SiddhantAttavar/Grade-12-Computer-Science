'''
Input the code name and salary of n employees, and store it in a nested dictionary.
Tax percentage is 2%, allowance is 3%
Deduct tax and add allowance
Add final salary to the dictionary
Print results in tabular format
'''

n = int(input('Enter no. of employees: '))
employees = {}
for i in range(n):
	code = int(input('Enter employee code: '))
	name = input('Enter employee name: ')
	salary = int(input('Enter employee salary: '))
	employees[code] = {
		'name': name,
		'salary': salary,
		'fin_salary': salary * 1.01
	}

print('Code', 'Name', 'Salary', 'Final Salary', sep = '\t')
for k, v in employees.items():
	print(k, v['name'], v['salary'], v['fin_salary'], sep = '\t')