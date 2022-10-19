# Ask user to enter age, gender ( M or F ) and then using following
#  rules print their place of service.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# And any other input of age should print "ERROR".
print (".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
age = float(input("Enter age (must be greater than 21) \n")) #absence of int at first create errors
if age>=21 and age <=60:
  gender = input("gender (m or f) : \n")
  if gender == "m" or gender == "f":
    if gender == "f" : 
      print ("you will work in Urban areas only .")
    elif gender == "m" and 21<=age<=40:
      print ("You can work anywhere urban/rural .")
    elif gender == "m" and 40<age<=60:
      print ("you will work in Urban areas only .")
  else:
    print("invalid input for gender")
else:
    print("invalid input for age")



