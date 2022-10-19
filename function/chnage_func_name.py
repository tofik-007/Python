def display_student(name,age):
    """Assign a different name to function and call it through the new name"""
    print("name : ",name,"\nage : ",age)
print(display_student.__doc__)
name,age = map(str, input("first give name and then age having space between : ").split())
show_student = display_student 
show_student(name,age)