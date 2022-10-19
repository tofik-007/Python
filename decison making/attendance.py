# A student will not be allowed to sit in exam if his/her attendence 
# is less than 75%.
# Take following input from user

# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.s
'''''
def health_issue():
    y =input("any health issues y/n : ")
    if y == "y":
        print("you are allowed to sit in the exams")
    else:
        print("sorry you are not allowed to sit in exams")
'''
tot_class = int(input("enter anumber of classes are held till today :"))
attended_class = int(input("enter a number of attended classes by you among given classes :"))
# attendance= float(attended_class/tot_class)*100
attendance= (attended_class/tot_class)*100
if attendance > 75:
    print("total percentage of attendance is",attendance)
    print("you are allowed to sit in the exams")
else:
    print("total percentage of attendance is",attendance)
    print("you are not allowed to sit in exams")
    yes = input("any health issues yes/no :")
    if yes == "yes":
        print("you are allowed to sit in the exams .")
    else:
        print("you are not allowed to sit in the exams.")
    # health_issue()