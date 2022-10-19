print("function arguement ")

print("required arguements : ")
#in this if parameter isn't given it shows syntax error

def printme( str ):
   "This prints a passed string into this function"
   print (str)

printme(str = "james")

print("keyword arguments : ")
#assign input for function's parameter at the time of function call
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name:", name)
   print ("Age:", age)

printinfo( age=21, name="TAufik" )

print("default arguements")
#default arguement for parameters set at the time of declaration of function
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)

printinfo( name="miki" )

print("variable length arguements ")

def printInfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ",arg1)
   for var in vartuple:
      print (var)

printInfo( 10 )
printInfo( 70, 60, 50 ,4556 , 4587 , 102225 )