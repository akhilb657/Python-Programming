n = int(input("Enter number of employees: "))
employees = {}
for i in range(n):
    name = input("Enter employee name: ")
    sal = int(input("Enter salary of the employee: "))
    employees[name] = sal

print("Employee details are saved, now you can know the employee details")
while(True):
    name = input("Enter employee name: ")
    salary = employees.get(name,-1)
    if salary == -1:
        print("Employee does not exist")
    else:
        print("Salary of the employee is",salary)
    option = input("Do you want details of another employee[Yes/No]")

    if option == 'No':
        break