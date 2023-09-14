employee_file = open("employees.txt", "r")
print(employee_file.read())

print(employee_file.readline())
print(employee_file.readline())
employee_file.close()
