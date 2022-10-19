# Take input of age of 3 people by user and determine oldest and
#  youngest among them.
james = int(input("enter the age of james : "))
sam = int(input("enter the age of sam : "))
ethan = int(input("enter the age of ethan : "))
if james > sam and james > ethan:
    print("james is oldest among all")
elif sam > james and sam > ethan :
    print("sam is oldest among all")
elif ethan > james and ethan > sam:
    print("ethan is oldest among all")
else:
    print("all are equal")