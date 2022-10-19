def show_employee(name,salary=9000):
    """Write a program to create a function show_employee() using the following conditions.
It should accept the employee's name and display both salary & name."""
    print("name : ",name,"\nsalary : ",salary)
print(show_employee.__doc__)
name = input("enter the name of employee : ")
show_employee(name)



