n = int(input('enter the number of employees'))
employees = {}
for i in range(n):
    name = input('enter employee name')
    salary = input('enter employee salary')
    employees[name] = salary

print("give a name to know their salary")
while True:
    name = input('enter employee name')
    salary = employees.get(name, -1)
    if salary == -1:
        print("employee does not exist")
    else:
        print('employee salary is', salary)
    choice = input('do you want another employee details[Yes|No]')
    if choice.lower() == 'no':
        break
