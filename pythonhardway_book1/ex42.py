# late grade
totalpoints = input("How many points did you score? " )
late = input("Was the assignment late? True of False  ")

if late == True:
    print("Your work was late and your score is:", int(totalpoints) / 2)
else:
    print("Your Grade is: ", totalpoints)