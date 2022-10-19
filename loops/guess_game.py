print("it's the guess game predict the number in less number of steps and you will be rewarded.")
run = True
while run == True:
    num = float(input("enter your guessed number :"))
    if num in range(0,10):
        if num == 5:
            print("correct , you won tesla s1")
            run = False
        elif num < 5:
            print("guess higher")
        elif num > 5:
            print("guess lower")
    else:
        print("be in range of 0 to 10")   