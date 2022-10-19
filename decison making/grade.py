'''A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.'''
marks = float(input("enter the marks you get in the exams out of 100 : "))
if 0 < marks <= 100: #---> mistake is here <=(missing)
    if marks <= 25:
        print("FAIL")  
    elif 25 <= marks <= 45:
        print("pass(E)")
    elif 45 <= marks <= 50:
        print("pass(D)")
    elif 50 <= marks <= 60:
        print("pass(C)")
    elif 60 <= marks <= 80:
        print("pass(B)")
    elif 80<= marks <=100:
        print("pass(A)")
else:
    print("enter valid marks")
