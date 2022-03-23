totalpoints = int(input("What was the total number of points you earned? "))
late=input("Was the assignment late?  True or False")

if late == False:
    print("Great job! your total points are: ", totalpoints)
else:
    lategrade = totalpoints/2
    print("Sorry but you lose points. Your new total is: ", lategrade)